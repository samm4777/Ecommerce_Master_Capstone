# Phase 18: SQL Performance Challenge


## Selected Query

Seller Performance Analysis


Business Purpose:

Measure seller performance using:

- Orders
- Products sold
- Merchandise value
- Freight value
- Customer reviews


---

# Before Optimization


## Problem

The original query joined large fact tables before aggregation.

Issues:

- More rows processed
- Larger intermediate datasets
- Higher logical reads


Performance:


CPU Time:
(fill from SQL Server)


Elapsed Time:
(fill from SQL Server)


Logical Reads:
(fill from SQL Server)



---

# Optimization Applied


Changes:

1. Aggregated OrderItems before joining.
2. Aggregated Reviews separately.
3. Reduced unnecessary row expansion.
4. Added indexes on frequently joined columns.


---

# After Optimization


Performance:


CPU Time:
(fill from SQL Server)


Elapsed Time:
(fill from SQL Server)


Logical Reads:
(fill from SQL Server)



---

# Comparison


| Metric | Before | After |
|-|-|-|
| CPU Time | | |
| Elapsed Time | | |
| Logical Reads | | |


---

# Conclusion


The optimization improved query efficiency by reducing the amount of data processed before joins.

The main improvement came from early aggregation and indexing frequently used join columns.