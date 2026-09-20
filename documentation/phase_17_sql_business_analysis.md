# Phase 17: SQL Business Analysis (15+ Questions)

## Overview

This phase consolidates business questions developed during Phases 12–16.

The objective was to demonstrate SQL-based business analysis across multiple areas:

- Customer behaviour
- Repeat customers
- Delivery performance
- Seller performance
- Product performance
- Category analysis
- Payment behaviour
- Freight analysis
- Geographic analysis


---

# Business Questions Covered


## Customer Analysis

### Q1. How many unique customers exist in the marketplace?

Business Area:
Customer Analysis


SQL Concepts:
- COUNT DISTINCT
- Aggregation


---

### Q2. Which customers purchased more than once?

Business Area:
Repeat Customer Analysis


SQL Concepts:
- GROUP BY
- HAVING
- Aggregation


---

### Q3. What percentage of customers are repeat customers?

Business Area:
Customer Retention


SQL Concepts:
- CTE
- Aggregation
- Subquery


---

### Q4. Who are the highest-value customers based on purchase value?

Business Area:
Customer Value Analysis


SQL Concepts:
- JOIN
- Aggregation
- ORDER BY


---

# Delivery Analysis


### Q5. What is the average delivery time across all orders?

Business Area:
Delivery Performance


SQL Concepts:
- Date Functions
- Aggregation


---

### Q6. How many deliveries were completed on time versus late?

Business Area:
Delivery Performance


SQL Concepts:
- CASE
- Conditional Aggregation


---

### Q7. Which customer states experience longer delivery times?

Business Area:
Geographic Delivery Analysis


SQL Concepts:
- JOIN
- GROUP BY
- Aggregation


---

### Q8. Are late deliveries associated with lower review scores?

Business Area:
Delivery Satisfaction Analysis


SQL Concepts:
- CASE
- JOIN
- Aggregation


---

# Seller Analysis


### Q9. Which sellers generate the highest merchandise value?

Business Area:
Seller Performance


SQL Concepts:
- JOIN
- Aggregation
- Ranking


---

### Q10. Which sellers have the highest freight burden percentage?

Business Area:
Seller Logistics Performance


SQL Concepts:
- Calculation
- Aggregation
- Ranking


---

### Q11. Which sellers perform best when combining sales, reviews and delivery?

Business Area:
Seller Performance Framework


SQL Concepts:
- CTE
- Window Functions
- Ranking


---

# Product & Category Analysis


### Q12. Which categories generate the highest revenue?

Business Area:
Category Performance


SQL Concepts:
- JOIN
- Aggregation


---

### Q13. Which categories sell the highest number of units?

Business Area:
Product Volume Analysis


SQL Concepts:
- GROUP BY
- Aggregation


---

### Q14. Which categories have the lowest average review scores?

Business Area:
Customer Satisfaction


SQL Concepts:
- Aggregation
- Filtering


---

# Payment & Freight Analysis


### Q15. Which payment methods generate the highest payment value?

Business Area:
Payment Analysis


SQL Concepts:
- Aggregation
- Ranking


---

### Q16. Does installment count influence average order value?

Business Area:
Payment Behaviour


SQL Concepts:
- GROUP BY
- Aggregation


---

### Q17. Which product categories have the highest freight percentage?

Business Area:
Freight Analysis


SQL Concepts:
- Calculated Metrics
- Ranking


---

# Geographic Analysis


### Q18. Which states generate the highest revenue?

Business Area:
Geographic Sales Analysis


SQL Concepts:
- JOIN
- Aggregation


---

### Q19. Which states contain the highest number of customers?

Business Area:
Customer Geography


SQL Concepts:
- GROUP BY
- Ranking


---

### Q20. Where are sellers geographically concentrated?

Business Area:
Seller Geography


SQL Concepts:
- JOIN
- Aggregation


---

# SQL Concept Coverage Checklist


| SQL Concept | Covered |
|---|---|
| JOIN | Yes |
| CTE | Yes |
| Window Functions | Yes |
| ROW_NUMBER | Yes |
| RANK / DENSE_RANK | Yes |
| LAG | Yes |
| CASE | Yes |
| Subqueries | Yes |
| Aggregations | Yes |
| Date Functions | Yes |
| Conditional Aggregation | Yes |


---

# Additional SQL Demonstration Queries Added


## Window Function Example

Purpose:
Rank sellers by business performance.


Functions:

- RANK()
- ROW_NUMBER()
- DENSE_RANK()


---

## LAG Example

Purpose:
Compare monthly sales performance with previous period.


Function:

LAG()


---

## Conditional Aggregation Example

Purpose:
Compare order status performance.


Functions:

CASE WHEN


---

# Phase 17 Status

Completed.

Total meaningful business questions:

20

Coverage includes all required SQL concepts.

Next Phase:
Phase 18 - Final SQL Business Analysis Review