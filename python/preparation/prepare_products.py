import pandas as pd

from python.extract.load_raw_data import load_csv
from python.config.config import OUTPUT_PATH



def prepare_products():

    print("\nLoading products data...")


    products = load_csv(
        "olist_products_dataset.csv"
    )


    print("\nOriginal columns:")
    print(products.columns)



    # Convert product ID

    products["product_id"] = (
        products["product_id"]
        .astype(str)
    )



    # Missing category handling

    print("\nMissing category values before:")

    print(
        products[
            "product_category_name"
        ]
        .isnull()
        .sum()
    )


    products[
        "product_category_name"
    ] = (
        products[
            "product_category_name"
        ]
        .fillna("Unknown")
    )



    # Numeric columns

    numeric_columns = [

        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"

    ]


    for col in numeric_columns:

        products[col] = pd.to_numeric(
            products[col],
            errors="coerce"
        )



    # Duplicate check

    before = len(products)


    products = (
        products
        .drop_duplicates()
    )


    after = len(products)


    print(
        "\nDuplicate rows removed:",
        before-after
    )



    print(
        "\nMissing category values after:"
    )

    print(
        products[
            "product_category_name"
        ]
        .isnull()
        .sum()
    )



    # Save

    output_file = (
        OUTPUT_PATH +
        "/products_prepared.csv"
    )


    products.to_csv(
        output_file,
        index=False
    )


    print(
        "\nSaved:",
        output_file
    )



if __name__ == "__main__":

    prepare_products()