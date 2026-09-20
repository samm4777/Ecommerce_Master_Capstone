"""Verify order-level joins preserve source totals and counts."""

from pathlib import Path
from decimal import Decimal
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "raw_data"
OUT = BASE / "profiling"
OUT.mkdir(exist_ok=True)

orders = pd.read_csv(
    RAW / "olist_orders_dataset.csv", dtype="string"
)
items = pd.read_csv(
    RAW / "olist_order_items_dataset.csv", dtype="string"
)
payments = pd.read_csv(
    RAW / "olist_order_payments_dataset.csv", dtype="string"
)
reviews = pd.read_csv(
    RAW / "olist_order_reviews_dataset.csv", dtype="string"
)


def to_cents(series):
    """Use exact integer cents for financial reconciliation."""
    def convert(value):
        if pd.isna(value):
            raise ValueError("Missing monetary value found")
        cents = Decimal(value) * 100
        if cents != cents.to_integral_value():
            raise ValueError(f"Unexpected monetary precision: {value}")
        return int(cents)

    return series.map(convert).astype("int64")


assert orders["order_id"].notna().all()
assert orders["order_id"].is_unique

for name, frame in [
    ("items", items),
    ("payments", payments),
    ("reviews", reviews),
]:
    assert frame["order_id"].notna().all(), f"{name}: null order ID"
    assert frame["order_id"].isin(orders["order_id"]).all(), (
        f"{name}: orphan order ID"
    )

items["price_cents"] = to_cents(items["price"])
items["freight_cents"] = to_cents(items["freight_value"])
payments["payment_cents"] = to_cents(payments["payment_value"])
reviews["score"] = pd.to_numeric(
    reviews["review_score"], errors="raise"
)
assert reviews["score"].isin([1, 2, 3, 4, 5]).all()

item_totals = items.groupby("order_id", as_index=False).agg(
    item_count=("order_item_id", "size"),
    sales_cents=("price_cents", "sum"),
    freight_cents=("freight_cents", "sum"),
)

payment_totals = payments.groupby("order_id", as_index=False).agg(
    payment_count=("payment_sequential", "size"),
    payment_cents=("payment_cents", "sum"),
)

review_totals = reviews.groupby("order_id", as_index=False).agg(
    review_count=("review_id", "size"),
    score_sum=("score", "sum"),
    score_count=("score", "count"),
)

# Nullable integers preserve exact values through left joins.
for frame in [item_totals, payment_totals, review_totals]:
    for column in frame.columns:
        if column != "order_id":
            frame[column] = frame[column].astype("Int64")

overview = orders[["order_id", "order_status"]].copy()

for frame in [item_totals, payment_totals, review_totals]:
    overview = overview.merge(
        frame,
        on="order_id",
        how="left",
        validate="one_to_one",
    )

# Keep absent child records distinguishable from recorded zeros.
overview["has_items"] = overview["item_count"].notna()
overview["has_payments"] = overview["payment_count"].notna()
overview["has_reviews"] = overview["review_count"].notna()

results = []


def check(metric, before, after):
    before, after = int(before), int(after)
    results.append({
        "Metric": metric,
        "Before Join": before,
        "After Join": after,
        "Result": "PASS" if before == after else "FAIL",
    })


check("Order rows", len(orders), len(overview))
check(
    "Distinct orders",
    orders["order_id"].nunique(),
    overview["order_id"].nunique(),
)
check("Item records", len(items), overview["item_count"].sum())
check(
    "Merchandise sales (cents)",
    items["price_cents"].sum(),
    overview["sales_cents"].sum(),
)
check(
    "Freight (cents)",
    items["freight_cents"].sum(),
    overview["freight_cents"].sum(),
)
check(
    "Payment records",
    len(payments),
    overview["payment_count"].sum(),
)
check(
    "Payment value (cents)",
    payments["payment_cents"].sum(),
    overview["payment_cents"].sum(),
)
check(
    "Review records",
    len(reviews),
    overview["review_count"].sum(),
)
check(
    "Review score sum",
    reviews["score"].sum(),
    overview["score_sum"].sum(),
)
check(
    "Valid review score count",
    reviews["score"].count(),
    overview["score_count"].sum(),
)
check(
    "Reviewed orders",
    reviews["order_id"].nunique(),
    overview["has_reviews"].sum(),
)

report = pd.DataFrame(results)
report.to_csv(
    OUT / "phase_03_safe_join_validation.csv", index=False
)

print(report.to_string(index=False))
print("\nPopulation: all source orders, regardless of status.")
print("Financial totals are compared in exact integer cents.")
print("Missing child records remain missing in the overview.")

if report["Result"].eq("FAIL").any():
    raise AssertionError("Reconciliation failed; inspect the report.")

print("\nSUCCESS: all totals and counts survived the joins.")