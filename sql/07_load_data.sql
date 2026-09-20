/*
Phase 09:
Data Loading Strategy

Loading sequence:

1. Python prepared CSV files
2. Staging tables
3. Dimension tables
4. Fact tables


Actual bulk loading can be performed using:
- Azure Data Studio Import Wizard
- SQL Server Import/Export Wizard
- Python SQLAlchemy pipeline
*/


-- Example loading order:

-- Step 1
-- Load CSV files into stg schema


-- Step 2
-- Populate dimensions

-- DimCustomer
-- DimProduct
-- DimCategory
-- DimSeller
-- DimGeography
-- DimDate


-- Step 3
-- Populate facts

-- FactOrders
-- FactOrderItems
-- FactPayments
-- FactReviews