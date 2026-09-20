# Phase 04: Customer Identity Investigation and Decisions

## 1. Objective

Investigate customer identifiers and determine how to identify
order-level customers, unique customers and repeat customers.

## 2. Identifier Decisions

| Analysis | Identifier | Reason |
|---|---|---|
| Link an order to its customer record | customer_id | Matches orders.customer_id to customers.customer_id |
| Count unique customers across orders | customer_unique_id | Links multiple order-level customer records to the same dataset customer identity |
| Identify repeat customers | customer_unique_id with at least two distinct order_id values | Counts separate orders rather than items or payment records |
| Count orders | order_id | Identifies each order uniquely |

customer_unique_id is the dataset's proxy for a real customer.
It does not independently verify a person's identity.

## 3. Investigation Results

| Check | Result |
|---|---:|
| Customer records | 99,441 |
| Distinct customer_id values | 99,441 |
| Distinct customer_unique_id values | 96,096 |
| Orders | 99,441 |
| customer_id values linked to multiple orders | 0 |
| customer_unique_id values with multiple customer records | 2,997 |

customer_id identifies an order-associated customer record in this
extract. Counting it as unique people would count repeat customers
more than once.

Repeated customer_unique_id values are expected and must not be
removed from the raw customer table as duplicate records.

## 4. Method

1. Validate that customer identifiers are neither null nor blank.
2. Validate uniqueness of customers.customer_id and orders.order_id.
3. Confirm every order's customer_id exists in customers.
4. Join orders to customers on customer_id using many-to-one validation.
5. Confirm the join preserves the order row count and identity coverage.
6. Group by customer_unique_id and count distinct order_id values.
7. Classify customers with two or more qualifying orders as repeat customers.
8. Calculate results separately for all orders and delivered orders.

No item, payment or review tables are required for this calculation.

## 5. Customer Analysis Results

| Metric | All orders | Delivered orders only |
|---|---:|---:|
| Orders | 99,441 | 96,478 |
| Unique customers | 96,096 | 93,358 |
| Customers with exactly one qualifying order | 93,099 | 90,557 |
| Repeat customers | 2,997 | 2,801 |
| Repeat customer rate | 3.12% | 3.00% |
| Orders from repeat customers | 6,342 | 5,921 |
| Additional orders beyond each customer's first | 3,345 | 3,120 |
| Maximum orders per customer | 17 | 15 |

Repeat customer rate =
repeat customers / unique customers in the same population * 100.

Orders from repeat customers includes their first qualifying order.
Additional orders beyond first excludes each customer's first
qualifying order. These are different measures.

Reconciliation:
- All orders: 93,099 + 6,342 = 99,441.
- Delivered orders: 90,557 + 5,921 = 96,478.
- All-order customers: 93,099 + 2,997 = 96,096.
- Delivered-order customers: 90,557 + 2,801 = 93,358.

## 6. Primary Repeat-Purchase Definition

The primary repeat-purchase measure uses delivered orders only.

A repeat purchasing customer has at least two distinct orders
with order_status = delivered under the same customer_unique_id.

Result: 2,801 repeat customers out of 93,358 customers with at
least one delivered order, giving a rounded rate of 3.00%.

The all-order definition is retained separately as repeat order
activity. It includes canceled and other non-delivered statuses,
so it must not be labeled completed repeat purchasing.

A customer with two total orders but only one delivered order is
a repeat customer under the all-order definition, but not under
the delivered-order definition.

## 7. Modeling Decisions

- Preserve customer_id for order-level joins and source traceability.
- Use customer_unique_id for customer-level grouping and distinct counts.
- A future customer-level dimension should contain one row per
  customer_unique_id, with a bridge or mapping from customer_id.
- Preserve order-associated location attributes; do not select an
  arbitrary location when customer records differ across purchases.
- Count distinct orders, not item rows or payment rows.
- Apply the same status and time filters to numerator and denominator.

## 8. Limitations

- Repeat status is measured only within the available dataset window.
- A one-order customer may have purchases outside that window.
- Customers have different lengths of observation; this rate is
  descriptive, not a cohort retention rate.
- Delivered status does not establish the absence of later refunds.
- Customer identity depends on the supplied customer_unique_id mapping.
- Historical as-of analysis must use only orders available by that
  cutoff; full-window repeat status must not leak into earlier periods.

## 9. Supporting Files

- python/phase_04_customer_identity.py
- profiling/phase_04_identity_checks.csv
- profiling/phase_04_customer_summary.csv
- profiling/phase_04_order_frequency.csv

## 10. Explanation for the Supervisor

I used customer_id to connect each order to its customer record.
I used customer_unique_id to recognize the same customer across
different orders. I counted distinct order_id values per
customer_unique_id and classified customers with at least two
qualifying orders as repeat customers.

The primary repeat-purchase metric uses delivered orders:
2,801 repeat customers out of 93,358 customers, or 3.00%.
All-order repeat activity is reported separately at 3.12%.
