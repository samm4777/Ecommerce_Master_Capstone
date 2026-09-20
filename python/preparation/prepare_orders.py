import pandas as pd

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH



def prepare_orders():

    print("\nLoading orders data...")


    orders = load_csv(
        "olist_orders_dataset.csv"
    )


    print("\nOriginal columns:")
    print(orders.columns)


    # Convert order IDs to string

    orders["order_id"] = (
        orders["order_id"]
        .astype(str)
    )


    # Convert date columns

    date_columns = [

        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"

    ]


    for col in date_columns:

        orders[col] = pd.to_datetime(
            orders[col],
            errors="coerce"
        )


    # Check missing dates

    print("\nMissing date values:")

    print(
        orders[date_columns]
        .isnull()
        .sum()
    )


    # Remove exact duplicates only

    before = len(orders)


    orders = (
        orders
        .drop_duplicates()
    )


    after = len(orders)


    print(
        "\nDuplicate rows removed:",
        before-after
    )


    # Save prepared data

    output_file = (
        OUTPUT_PATH +
        "/orders_prepared.csv"
    )


    orders.to_csv(
        output_file,
        index=False
    )


    print(
        "\nSaved:",
        output_file
    )



if __name__ == "__main__":

    prepare_orders()