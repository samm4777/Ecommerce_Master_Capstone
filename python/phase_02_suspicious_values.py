"""
Phase 02: Suspicious Values Check

Checks unusual values in raw datasets.
"""

import pandas as pd
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_PATH, "raw_data")
OUTPUT_PATH = os.path.join(BASE_PATH, "profiling")


results = []


# Orders status check

orders = pd.read_csv(
    os.path.join(RAW_PATH, "olist_orders_dataset.csv")
)

results.append({
    "Dataset": "orders",
    "Check": "Order Status Values",
    "Result": ", ".join(
        orders["order_status"].unique()
    )
})


# Payment values

payments = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_payments_dataset.csv")
)

results.append({
    "Dataset": "payments",
    "Check": "Negative Payment Values",
    "Result": str(
        (payments["payment_value"] < 0).sum()
    )
})


# Order item prices

items = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_items_dataset.csv")
)

results.append({
    "Dataset": "order_items",
    "Check": "Negative Product Prices",
    "Result": str(
        (items["price"] < 0).sum()
    )
})


# Product weight

products = pd.read_csv(
    os.path.join(RAW_PATH, "olist_products_dataset.csv")
)

results.append({
    "Dataset": "products",
    "Check": "Missing Product Weight",
    "Result": str(
        products["product_weight_g"].isna().sum()
    )
})


# Save report

pd.DataFrame(results).to_csv(
    os.path.join(
        OUTPUT_PATH,
        "suspicious_values_report.csv"
    ),
    index=False
)


print("Suspicious values check completed.")
print(pd.DataFrame(results))