import pandas as pd

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH



def prepare_payments():

    print("\nLoading payments data...")


    payments = load_csv(
        "olist_order_payments_dataset.csv"
    )


    print("\nOriginal columns:")
    print(payments.columns)



    # Convert identifiers

    payments["order_id"] = (
        payments["order_id"]
        .astype(str)
    )



    # Convert payment values

    numeric_columns = [

        "payment_sequential",
        "payment_installments",
        "payment_value"

    ]


    for col in numeric_columns:

        payments[col] = pd.to_numeric(
            payments[col],
            errors="coerce"
        )



    # Missing value check

    print("\nMissing values:")

    print(
        payments.isnull().sum()
    )



    # Duplicate check

    before = len(payments)


    payments = (
        payments
        .drop_duplicates()
    )


    after = len(payments)


    print(
        "\nDuplicate rows removed:",
        before-after
    )



    # Save output

    output_file = (
        OUTPUT_PATH +
        "/payments_prepared.csv"
    )


    payments.to_csv(
        output_file,
        index=False
    )


    print(
        "\nSaved:",
        output_file
    )



if __name__ == "__main__":

    prepare_payments()