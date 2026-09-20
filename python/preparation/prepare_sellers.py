"""
Phase 06:
Prepare Sellers Data

Responsible for:
- Loading raw seller data
- Checking missing values
- Removing duplicate records
- Saving prepared output
"""

import pandas as pd

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH


def prepare_sellers():

    print("Loading sellers data...")

    df = load_csv(
        "olist_sellers_dataset.csv"
    )

    print("Original shape:")
    print(df.shape)

    print("\nOriginal columns:")
    print(df.columns)


    print("\nMissing values:")
    print(df.isnull().sum())


    # Remove duplicate sellers
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(
        f"\nDuplicates removed: {before-after}"
    )


    # Save prepared data

    output_file = (
    str(OUTPUT_PATH)
    + "/sellers_prepared.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"\nSaved: {output_file}"
    )


    print(df.shape)



if __name__ == "__main__":

    prepare_sellers()