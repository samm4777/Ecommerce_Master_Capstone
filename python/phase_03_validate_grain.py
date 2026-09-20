"""Validate source grain, candidate keys and relationship coverage."""

from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "raw_data"
OUT = BASE / "profiling"
OUT.mkdir(exist_ok=True)

files = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "categories": "product_category_name_translation.csv",
    "geolocation": "olist_geolocation_dataset.csv",
}

# Preserve identifiers and leading zeros in ZIP prefixes.
tables = {
    name: pd.read_csv(RAW / filename, dtype="string")
    for name, filename in files.items()
}

keys = []


def check_key(table, columns):
    df = tables[table]
    null_rows = int(df[columns].isna().any(axis=1).sum())
    duplicate_rows = int(df.duplicated(columns, keep=False).sum())

    keys.append({
        "Table": table,
        "Candidate Key": " + ".join(columns),
        "Null Key Rows": null_rows,
        "Rows in Duplicate Key Groups": duplicate_rows,
        "Result": (
            "PASS" if null_rows == 0 and duplicate_rows == 0
            else "INVESTIGATE"
        ),
    })


for table, columns in [
    ("customers", ["customer_id"]),
    ("orders", ["order_id"]),
    ("products", ["product_id"]),
    ("sellers", ["seller_id"]),
    ("categories", ["product_category_name"]),
    ("items", ["order_id", "order_item_id"]),
    ("payments", ["order_id", "payment_sequential"]),
    ("reviews", ["review_id"]),
    ("reviews", ["order_id", "review_id"]),
]:
    check_key(table, columns)

checks = []


def record(check, count):
    checks.append({"Check": check, "Count": int(count)})


orders = tables["orders"]
customers = tables["customers"]

customer_order_counts = orders.groupby("customer_id").size()

record(
    "Customer IDs associated with multiple orders",
    customer_order_counts.gt(1).sum(),
)
record(
    "Customer records unused by orders",
    (~customers["customer_id"].isin(orders["customer_id"])).sum(),
)
record(
    "Distinct customer_unique_id values",
    customers["customer_unique_id"].nunique(),
)

coverage = []

for table in ["items", "payments", "reviews"]:
    counts = tables[table].groupby("order_id").size()

    record(
        f"Orders with multiple {table} records",
        counts.gt(1).sum(),
    )

    missing = ~orders["order_id"].isin(counts.index)
    record(f"Orders without {table}", missing.sum())

    by_status = (
        orders.loc[missing]
        .groupby("order_status", dropna=False)
        .size()
    )

    for status, count in by_status.items():
        coverage.append({
            "Missing Child Table": table,
            "Order Status": status,
            "Order Count": int(count),
        })

products = tables["products"]
category = products["product_category_name"]

record("Products with missing category", category.isna().sum())
record(
    "Products with non-null unmatched category",
    (
        category.notna()
        & ~category.isin(tables["categories"]["product_category_name"])
    ).sum(),
)

geo = tables["geolocation"]
geo_prefixes = geo["geolocation_zip_code_prefix"].dropna()

record("Exact duplicate geolocation rows", geo.duplicated().sum())
record(
    "ZIP prefixes with multiple geolocation rows",
    geo_prefixes.value_counts().gt(1).sum(),
)

for table, column in [
    ("customers", "customer_zip_code_prefix"),
    ("sellers", "seller_zip_code_prefix"),
]:
    prefixes = tables[table][column]
    record(f"{table}: missing ZIP prefixes", prefixes.isna().sum())
    record(
        f"{table}: non-null unmatched ZIP prefixes",
        (prefixes.notna() & ~prefixes.isin(geo_prefixes)).sum(),
    )

raw_scores = tables["reviews"]["review_score"]
scores = pd.to_numeric(raw_scores, errors="coerce")

record("Missing review scores", raw_scores.isna().sum())
record(
    "Non-null invalid review scores",
    (
        raw_scores.notna()
        & ~scores.isin([1, 2, 3, 4, 5])
    ).sum(),
)

key_report = pd.DataFrame(keys)
relationship_report = pd.DataFrame(checks)
coverage_report = pd.DataFrame(
    coverage,
    columns=["Missing Child Table", "Order Status", "Order Count"],
)

key_report.to_csv(OUT / "phase_03_key_validation.csv", index=False)
relationship_report.to_csv(
    OUT / "phase_03_relationship_validation.csv", index=False
)
coverage_report.to_csv(
    OUT / "phase_03_missing_children_by_status.csv", index=False
)

print("\nKEY VALIDATION")
print(key_report.to_string(index=False))

print("\nRELATIONSHIP VALIDATION")
print(relationship_report.to_string(index=False))

print("\nMISSING CHILD RECORDS BY ORDER STATUS")
print(coverage_report.to_string(index=False))

print("\nThree validation reports saved in profiling/")