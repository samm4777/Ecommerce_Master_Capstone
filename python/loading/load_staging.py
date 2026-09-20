"""
Phase 10:
Load prepared CSV files into Azure SQL staging tables
"""


import pandas as pd

from python.config.database_config import get_engine


INPUT_PATH = "python/output"


def load_table(file_name, table_name):

    engine = get_engine()

    file_path = f"{INPUT_PATH}/{file_name}"

    print(f"Loading {file_name}...")


    df = pd.read_csv(file_path)


    df.to_sql(
        name=table_name,
        con=engine,
        schema="stg",
        if_exists="replace",
        index=False,
        chunksize=5000
    )


    print(
        f"Loaded {table_name}: {len(df)} rows"
    )



def load_staging():

    tables = {

    "customers_prepared.csv":
        "customers",

    "orders_prepared.csv":
        "orders",

    "order_items_prepared.csv":
        "order_items",

    "payments_prepared.csv":
        "payments",

    "products_prepared.csv":
        "products",

    "sellers_prepared.csv":
        "sellers",

    "reviews_prepared.csv":
        "reviews",

    "geolocation_prepared.csv":
        "geolocation",

    "category_translation_prepared.csv":
        "category_translation"
}


    for file_name, table_name in tables.items():

        load_table(
            file_name,
            table_name
        )


if __name__ == "__main__":

    load_staging()