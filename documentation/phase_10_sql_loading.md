# Phase 10: SQL Server Loading

## Overview

This phase implements a reproducible loading process from prepared CSV files into the Azure SQL Server analytics database.

The loading architecture follows a layered approach:
Prepared CSV Files
|
|
v
Staging Layer (stg schema)
|
|
v
Dimension Layer (dim schema)
|
|
v
Fact Layer (fact schema)

The objective was to load data through scripts without manual database editing.

---

# 1. Loading Architecture

The Azure SQL database contains three main layers:

## Staging Layer

Purpose:

- Store prepared source data
- Maintain a copy of cleaned datasets before transformation
- Provide input for dimension and fact loading


Loaded staging tables:

| Table | Records |
|---|---:|
| customers | 99,441 |
| orders | 99,441 |
| order_items | 112,650 |
| payments | 103,886 |
| products | 32,951 |
| sellers | 3,095 |
| reviews | 99,224 |
| geolocation | 738,332 |
| category_translation | 71 |


---

# 2. Dimension Loading

Dimensions were populated from staging tables using SQL transformation logic.

Loaded dimensions:

| Dimension | Purpose |
|---|---|
| dim.Customer | Customer descriptive information |
| dim.Product | Product attributes |
| dim.Category | Product category information |
| dim.Seller | Seller information |
| dim.Geography | Location attributes |
| dim.Date | Date intelligence for analytics |


Surrogate keys were generated inside SQL Server identity columns.

Examples:

- customer_key
- product_key
- seller_key
- category_key
- geography_key
- date_key


---

# 3. Fact Loading

Fact tables were populated according to the grain defined in Phase 08.


## Fact Orders

Grain:

> One row represents one customer order.


Contains:

- order identifier
- customer key
- date key
- geography key
- order status
- delivery metrics


---

## Fact Order Items

Grain:

> One row represents one product item belonging to one customer order.


Contains:

- order key
- product key
- seller key
- price
- freight value


---

## Fact Payments

Grain:

> One row represents one payment transaction.


Contains:

- payment information
- payment value
- payment method


---

## Fact Reviews

Grain:

> One row represents one customer review.


Contains:

- order reference
- review score
- review details


---

# 4. Loading Scripts

The following scripts were created:
python/loading/

├── load_staging.py
├── load_dimensions.py
├── load_facts.py
└── test_connection.py

Responsibilities:

## load_staging.py

- Loads prepared CSV files
- Inserts records into staging tables


## load_dimensions.py

- Creates analytical dimensions
- Generates surrogate keys
- Applies required transformations


## load_facts.py

- Loads fact tables
- Maintains relationships with dimensions


## test_connection.py

- Validates Azure SQL connectivity


---

# 5. Reproducibility Approach

The loading process was designed to be repeatable.

Each execution:

1. Connects to Azure SQL database
2. Loads staging tables
3. Rebuilds dimensions
4. Rebuilds facts

No manual SQL record editing is required.

Running the scripts again produces the same analytical dataset.

---

# 6. Validation Results

Validation was performed in SQL Server Management Studio.

Successful checks:

## Fact Loading

| Fact Table | Status |
|---|---|
| fact.Orders | Loaded |
| fact.OrderItems | Loaded |
| fact.Payments | Loaded |
| fact.Reviews | Loaded |


## Relationship Validation

Checked:

- Fact orders linked with customers
- Order items linked with products
- Payments linked with orders


No loading failures remained after validation.

---

# 7. Technical Decisions

## Azure SQL Database

Azure SQL Database was selected as the analytical database platform.

Benefits:

- Cloud-hosted SQL Server compatibility
- Scalable analytical storage
- Integration support for future BI tools


## SQL Responsibility

SQL Server handled:

- Table relationships
- Primary keys
- Foreign keys
- Surrogate keys
- Data warehouse structure
- Analytical storage


Python handled:

- File loading automation
- Database connectivity
- Execution orchestration


---

# Phase 10 Completion Status

✅ Azure SQL database created  
✅ Staging data loaded  
✅ Dimensions loaded  
✅ Facts loaded  
✅ Loading scripts created  
✅ Validation completed  
✅ Reproducible process implemented