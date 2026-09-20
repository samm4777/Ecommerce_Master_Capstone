# Phase 14: Seller Performance Framework


## Objective

The objective of this phase is to evaluate seller performance using multiple business dimensions.

Seller performance is not measured only by revenue because high sales volume alone does not represent complete seller quality.

The framework combines:

- Sales contribution
- Order activity
- Customer satisfaction
- Delivery performance
- Product diversity


---

# Seller Performance Framework


| Dimension | Weight | Metrics |
|---|---:|---|
| Sales Performance | 25% | Merchandise Value, Freight Value |
| Order Performance | 20% | Total Orders, Items Sold |
| Customer Satisfaction | 25% | Average Review Score, Review Count |
| Delivery Performance | 20% | Average Delivery Days |
| Product Diversity | 10% | Categories Sold, Unique Products |


---

# Metric Justification


## 1. Sales Performance (25%)

Metrics:

- Merchandise Value
- Freight Value


Reason:

Sales contribution measures the seller's commercial importance.

However, revenue is not used alone because sellers with high sales may still have delivery or satisfaction issues.


---

## 2. Order Performance (20%)

Metrics:

- Total Orders
- Products Sold


Reason:

Order volume represents seller activity and customer demand.


---

## 3. Customer Satisfaction (25%)

Metrics:

- Average Review Score
- Review Count


Reason:

Customer feedback represents buyer experience.

A seller with strong sales but poor reviews requires further investigation.


---

## 4. Delivery Performance (20%)

Metrics:

- Average Delivery Days


Reason:

Delivery reliability affects customer experience and operational quality.


Note:

Some delivery records contain missing delivery timestamps.
SQL aggregate functions ignore NULL values during calculations.


---

## 5. Product Diversity (10%)

Metrics:

- Category Count
- Unique Products


Reason:

A wider product portfolio indicates stronger market coverage.


---

# Seller Score Calculation


Seller Performance Score:

(Sales Score × 25%)
+
(Order Score × 20%)
+
(Customer Satisfaction Score × 25%)
+
(Delivery Score × 20%)
+
(Product Diversity Score × 10%)



Scores should be normalized before applying weights.


---

# Business Interpretation


This framework prevents revenue-only evaluation.

A balanced seller evaluation should identify sellers who:

- Generate business value
- Maintain customer satisfaction
- Deliver reliably
- Offer diverse products


---

# Data Sources Used

SQL tables:

- stg.order_items
- stg.orders
- stg.reviews
- stg.products
- stg.sellers


---

# Phase Conclusion

The seller performance framework provides a balanced method for evaluating sellers using financial, operational, and customer experience indicators.