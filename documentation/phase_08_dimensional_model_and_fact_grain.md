# Phase 08: Dimensional Model & Fact Table Grain

## Objective

Design an analytical dimensional model for the E-Commerce Decision Intelligence Platform.

The model converts the prepared operational data into a structure suitable for:

- SQL Server analytics
- Power BI reporting
- DAX calculations
- Business performance analysis

The model supports analysis of:

- Sales performance
- Customer behaviour
- Product performance
- Seller performance
- Delivery performance
- Customer satisfaction
- Payment behaviour
- Freight impact
- Business risks and opportunities

---

# Modeling Approach

A Star Schema design was selected.

The reason for using a dimensional model is:

- Separate business events from descriptive information.
- Improve reporting performance.
- Simplify Power BI relationships.
- Prevent duplicate financial calculations.
- Maintain correct business grain.

The source ERD from Phase 03 represents the operational data structure, while this Phase 08 model represents the analytical warehouse structure.

---

# Dimension Tables

## DimCustomer

### Purpose

Stores customer descriptive information.

### Grain

One row represents one unique customer.

### Key Design

Primary Key:

customer_key (surrogate key)

Business Key:

customer_unique_id

### Attributes

- customer_unique_id
- customer_city
- customer_state
- customer_zip_code_prefix

---

# DimProduct

### Purpose

Stores product-level descriptive information.

### Grain

One row represents one product.

### Key Design

Primary Key:

product_key

Business Key:

product_id

### Attributes

- product_id
- category_key
- product weight
- product dimensions

---

# DimCategory

### Purpose

Stores product category information.

### Grain

One row represents one product category.

### Key Design

Primary Key:

category_key

Business Key:

product_category_name

### Attributes

- category_name
- category_name_english

---

# DimSeller

### Purpose

Stores seller descriptive information.

### Grain

One row represents one seller.

### Key Design

Primary Key:

seller_key

Business Key:

seller_id

### Attributes

- seller_id
- seller_city
- seller_state
- seller_zip_code_prefix

---

# DimGeography

### Purpose

Supports geographic analysis.

### Grain

One row represents one geographic location.

### Key Design

Primary Key:

geography_key

### Attributes

- zip_code_prefix
- city
- state
- latitude
- longitude

---

# DimDate

### Purpose

Supports time-based analysis and DAX time intelligence.

### Grain

One row represents one calendar date.

### Key Design

Primary Key:

date_key

### Attributes

- Date
- Day
- Month
- Quarter
- Year

---

# Fact Tables

## FactOrders

### Source

orders_prepared.csv

### Grain

One row represents one customer order.

### Purpose

Stores order-level business events.

### Measures

- Order count
- Delivery duration
- Delivery performance metrics

### Foreign Keys

- customer_key
- date_key
- geography_key

---

# FactOrderItems

### Source

order_items_prepared.csv

### Grain

One row represents one product item belonging to one customer order.

### Purpose

Stores item-level sales information.

### Measures

- Price
- Freight value
- Quantity

### Foreign Keys

- order_key
- product_key
- seller_key

---

# FactPayments

### Source

payments_prepared.csv

### Grain

One row represents one payment transaction.

### Purpose

Stores payment behaviour information.

### Measures

- Payment value
- Payment installments

### Important Decision

Payments are stored separately from order items because one order can contain multiple payment transactions.

Combining payment and item tables would multiply values and create incorrect financial reporting.

---

# FactReviews

### Source

order_reviews_dataset.csv

### Grain

One row represents one customer review.

### Purpose

Stores customer satisfaction information.

### Measure

- Review score

---

# Surrogate Key Decisions

Surrogate keys are used for dimension tables.

Used keys:

- customer_key
- product_key
- category_key
- seller_key
- geography_key
- date_key

## Justification

Surrogate keys were selected because:

- They separate analytical identifiers from source system identifiers.
- They improve warehouse consistency.
- They support future data changes.
- They improve SQL Server joins.
- They allow historical tracking if business attributes change.

---

# Prevention of Duplicate Financial Values

The model prevents incorrect reporting by maintaining separate business grains.

Examples:

## Orders vs Order Items

An order can contain multiple products.

Therefore:

FactOrders and FactOrderItems remain separate.

---

## Payments vs Order Items

An order can contain:

- Multiple products
- Multiple payment records

Directly joining these tables would duplicate:

- Payment value
- Freight value
- Revenue calculations

Therefore:

FactPayments remains a separate fact table.

---

# Final Analytical Model

## Fact Tables

- FactOrders
- FactOrderItems
- FactPayments
- FactReviews


## Dimension Tables

- DimCustomer
- DimProduct
- DimCategory
- DimSeller
- DimGeography
- DimDate


# Draft Diagram

The draft dimensional model diagram is stored in:
