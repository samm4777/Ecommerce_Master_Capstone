import pandas as pd

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH



def prepare_customers():


    customers = load_csv(
        "olist_customers_dataset.csv"
    )


    print(
        "\nOriginal Data Types"
    )

    print(
        customers.dtypes
    )


    # Convert IDs to string

    id_columns = [
        "customer_id",
        "customer_unique_id"
    ]


    for col in id_columns:

        customers[col] = (
            customers[col]
            .astype(str)
        )


    # Postal code is identifier
    customers[
        "customer_zip_code_prefix"
    ] = (
        customers[
            "customer_zip_code_prefix"
        ]
        .astype(str)
    )


    # Remove exact duplicates

    before = len(customers)


    customers = (
        customers
        .drop_duplicates()
    )


    after = len(customers)


    print(
        f"Duplicates removed: {before-after}"
    )


    # Save prepared file

    output_file = (
        OUTPUT_PATH +
        "/customers_prepared.csv"
    )


    customers.to_csv(
        output_file,
        index=False
    )


    print(
        "Saved:",
        output_file
    )



if __name__ == "__main__":

    prepare_customers()