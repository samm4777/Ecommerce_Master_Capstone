# Phase 05: Business Metric Definitions

## 1. Purpose

Define consistent business metrics before building analytical tables,
reports and Power BI measures.

These definitions incorporate the validated source grains from
Phase 03 and customer identity decisions from Phase 04.

## 2. Shared Reporting Rules

- Count orders using distinct order_id.
- Link orders to customer records using customer_id.
- Identify customers across purchases using customer_unique_id.
- Default date filtering uses order_purchase_timestamp.
- Completed-purchase metrics use order_status = delivered.
- Operational order metrics include all statuses unless specified.
- Apply identical population and date filters to related numerators
  and denominators.
- Monetary values are in Brazilian reais (BRL), not PKR or USD.
- Preserve missing records separately from recorded zero values.
- Return blank for ratios with a zero denominator.
- Keep raw source files unchanged.

## 3. Order and Customer Metrics

| Metric | Definition | Calculation / source |
|---|---|---|
| Order | One recorded order, regardless of status | Distinct orders.order_id |
| Completed Order | An order whose recorded status is delivered | Distinct order_id where order_status = delivered |
| Cancelled Order | An order whose recorded status is canceled | Distinct order_id where order_status = canceled |
| Customer | A distinct dataset customer identity with at least one order in the selected population | Distinct customer_unique_id after linking orders to customers on customer_id |
| Purchasing Customer | A distinct customer with at least one delivered order in the selected population | Distinct customer_unique_id for delivered orders |
| Repeat Customer | A customer with at least two distinct delivered orders within the selected purchase-date period | Group delivered orders by customer_unique_id and count customers with distinct order_id >= 2 |

### Customer Identity Decisions

customer_id identifies the order-associated customer record.
It must be used for the orders-to-customers join, not as the
identifier for distinct people across purchases.

customer_unique_id is the dataset's customer identity proxy.
It does not independently verify a real person.

The primary repeat-customer definition uses delivered orders.
An all-status variant may be reported separately as
"Repeat Order-Activity Customers".

Repeat Customer Rate =
Repeat Customers / Purchasing Customers * 100.

Both numerator and denominator use the same selected period
and delivered-order population.

This is a within-period repeat-purchase metric. It is not a
historical returning-customer or cohort-retention metric.
A customer with one order before the selected period and one
inside it is not a repeat customer under this within-period rule.

The canceled status is spelled with one "l" in the source.
Unavailable orders are not automatically classified as canceled.

## 4. Financial Metrics

| Metric | Definition | Calculation / source |
|---|---|---|
| Merchandise Value | Sum of item prices for delivered orders in the selected population; excludes freight | SUM(order_items.price) after filtering through eligible order_id values |
| Payment Value | Sum of recorded payment values associated with delivered orders in the selected population | SUM(order_payments.payment_value) for eligible order_id values |
| Freight Value | Sum of item-level freight charges for delivered orders in the selected population | SUM(order_items.freight_value) for eligible order_id values |
| Average Order Value (AOV) | Merchandise value per completed order | Merchandise Value / Completed Orders |

### Merchandise Value

Each order_items row is a numbered item within an order.
Sum price once per validated (order_id, order_item_id) row.

Do not multiply price by order_item_id: it is a sequence number,
not a quantity field.

Merchandise Value excludes freight. It is not payment value,
profit, marketplace commission or audited net revenue.

All-status merchandise totals may be reported separately, but
must be labeled "Merchandise Value - All Order Statuses".

### Payment Value

Each payment row is identified by
(order_id, payment_sequential).

Sum every qualifying payment record once. An order may have
multiple payment records or payment methods.

Do not multiply payment_value by payment_installments.
Do not use SUM(DISTINCT payment_value), because separate
legitimate payment records may have equal values.

Payment Value is the amount recorded in the payment dataset.
It does not independently establish settlement, refunds or net cash.

The source has no payment timestamp in this table. Therefore,
the default period is the associated order's purchase period,
not a payment-receipt period.

Missing payment records remain unknown, not confirmed zero.
Report the count of completed orders without payment records
alongside payment-based analysis.

### Freight Value

Sum freight_value once per item row.
Do not treat freight as a single order-level amount before
aggregating the order's items.

Freight Value represents the recorded freight charge, not a
verified logistics expense or profit measure.

### AOV

The primary AOV excludes freight and uses completed orders.

AOV = delivered-order merchandise value /
      distinct delivered orders.

Do not average item prices or divide by item count.

If a completed order has no item records or missing prices,
flag incomplete merchandise coverage. Do not present the AOV
as complete; return blank until resolved or publish a separately
labeled covered-orders AOV with its own matching denominator.

### Financial Reconciliation

Compare Payment Value with Merchandise Value + Freight Value
for the same order population.

Use exact integer cents where possible.
Do not assume the values are interchangeable or force equality.
Investigate differences at order level.

Do not add Payment Value to Merchandise Value as combined revenue.

## 5. Delivery Metrics

### Eligible Delivery Population

An order is eligible for on-time/late classification when:

- order_status = delivered;
- order_delivered_customer_date is present and parses correctly;
- order_estimated_delivery_date is present and parses correctly.

Use calendar dates for comparison, ignoring time of day.
A delivery at any time on the estimated date is on time.

Missing or invalid dates are "Unclassified", not on time or late.
Keep them out of delivery-rate denominators and report their count.

Chronology anomalies, such as delivery before purchase, must be
flagged for investigation and excluded from published delivery KPIs
until resolved. Report those exclusions.

| Metric | Definition | Calculation |
|---|---|---|
| On-Time Delivery | Eligible order delivered on or before its estimated date | Actual delivery date <= estimated delivery date |
| Late Delivery | Eligible order delivered after its estimated date | Actual delivery date > estimated delivery date |
| Delivery Delay | Non-negative calendar days past the estimated date for an eligible order | MAX(actual delivery date - estimated delivery date, 0) |
| On-Time Delivery Rate | Share of eligible orders delivered on time | On-time orders / eligible orders * 100 |
| Late Delivery Rate | Share of eligible orders delivered late | Late orders / eligible orders * 100 |
| Average Delivery Delay | Average delay across all eligible orders, including zero for on-time orders | Sum delay days / eligible orders |
| Average Late-Order Delay | Average delay among late orders only | Sum delay days for late orders / late orders |

Early delivery has zero Delivery Delay.
For analysis of early versus late delivery, use a separately named
"Delivery Variance Days" metric that retains negative values.

Eligible orders = On-Time Delivery orders + Late Delivery orders.

These metrics describe delivered orders grouped by purchase date.
An undelivered overdue order is not counted as a Late Delivery;
it requires a separately defined overdue-open-order metric.

## 6. Average Review Score

Definition:
The review-weighted mean of valid review scores associated with
delivered orders in the selected purchase-date population.

Calculation:
SUM(valid review_score) / COUNT(valid review_score).

Rules:

- Valid scores are integers from 1 through 5.
- The validated review key is (order_id, review_id).
- Retain each review record once at that grain.
- Multiple reviews for one order are included under this explicit
  review-weighted policy.
- Missing reviews are not zero scores.
- Missing review comments do not invalidate a valid numeric score.
- Return blank when there are no valid reviews.
- Exclude and report invalid scores.
- Do not average order-level averages to calculate this metric.

For aggregated review data, preserve score_sum and score_count.
Calculate SUM(score_sum) / SUM(score_count).

An order-weighted review average would be a separate metric
requiring an explicit one-score-per-order policy.

## 7. Preventing Duplicate Calculations

Keep orders, items, payments and reviews at their natural grains.

For an order-level overview:

1. Aggregate items by order_id to merchandise and freight totals.
2. Aggregate payments by order_id to payment totals.
3. Aggregate reviews by order_id to score sum and valid-score count.
4. Left join those aggregates to the unique orders table.
5. Validate one-to-one joins and reconcile totals before and after.
6. Apply the defined status and date filters consistently.

Never directly join raw items, payments and reviews and then sum
their financial fields.

Customer and order counts must not increase because an order
contains multiple items, payment records or reviews.

## 8. Product, Seller and Payment-Method Filters

Product and seller merchandise/freight analysis uses item grain.

Distinct order and customer counts across product or seller groups
are not additive: the same order or customer can occur in several groups.

For a product/seller slice, category AOV means selected-item
merchandise value divided by distinct delivered orders containing
those selected items. Label it clearly; it is not full-basket AOV.

Do not repeat an order's full payment across its products or sellers.
Payment allocation requires a separately documented allocation rule
that reconciles back to the original order payment.

Payment-method filters apply naturally to payment records.
Do not assign full merchandise totals to every payment method in a
split-payment order.

Order reviews are order-level feedback. Do not describe them as
independent product reviews merely because they are linked to items.

## 9. Reporting Limitations

- Delivered status is a snapshot, not proof of refund-free revenue.
- The source does not establish full accounting revenue or profit.
- Repeat behavior is limited to the dataset and selected period.
- Review results reflect customers who submitted valid scores.
- Historical as-of reporting requires temporal rules beyond filtering
  purchase dates; current statuses and later reviews may reveal
  information unavailable at an earlier cutoff.

## 10. Explanation for the Supervisor

I calculated merchandise value by summing item prices once per
validated order-item key for delivered orders. Freight is separate.

I handled payments in a separate payment-grain table, summed all
payment records once per order, and joined the order-level totals.
I did not multiply payment values by installments or treat them as
interchangeable with merchandise value.

I used customer_id for order joins and customer_unique_id for unique
and repeat customers. Repeat customers have at least two delivered
orders within the selected purchase-date period.

## 11. Phase Deliverable

Metric definitions are documented before Power BI implementation.
Implementation must follow these populations, grains, denominators
and missing-data rules.
