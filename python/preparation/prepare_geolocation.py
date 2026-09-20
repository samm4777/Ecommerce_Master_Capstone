"""
Phase 06:
Prepare Geolocation Data

Responsible for:
- Loading raw geolocation data
- Checking missing values
- Removing duplicates
- Saving prepared output
"""

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH


def prepare_geolocation():

    print("Loading geolocation data...")


    df = load_csv(
        "olist_geolocation_dataset.csv"
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
        + "/geolocation_prepared.csv"
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

    prepare_geolocation()