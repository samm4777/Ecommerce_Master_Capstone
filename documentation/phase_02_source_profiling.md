# Phase 02: Source Data Profiling

## 1. Phase Objective

The objective of this phase was to profile all 9 raw Olist datasets
before performing any transformation or cleaning.

The purpose of profiling was to understand:

-   Dataset structure
-   Data size
-   Columns
-   Data types
-   Missing values
-   Duplicate records
-   Unique identifiers
-   Date ranges
-   Suspicious values
-   Relationships between datasets
-   Orphan records
-   Data quality concerns

------------------------------------------------------------------------

## 2. Profiling Approach

A reproducible Python/Pandas profiling process was created.

The original CSV files stored in:

    raw_data/

were analyzed without modification.

All profiling outputs were saved in:

    profiling/

------------------------------------------------------------------------

## 3. Profiling Scripts Created

    python/

    phase_02_source_profiling.py
    phase_02_relationship_checks.py
    phase_02_suspicious_values.py
    phase_02_final_profiling_summary.py

------------------------------------------------------------------------

## 4. Profiling Outputs Generated

    profiling/

    dataset_summary.csv
    missing_values_report.csv
    data_types_report.csv
    unique_identifier_report.csv
    date_range_report.csv
    relationship_orphan_report.csv
    suspicious_values_report.csv
    final_source_profiling_report.xlsx

------------------------------------------------------------------------

## 5. Dataset Profiling Summary

All 9 Olist datasets were successfully profiled:

  Dataset                Purpose
  ---------------------- -----------------------------------
  customers              Customer information and location
  geolocation            ZIP code geographic information
  order_items            Products purchased inside orders
  order_payments         Payment details
  order_reviews          Customer review information
  orders                 Order lifecycle information
  products               Product attributes
  sellers                Seller information
  category_translation   Category name translation

------------------------------------------------------------------------

## 6. Data Quality Findings

### Duplicate Records

The profiling identified duplicate records:

-   Geolocation dataset contains duplicate rows.

This requires further investigation before analytical modeling.

### Missing Values

Important missing values identified:

#### Order Reviews

-   review_comment_title
-   review_comment_message

#### Orders

-   order_approved_at
-   order_delivered_carrier_date
-   order_delivered_customer_date

#### Products

-   product_category_name
-   product dimensions
-   product weight
-   product description attributes

------------------------------------------------------------------------

## 7. Relationship and Orphan Checks

Relationship validation was performed between:

-   Orders → Customers
-   Order Items → Orders
-   Payments → Orders
-   Reviews → Orders
-   Order Items → Products
-   Order Items → Sellers

Result:

    0 orphan records

------------------------------------------------------------------------

## 8. Suspicious Values Check

Checks performed:

-   Order status values
-   Negative payment values
-   Negative product prices
-   Missing product weights

Results:

-   No negative payment values found.
-   No negative product prices found.
-   Two products have missing weight values.
-   Order statuses contain valid operational states.

------------------------------------------------------------------------

## 9. Key Decisions

### Decision 1

Raw CSV files were not modified.

Reason: Maintains source data integrity and supports future
reconciliation.

### Decision 2

Profiling was completed before transformations.

Reason: Cleaning decisions will be based on actual data problems.

### Decision 3

Separate profiling outputs were created.

Reason: Maintains traceability and avoids unnecessary data merging.

------------------------------------------------------------------------

## 10. Problems Faced and Solutions

  -----------------------------------------------------------------------
  Problem                             Solution
  ----------------------------------- -----------------------------------
  Large raw datasets                  Used Pandas profiling scripts

  Empty folders not tracked by Git    Added .gitkeep files

  Multiple relationship checks        Created separate validation scripts
  required                            
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 11. Phase 02 Completion Checklist

  Requirement                 Status
  --------------------------- -----------
  Profile all 9 datasets      Completed
  Dataset size analysis       Completed
  Row count analysis          Completed
  Column analysis             Completed
  Data type analysis          Completed
  Missing value analysis      Completed
  Duplicate analysis          Completed
  Identifier analysis         Completed
  Date range analysis         Completed
  Suspicious value analysis   Completed
  Relationship checks         Completed
  Orphan record checks        Completed
  Summary profiling report    Completed

------------------------------------------------------------------------

## 12. Next Phase

Phase 03 will focus on:

-   Source dataset grain understanding
-   Source ERD creation
-   Primary keys and foreign keys
-   Relationship types
-   Duplicate calculation prevention strategy
