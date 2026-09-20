# Phase 06: Python Data Preparation

## Objective

Create a reproducible Python/Pandas data preparation process for the Olist e-commerce dataset.

## Tools Used

- Python
- Pandas

## Input Data

Raw CSV files from:

raw_data/

Original files were not modified manually.

## Preparation Performed

### Customers

Actions:
- Converted customer identifiers to string
- Treated postal code as identifier
- Checked duplicate records

Result:
- Rows processed: 99,441
- Duplicate records removed: 0

---

### Orders

Actions:
- Converted order dates to datetime
- Validated missing timestamps
- Checked duplicate records

Results:
- Rows processed: 99,441
- Duplicate records removed: 0

Missing timestamps found:
- order_approved_at: 160
- order_delivered_carrier_date: 1,783
- order_delivered_customer_date: 2,965

---

### Order Items

Actions:
- Preserved item-level grain
- Converted identifiers
- Validated duplicates

Result:
- Rows processed: 112,650
- Duplicate records removed: 0

---

### Payments

Actions:
- Preserved payment transaction grain
- Converted numeric fields
- Validated duplicates

Result:
- Rows processed: 103,886
- Duplicate records removed: 0

---

### Products

Actions:
- Converted product identifiers
- Handled missing categories
- Converted numeric attributes

Result:

Missing categories before:
610

Action:
Replaced missing category with "Unknown"

Missing categories after:
0

---

## Important Decisions

1. Raw CSV files were never modified.

2. Separate tables were maintained.
No single merged dataframe was created because it can create duplicate revenue, payment and freight calculations.

3. Customer identity decisions from Phase 04 were preserved.

4. Prepared datasets maintain original business grain.

## Output Files

- customers_prepared.csv
- orders_prepared.csv
- order_items_prepared.csv
- payments_prepared.csv
- products_prepared.csv

## Validation

All prepared tables passed:

- Row count validation
- Missing key validation
- Duplicate key validation

## Python Responsibility

Python was responsible for:

- Loading raw data
- Data type correction
- Missing value handling
- Data validation
- Creating SQL-ready prepared datasets