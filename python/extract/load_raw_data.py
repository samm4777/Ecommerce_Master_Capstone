import pandas as pd
import os

from python.config.config import RAW_DATA_PATH


def load_csv(file_name):

    file_path = os.path.join(
        RAW_DATA_PATH,
        file_name
    )

    df = pd.read_csv(
        file_path
    )

    print(
        f"{file_name}: {df.shape}"
    )

    return df



if __name__ == "__main__":


    customers = load_csv(
        "olist_customers_dataset.csv"
    )


    print(
        customers.head()
    )