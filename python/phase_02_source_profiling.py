"""
Phase 02: Source Data Profiling

Profiles all 9 Olist raw datasets before transformation.

Creates:
- Dataset summary
- Missing values report
- Data types report
- Unique identifier report
- Date range report
"""

import pandas as pd
import os


# Paths

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_PATH, "raw_data")
OUTPUT_PATH = os.path.join(BASE_PATH, "profiling")

os.makedirs(OUTPUT_PATH, exist_ok=True)


# Datasets

datasets = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}


dataset_summary = []
missing_report = []
datatype_report = []
identifier_report = []
date_report = []


for dataset_name, filename in datasets.items():

    print(f"Profiling {dataset_name}...")

    file_path = os.path.join(RAW_DATA_PATH, filename)

    df = pd.read_csv(file_path)


    # Dataset summary

    dataset_summary.append({
        "Dataset": dataset_name,
        "File": filename,
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Duplicate Rows": df.duplicated().sum(),
        "Memory Usage MB": round(df.memory_usage(deep=True).sum()/1024/1024,2)
    })


    # Missing values

    for column in df.columns:

        missing_report.append({
            "Dataset": dataset_name,
            "Column": column,
            "Missing Count": df[column].isna().sum(),
            "Missing Percentage": round(
                (df[column].isna().sum()/len(df))*100,2
            )
        })


    # Data types

    for column in df.columns:

        datatype_report.append({
            "Dataset": dataset_name,
            "Column": column,
            "Data Type": str(df[column].dtype)
        })


    # Unique identifiers

    for column in df.columns:

        unique_count = df[column].nunique()

        if unique_count == len(df):

            identifier_report.append({
                "Dataset": dataset_name,
                "Possible Unique Identifier": column,
                "Unique Values": unique_count
            })


    # Date columns

    for column in df.columns:

        if "date" in column:

            converted = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            date_report.append({
                "Dataset": dataset_name,
                "Column": column,
                "Minimum Date": converted.min(),
                "Maximum Date": converted.max(),
                "Invalid Dates": converted.isna().sum()
            })


# Save outputs

pd.DataFrame(dataset_summary).to_csv(
    os.path.join(OUTPUT_PATH, "dataset_summary.csv"),
    index=False
)

pd.DataFrame(missing_report).to_csv(
    os.path.join(OUTPUT_PATH, "missing_values_report.csv"),
    index=False
)

pd.DataFrame(datatype_report).to_csv(
    os.path.join(OUTPUT_PATH, "data_types_report.csv"),
    index=False
)

pd.DataFrame(identifier_report).to_csv(
    os.path.join(OUTPUT_PATH, "unique_identifier_report.csv"),
    index=False
)

pd.DataFrame(date_report).to_csv(
    os.path.join(OUTPUT_PATH, "date_range_report.csv"),
    index=False
)


print("\nProfiling completed successfully.")
print("Reports saved inside profiling folder.")