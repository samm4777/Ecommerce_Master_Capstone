import pandas as pd
import os

from python.config.config import OUTPUT_PATH



def check_table(file_name, key_columns):

    path = os.path.join(
        OUTPUT_PATH,
        file_name
    )


    df = pd.read_csv(path)


    print("\n====================")
    print(file_name)
    print("====================")


    # Row count

    print(
        "Rows:",
        len(df)
    )


    # Missing keys

    print("\nMissing key values:")

    print(
        df[key_columns]
        .isnull()
        .sum()
    )


    # Duplicate keys

    print("\nDuplicate keys:")

    print(
        df.duplicated(
            subset=key_columns
        )
        .sum()
    )



def run_quality_checks():


    check_table(
        "customers_prepared.csv",
        [
            "customer_id"
        ]
    )


    check_table(
        "orders_prepared.csv",
        [
            "order_id"
        ]
    )


    check_table(
        "order_items_prepared.csv",
        [
            "order_id",
            "order_item_id"
        ]
    )


    check_table(
        "payments_prepared.csv",
        [
            "order_id",
            "payment_sequential"
        ]
    )


    check_table(
        "products_prepared.csv",
        [
            "product_id"
        ]
    )



if __name__ == "__main__":

    run_quality_checks()