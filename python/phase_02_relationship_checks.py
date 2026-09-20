"""
Phase 02: Relationship and Orphan Record Checks

Purpose:
Check relationships between Olist datasets
and identify orphan records.
"""

import pandas as pd
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_PATH, "raw_data")

OUTPUT_PATH = os.path.join(BASE_PATH, "profiling")


# Load datasets

customers = pd.read_csv(
    os.path.join(RAW_PATH, "olist_customers_dataset.csv")
)

orders = pd.read_csv(
    os.path.join(RAW_PATH, "olist_orders_dataset.csv")
)

order_items = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_items_dataset.csv")
)

payments = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_payments_dataset.csv")
)

reviews = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_reviews_dataset.csv")
)

products = pd.read_csv(
    os.path.join(RAW_PATH, "olist_products_dataset.csv")
)

sellers = pd.read_csv(
    os.path.join(RAW_PATH, "olist_sellers_dataset.csv")
)


results = []


# Orders -> Customers

orphan_orders_customer = (
    orders[~orders["customer_id"].isin(customers["customer_id"])]
    .shape[0]
)

results.append({
    "Relationship": "Orders to Customers",
    "Orphan Records": orphan_orders_customer
})


# Order Items -> Orders

orphan_items_orders = (
    order_items[~order_items["order_id"].isin(orders["order_id"])]
    .shape[0]
)

results.append({
    "Relationship": "Order Items to Orders",
    "Orphan Records": orphan_items_orders
})


# Payments -> Orders

orphan_payments_orders = (
    payments[~payments["order_id"].isin(orders["order_id"])]
    .shape[0]
)

results.append({
    "Relationship": "Payments to Orders",
    "Orphan Records": orphan_payments_orders
})


# Reviews -> Orders

orphan_reviews_orders = (
    reviews[~reviews["order_id"].isin(orders["order_id"])]
    .shape[0]
)

results.append({
    "Relationship": "Reviews to Orders",
    "Orphan Records": orphan_reviews_orders
})


# Order Items -> Products

orphan_items_products = (
    order_items[~order_items["product_id"].isin(products["product_id"])]
    .shape[0]
)

results.append({
    "Relationship": "Order Items to Products",
    "Orphan Records": orphan_items_products
})


# Order Items -> Sellers

orphan_items_sellers = (
    order_items[~order_items["seller_id"].isin(sellers["seller_id"])]
    .shape[0]
)

results.append({
    "Relationship": "Order Items to Sellers",
    "Orphan Records": orphan_items_sellers
})


# Save result

relationship_df = pd.DataFrame(results)

relationship_df.to_csv(
    os.path.join(
        OUTPUT_PATH,
        "relationship_orphan_report.csv"
    ),
    index=False
)


print("Relationship checks completed.")
print(relationship_df)