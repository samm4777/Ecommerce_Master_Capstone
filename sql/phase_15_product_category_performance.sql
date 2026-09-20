/*
Phase 15:
Product & Category Performance Analysis

Analysis:
- Revenue
- Volume
- Ratings
- Delivery
- Freight
*/


----------------------------------------------------
-- 1. Category Revenue Performance
----------------------------------------------------

SELECT

p.product_category_name,

SUM(oi.price) AS Total_Revenue,

COUNT(DISTINCT oi.order_id) AS Total_Orders,


COUNT(oi.product_id) AS Units_Sold


FROM stg.order_items oi


LEFT JOIN stg.products p

ON oi.product_id = p.product_id


GROUP BY

p.product_category_name


ORDER BY

Total_Revenue DESC;



----------------------------------------------------
-- 2. Category Volume Performance
----------------------------------------------------

SELECT

p.product_category_name,

COUNT(oi.product_id) AS Units_Sold,


COUNT(DISTINCT oi.order_id) AS Orders


FROM stg.order_items oi


LEFT JOIN stg.products p

ON oi.product_id = p.product_id


GROUP BY

p.product_category_name


ORDER BY

Units_Sold DESC;



----------------------------------------------------
-- 3. Category Customer Satisfaction
----------------------------------------------------

SELECT


p.product_category_name,


AVG(r.review_score) AS Average_Rating,


COUNT(r.review_id) AS Reviews



FROM stg.order_items oi


LEFT JOIN stg.products p

ON oi.product_id = p.product_id


LEFT JOIN stg.reviews r

ON oi.order_id = r.order_id



GROUP BY

p.product_category_name



ORDER BY

Average_Rating DESC;



----------------------------------------------------
-- 4. Poorly Rated Categories
----------------------------------------------------

SELECT TOP 10


p.product_category_name,


AVG(r.review_score) AS Average_Rating,


COUNT(r.review_id) AS Review_Count



FROM stg.order_items oi


JOIN stg.products p

ON oi.product_id=p.product_id


JOIN stg.reviews r

ON oi.order_id=r.order_id



GROUP BY

p.product_category_name



HAVING COUNT(r.review_id) > 50


ORDER BY

Average_Rating ASC;



----------------------------------------------------
-- 5. Category Delivery Performance
----------------------------------------------------

SELECT


p.product_category_name,


AVG(

DATEDIFF(

DAY,

TRY_CONVERT(datetime,o.order_delivered_carrier_date),

TRY_CONVERT(datetime,o.order_delivered_customer_date)

)

) AS Average_Delivery_Days



FROM stg.order_items oi


JOIN stg.products p

ON oi.product_id=p.product_id


JOIN stg.orders o

ON oi.order_id=o.order_id



GROUP BY

p.product_category_name



ORDER BY

Average_Delivery_Days DESC;



----------------------------------------------------
-- 6. Category Freight Burden
----------------------------------------------------

SELECT


p.product_category_name,


SUM(oi.freight_value) AS Total_Freight,


AVG(oi.freight_value) AS Average_Freight,


SUM(oi.price) AS Merchandise_Value,


(SUM(oi.freight_value) /
NULLIF(SUM(oi.price),0))*100 
AS Freight_Percentage



FROM stg.order_items oi


JOIN stg.products p

ON oi.product_id=p.product_id



GROUP BY

p.product_category_name



ORDER BY

Freight_Percentage DESC;



----------------------------------------------------
-- 7. Low Performing Categories
----------------------------------------------------

SELECT TOP 10


p.product_category_name,


COUNT(oi.order_id) AS Orders,


SUM(oi.price) AS Revenue,


AVG(r.review_score) AS Rating



FROM stg.order_items oi


JOIN stg.products p

ON oi.product_id=p.product_id


LEFT JOIN stg.reviews r

ON oi.order_id=r.order_id



GROUP BY

p.product_category_name



ORDER BY

Revenue ASC;