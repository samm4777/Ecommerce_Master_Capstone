/*
Phase 12:
Customer & Repeat Customer Analysis

Purpose:
Analyze customer behaviour,
repeat customers,
customer value,
geography,
and satisfaction.
*/


USE Ecommerce_Analytics;



--------------------------------------------------
-- 1. Unique Customers
--------------------------------------------------

SELECT
COUNT(DISTINCT customer_key) AS Unique_Customers
FROM fact.Orders;



--------------------------------------------------
-- 2. Customer Order Frequency
--------------------------------------------------

SELECT

c.customer_unique_id,

COUNT(o.order_id) AS Total_Orders

FROM fact.Orders o

JOIN dim.Customer c
ON o.customer_key = c.customer_key

GROUP BY
c.customer_unique_id

ORDER BY Total_Orders DESC;



--------------------------------------------------
-- 3. Repeat Customers
--------------------------------------------------

WITH customer_orders AS

(

SELECT

c.customer_unique_id,

COUNT(o.order_id) AS order_count

FROM fact.Orders o

JOIN dim.Customer c

ON o.customer_key = c.customer_key

GROUP BY
c.customer_unique_id

)


SELECT

COUNT(*) AS Repeat_Customers

FROM customer_orders

WHERE order_count > 1;



--------------------------------------------------
-- 4. Repeat Customer Percentage
--------------------------------------------------

WITH customer_orders AS

(

SELECT

c.customer_unique_id,

COUNT(o.order_id) AS order_count

FROM fact.Orders o

JOIN dim.Customer c

ON o.customer_key=c.customer_key

GROUP BY
c.customer_unique_id

)


SELECT

CAST(
SUM(
CASE WHEN order_count > 1
THEN 1
ELSE 0
END
)

*100.0

/

COUNT(*)

AS DECIMAL(10,2)

)

AS Repeat_Customer_Percentage


FROM customer_orders;



--------------------------------------------------
-- 5. Customer Value
--------------------------------------------------

SELECT

c.customer_unique_id,

COUNT(o.order_id) AS Orders,

SUM(oi.price) AS Customer_Value


FROM fact.Orders o


JOIN dim.Customer c

ON o.customer_key=c.customer_key


JOIN fact.OrderItems oi

ON o.order_id=oi.order_id


GROUP BY

c.customer_unique_id


ORDER BY Customer_Value DESC;



--------------------------------------------------
-- 6. Average Order Value
--------------------------------------------------

SELECT

AVG(order_value)

FROM

(

SELECT

o.order_id,

SUM(oi.price) AS order_value


FROM fact.Orders o


JOIN fact.OrderItems oi

ON o.order_id=oi.order_id


GROUP BY o.order_id

) x;



--------------------------------------------------
-- 7. Customer Geography
--------------------------------------------------

SELECT

c.customer_state,

COUNT(DISTINCT c.customer_unique_id)
AS Customers


FROM dim.Customer c


GROUP BY

c.customer_state


ORDER BY Customers DESC;



--------------------------------------------------
-- 8. Customer Satisfaction
--------------------------------------------------

SELECT

AVG(review_score)

AS Average_Rating


FROM fact.Reviews;