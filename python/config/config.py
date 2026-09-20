import os


# Project Root
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


# Data Locations

RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    "raw_data"
)


OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "python",
    "output"
)


# Create output folder if missing

os.makedirs(
    OUTPUT_PATH,
    exist_ok=True
)


print("Base Directory:")
print(BASE_DIR)

print("\nRaw Data:")
print(RAW_DATA_PATH)

print("\nOutput:")
print(OUTPUT_PATH)