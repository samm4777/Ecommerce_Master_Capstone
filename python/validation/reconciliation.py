"""
Phase 11:
Data Reconciliation
Raw -> Python -> SQL
"""

import pandas as pd
from pathlib import Path


OUTPUT_PATH = Path("python/output")

RECON_PATH = Path("reconciliation")


def run_reconciliation():

    RECON_PATH.mkdir(exist_ok=True)


    orders = pd.read_csv(
        OUTPUT_PATH / "orders_prepared.csv"
    )

    order_items = pd.read_csv(
        OUTPUT_PATH / "order_items_prepared.csv"
    )

    customers = pd.read_csv(
        OUTPUT_PATH / "customers_prepared.csv"
    )

    payments = pd.read_csv(
        OUTPUT_PATH / "payments_prepared.csv"
    )


    results = []


    results.append(
        ["Total Orders", len(orders)]
    )

    results.append(
        [
            "Delivered Orders",
            (orders["order_status"]=="delivered").sum()
        ]
    )

    results.append(
        [
            "Cancelled Orders",
            (orders["order_status"]=="canceled").sum()
        ]
    )


    results.append(
        [
            "Order Items",
            len(order_items)
        ]
    )


    results.append(
        [
            "Customers",
            len(customers)
        ]
    )


    results.append(
        [
            "Merchandise Value",
            round(order_items["price"].sum(),2)
        ]
    )


    results.append(
        [
            "Freight Value",
            round(order_items["freight_value"].sum(),2)
        ]
    )


    results.append(
        [
            "Payment Value",
            round(payments["payment_value"].sum(),2)
        ]
    )


    df = pd.DataFrame(
        results,
        columns=[
            "Metric",
            "Python"
        ]
    )


    df.to_csv(
        RECON_PATH / "python_reconciliation.csv",
        index=False
    )


    print(df)


if __name__ == "__main__":
    run_reconciliation()