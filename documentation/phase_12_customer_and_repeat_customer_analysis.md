# Phase 12: Customer & Repeat Customer Analysis

## Objective

Analyze customer behaviour using the Azure SQL analytical model.

The analysis covers:

- Unique customers
- Repeat customers
- Purchase frequency
- Customer value
- Customer geography
- Average order value
- Customer satisfaction


# Customer Identifier

The analysis uses:

customer_unique_id

from:

dim.Customer


Reason:

customer_key is a warehouse surrogate key and only identifies the warehouse record.

customer_unique_id represents the real customer across multiple orders and is therefore used for repeat customer analysis.


# Repeat Customer Definition

A repeat customer is defined as:

A customer who placed more than one order.

SQL logic:

COUNT(order_id) > 1


# Findings


| Metric | Result |
|---|---:|
| Unique Customers | 99,441 |
| Repeat Customers | 2,997 |
| Repeat Customer Percentage | 3.12% |
| Average Order Value | 147.38 |
| Average Review Rating | 4 |


# Customer Value Method

Customer value was calculated as:

SUM(Order Item Price)

grouped by customer_unique_id.


This identifies customers generating the highest merchandise value.


# Customer Geography

Customer distribution was analysed using:

customer_state

from dim.Customer.


Highest customer concentration:

| State | Customers |
|---|---:|
| SP | 40,302 |
| RJ | 12,384 |
| MG | 11,259 |


# Conclusion

The SQL analysis successfully identifies customer behaviour patterns including repeat purchasing, customer value, geographic concentration and satisfaction levels.

These results contribute to the business analysis questions required in Phase 17.