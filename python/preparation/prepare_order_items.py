import pandas as pd

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH



def prepare_order_items():

    print("\nLoading order items data...")


    items = load_csv(
        "olist_order_items_dataset.csv"
    )


    print("\nOriginal columns:")
    print(items.columns)


    # Convert identifiers

    id_columns = [

        "order_id",
        "product_id",
        "seller_id"

    ]


    for col in id_columns:

        items[col] = (
            items[col]
            .astype(str)
        )


    # Convert date

    items["shipping_limit_date"] = (
        pd.to_datetime(
            items["shipping_limit_date"],
            errors="coerce"
        )
    )


    # Check missing values

    print("\nMissing values:")

    print(
        items.isnull().sum()
    )


    # Duplicate check

    before = len(items)


    items = (
        items
        .drop_duplicates()
    )


    after = len(items)


    print(
        "\nDuplicate rows removed:",
        before-after
    )


    # Save output

    output_file = (
        OUTPUT_PATH +
        "/order_items_prepared.csv"
    )


    items.to_csv(
        output_file,
        index=False
    )


    print(
        "\nSaved:",
        output_file
    )



if __name__ == "__main__":

    prepare_order_items()