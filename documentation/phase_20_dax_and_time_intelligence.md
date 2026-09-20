# Phase 20: DAX Measures and Time Intelligence

## Overview

Created business-focused DAX measures in Power BI using the SQL analytical layer.

The purpose of DAX was to create reusable business calculations for executive analysis, KPI tracking, and time-based comparisons.

## Created Measures

1. Total Merchandise Value
- Calculates total product sales value using price × quantity.

2. Total Orders
- Counts completed order records.

3. Total Customers
- Counts unique customers.

4. Average Order Value
- Calculates average merchandise value per order.

5. Total Freight Value
- Calculates total shipping cost.

6. Freight %
- Measures freight cost contribution compared to merchandise value.

7. Repeat Customer %
- Identifies customers who placed more than one order.

8. On-Time Delivery %
- Calculates percentage of deliveries completed within expected delivery period.

9. Late Delivery %
- Calculates delayed deliveries.

10. Average Delivery Delay
- Calculates average delivery duration.

11. Average Review Score
- Calculates customer satisfaction score.

12. Previous Period Value
- Uses DATEADD for previous month comparison.

13. Growth %
- Calculates month-over-month growth.

14. Contribution %
- Calculates product contribution against total merchandise value.

## Time Intelligence

Implemented:
- Previous period comparison
- Month-over-month growth analysis
- Contribution analysis

The calculations use the Dim Date table instead of raw date columns.

## Business Value

DAX transforms raw analytical tables into management KPIs that support:
- Revenue monitoring
- Customer analysis
- Delivery performance
- Product contribution
- Trend analysis