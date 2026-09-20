"""Investigate customer identifiers and repeat-purchase definitions."""

from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "raw_data"
OUT = BASE / "profiling"
OUT.mkdir(exist_ok=True)

customers = pd.read_csv(
    RAW / "olist_customers_dataset.csv", dtype="string"
)
orders = pd.read_csv(
    RAW / "olist_orders_dataset.csv", dtype="string"
)

# Validate identifiers before joining.
for column in ["customer_id", "customer_unique_id"]:
    assert customers[column].notna().all(), f"Missing {column}"
    assert customers[column].str.strip().ne("").all(), (
        f"Blank {column}"
    )

assert customers["customer_id"].is_unique
assert orders["order_id"].notna().all()
assert orders["order_id"].is_unique
assert orders["customer_id"].notna().all()
assert orders["customer_id"].isin(customers["customer_id"]).all()

linked = orders.merge(
    customers[["customer_id", "customer_unique_id"]],
    on="customer_id",
    how="left",
    validate="many_to_one",
)

assert len(linked) == len(orders)
assert linked["customer_unique_id"].notna().all()

identity_checks = pd.DataFrame([
    {
        "Check": "Customer records",
        "Count": len(customers),
    },
    {
        "Check": "Distinct customer_id values",
        "Count": customers["customer_id"].nunique(),
    },
    {
        "Check": "Distinct customer_unique_id values",
        "Count": customers["customer_unique_id"].nunique(),
    },
    {
        "Check": "Orders",
        "Count": len(orders),
    },
    {
        "Check": "Customer IDs linked to multiple orders",
        "Count": int(
            orders.groupby("customer_id").size().gt(1).sum()
        ),
    },
    {
        "Check": "Unique customer IDs with multiple customer records",
        "Count": int(
            customers.groupby("customer_unique_id")
            ["customer_id"].nunique().gt(1).sum()
        ),
    },
])

# Compare two explicit definitions instead of mixing order statuses.
populations = {
    "All orders": linked,
    "Delivered orders only": linked.loc[
        linked["order_status"].eq("delivered")
    ],
}

summaries = []
distributions = []

for population, frame in populations.items():
    counts = frame.groupby("customer_unique_id")["order_id"].nunique()

    customer_count = len(counts)
    repeat_count = int(counts.ge(2).sum())
    order_count = int(counts.sum())

    summaries.append({
        "Population": population,
        "Orders": order_count,
        "Unique Customers": customer_count,
        "One-Order Customers": int(counts.eq(1).sum()),
        "Repeat Customers": repeat_count,
        "Repeat Customer Rate %": (
            round(repeat_count / customer_count * 100, 2)
            if customer_count else None
        ),
        "Orders From Repeat Customers": int(
            counts.loc[counts.ge(2)].sum()
        ),
        "Additional Orders Beyond First": int(
            (counts - 1).sum()
        ),
        "Maximum Orders Per Customer": (
            int(counts.max()) if customer_count else 0
        ),
    })

    frequency = counts.value_counts().sort_index()

    for orders_per_customer, number_of_customers in frequency.items():
        distributions.append({
            "Population": population,
            "Orders Per Customer": int(orders_per_customer),
            "Number of Customers": int(number_of_customers),
        })

    # Check that customer-level aggregation preserves order counts.
    assert order_count == frame["order_id"].nunique()

summary = pd.DataFrame(summaries)
distribution = pd.DataFrame(distributions)

identity_checks.to_csv(
    OUT / "phase_04_identity_checks.csv", index=False
)
summary.to_csv(
    OUT / "phase_04_customer_summary.csv", index=False
)
distribution.to_csv(
    OUT / "phase_04_order_frequency.csv", index=False
)

print("\nIDENTITY CHECKS")
print(identity_checks.to_string(index=False))

print("\nCUSTOMER SUMMARY")
print(summary.to_string(index=False))

print("\nORDER FREQUENCY")
print(distribution.to_string(index=False))

print("\nIDENTIFIER DECISIONS")
print("Order-level customer link: customer_id")
print("Distinct customer identity: customer_unique_id")
print("Repeat customer: customer_unique_id with >= 2 distinct order_id")
print("Primary repeat-purchase metric: delivered orders only")
print("All-order repeat activity: reported separately")
print(
    "customer_unique_id is the dataset's customer identity proxy; "
    "it does not independently verify a real person."
)
print(
    "Repeat status applies only within this dataset's observation window."
)

print("\nThree Phase 04 reports saved in profiling/")