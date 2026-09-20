"""
Phase 02: Final Source Profiling Summary

Combines profiling outputs into one Excel report.
"""

import pandas as pd
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFILE_PATH = os.path.join(BASE_PATH, "profiling")


OUTPUT_FILE = os.path.join(
    PROFILE_PATH,
    "final_source_profiling_report.xlsx"
)


files = {
    "Dataset Summary": "dataset_summary.csv",
    "Missing Values": "missing_values_report.csv",
    "Data Types": "data_types_report.csv",
    "Unique Identifiers": "unique_identifier_report.csv",
    "Date Ranges": "date_range_report.csv",
    "Relationships": "relationship_orphan_report.csv",
    "Suspicious Values": "suspicious_values_report.csv"
}


with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:

    for sheet_name, file_name in files.items():

        file_path = os.path.join(
            PROFILE_PATH,
            file_name
        )

        df = pd.read_csv(file_path)

        df.to_excel(
            writer,
            sheet_name=sheet_name[:31],
            index=False
        )


print("Final profiling report created:")
print(OUTPUT_FILE)