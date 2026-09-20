# Phase 09: SQL Server Analytics Database

## Database Platform

The analytics database was implemented using Azure SQL Database.

Azure SQL provides SQL Server compatible relational database capabilities in a cloud environment.

Database:

Ecommerce_Analytics


---

# Database Architecture

The database follows a layered analytical warehouse structure:

---

# Staging Layer

Purpose:

The staging layer stores prepared data received from the Python data preparation pipeline.

Tables:

- stg.customers
- stg.orders
- stg.order_items
- stg.payments
- stg.products
- stg.sellers
- stg.category_translation
- stg.reviews
- stg.geolocation


---

# Dimension Layer

Created according to Phase 08 dimensional model.

## DimCustomer

Grain:

One row represents one customer.


## DimProduct

Grain:

One row represents one product.


## DimCategory

Grain:

One row represents one product category.


## DimSeller

Grain:

One row represents one seller.


## DimGeography

Grain:

One row represents one geographic location.


## DimDate

Grain:

One row represents one calendar date.


Surrogate keys were implemented using IDENTITY columns where required.

Reason:

- Avoid dependency on source system keys
- Improve warehouse scalability
- Support future data integration


---

# Fact Layer

## FactOrders

Grain:

One row represents one customer order.


## FactOrderItems

Grain:

One row represents one product item belonging to one customer order.


## FactPayments

Grain:

One row represents one payment transaction.


## FactReviews

Grain:

One row represents one customer review.


---

# Keys and Relationships

Primary keys were created on all dimension and fact tables.

Foreign keys were implemented to maintain analytical relationships.

Relationships:

- Orders → Customer
- Orders → Date
- Orders → Geography
- OrderItems → Product
- OrderItems → Seller
- Product → Category


---

# SQL Responsibility

SQL was responsible for:

- Creating analytical database structures
- Creating schemas
- Creating staging tables
- Creating dimensions
- Creating fact tables
- Implementing primary keys
- Implementing foreign keys
- Supporting analytical reporting


Python was responsible for:

- Data cleaning
- Data preparation
- Missing value handling
- Data validation
- Creating prepared datasets


---

# Data Loading Strategy

Loading sequence:

1. Python prepared CSV files
2. Load into staging tables
3. Populate dimension tables
4. Populate fact tables


Loading tools:

- Azure Data Studio Import Wizard
- SQL Server Import/Export Wizard
- Python SQLAlchemy pipeline