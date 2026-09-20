"""
Phase 06:
Prepare Category Translation Data

Responsible for:
- Loading category translation data
- Checking missing values
- Removing duplicates
- Saving prepared output
"""

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH


def prepare_category_translation():

    print("Loading category translation data...")


    df = load_csv(
        "product_category_name_translation.csv"
    )


    print("Original shape:")
    print(df.shape)


    print("\nOriginal columns:")
    print(df.columns)


    print("\nMissing values:")
    print(df.isnull().sum())


    before = len(df)

    df = df.drop_duplicates()

    after = len(df)


    print(
        f"\nDuplicates removed: {before-after}"
    )


    output_file = (
        str(OUTPUT_PATH)
        + "/category_translation_prepared.csv"
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

    prepare_category_translation()