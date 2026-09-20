/*
Phase 14:
Seller Performance Framework

Purpose:
Evaluate sellers using multiple business dimensions.
Revenue alone is not used as the performance indicator.
*/


----------------------------------------------------
-- 1. Seller Sales Performance
----------------------------------------------------

SELECT

oi.seller_id,

COUNT(DISTINCT oi.order_id) AS Total_Orders,

COUNT(DISTINCT oi.product_id) AS Products_Sold,

SUM(oi.price) AS Merchandise_Value,

SUM(oi.freight_value) AS Freight_Value


FROM stg.order_items oi


GROUP BY

oi.seller_id;

----------------------------------------------------
-- 2. Seller Delivery Performance
----------------------------------------------------

SELECT


oi.seller_id,


COUNT(*) AS Total_Items,


AVG(

DATEDIFF(
DAY,
TRY_CONVERT(datetime,o.order_delivered_carrier_date),
TRY_CONVERT(datetime,o.order_delivered_customer_date)
)

) AS Average_Delivery_Days


FROM stg.order_items oi


JOIN stg.orders o

ON oi.order_id = o.order_id


GROUP BY

oi.seller_id;



----------------------------------------------------
-- 3. Seller Customer Satisfaction
----------------------------------------------------


SELECT


oi.seller_id,


AVG(r.review_score) AS Average_Review_Score,


COUNT(r.review_id) AS Review_Count


FROM stg.order_items oi


JOIN stg.reviews r

ON oi.order_id = r.order_id


GROUP BY

oi.seller_id;



----------------------------------------------------
-- 4. Product Mix Analysis
----------------------------------------------------

SELECT

oi.seller_id,

COUNT(DISTINCT p.product_category_name)
AS Category_Count,

COUNT(DISTINCT oi.product_id)
AS Unique_Products


FROM stg.order_items oi


LEFT JOIN stg.products p

ON oi.product_id = p.product_id


GROUP BY

oi.seller_id;



----------------------------------------------------
-- 5. Seller Performance Framework Score
----------------------------------------------------

/*

Framework:

Sales Contribution          25%
Order Volume                20%
Customer Satisfaction       25%
Delivery Performance        20%
Product Diversity           10%


Total Score = 100


*/
