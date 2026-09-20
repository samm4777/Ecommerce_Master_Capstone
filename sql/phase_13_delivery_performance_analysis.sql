/*
Phase 13:
Delivery Performance & Delivery vs Customer Satisfaction

Purpose:
Analyze order lifecycle,
delivery performance,
late deliveries,
geography,
seller/category impact,
and relationship with review scores.
*/


USE Ecommerce_Analytics;



--------------------------------------------------
-- 1. Order Lifecycle Performance
--------------------------------------------------

SELECT

AVG(
DATEDIFF(
DAY,
TRY_CONVERT(datetime, order_purchase_timestamp),
TRY_CONVERT(datetime, order_delivered_customer_date)
)
)
AS Average_Delivery_Days


FROM stg.orders

WHERE order_delivered_customer_date IS NOT NULL;



--------------------------------------------------
-- 2. Approval Time
--------------------------------------------------

SELECT

AVG(
DATEDIFF(
DAY,
TRY_CONVERT(datetime, order_purchase_timestamp),
TRY_CONVERT(datetime, order_approved_at)
)
)

AS Average_Approval_Days


FROM stg.orders

WHERE order_approved_at IS NOT NULL;



--------------------------------------------------
-- 3. Carrier Handover Time
--------------------------------------------------

SELECT

AVG(
DATEDIFF(
DAY,
TRY_CONVERT(datetime, order_approved_at),
TRY_CONVERT(datetime, order_delivered_carrier_date)
)
)

AS Average_Carrier_Handover_Days


FROM stg.orders

WHERE order_delivered_carrier_date IS NOT NULL;



--------------------------------------------------
-- 4. Estimated vs Actual Delivery
--------------------------------------------------

SELECT

AVG(

DATEDIFF(
DAY,
TRY_CONVERT(datetime, order_estimated_delivery_date),
TRY_CONVERT(datetime, order_delivered_customer_date)
)

)

AS Average_Delivery_Difference


FROM stg.orders

WHERE order_delivered_customer_date IS NOT NULL;



--------------------------------------------------
-- 5. Late Deliveries
--------------------------------------------------

SELECT

COUNT(*) AS Late_Deliveries


FROM stg.orders


WHERE

TRY_CONVERT(datetime, order_delivered_customer_date)

>

TRY_CONVERT(datetime, order_estimated_delivery_date);



--------------------------------------------------
-- 6. On Time Deliveries
--------------------------------------------------

SELECT

COUNT(*) AS On_Time_Deliveries


FROM stg.orders


WHERE

TRY_CONVERT(datetime, order_delivered_customer_date)

<=

TRY_CONVERT(datetime, order_estimated_delivery_date);



--------------------------------------------------
-- 7. Delivery Performance by Customer State
--------------------------------------------------

SELECT

c.customer_state,

AVG(o.delivery_days)

AS Average_Delivery_Days,


COUNT(*) AS Orders


FROM fact.Orders o


JOIN dim.Customer c

ON o.customer_key=c.customer_key


GROUP BY

c.customer_state


ORDER BY Average_Delivery_Days DESC;



--------------------------------------------------
-- 8. Delivery vs Review Score
--------------------------------------------------

SELECT

CASE

WHEN o.delivery_days >
0 THEN 'Delivered'

ELSE 'Other'

END AS Delivery_Status,


AVG(r.review_score)

AS Average_Rating,


COUNT(*) AS Reviews


FROM fact.Orders o


JOIN fact.Reviews r

ON o.order_id=r.order_id


GROUP BY

CASE

WHEN o.delivery_days >
0 THEN 'Delivered'

ELSE 'Other'

END;



--------------------------------------------------
-- 9. Late Delivery Review Comparison
--------------------------------------------------

SELECT


CASE

WHEN

TRY_CONVERT(datetime,s.order_delivered_customer_date)

>

TRY_CONVERT(datetime,s.order_estimated_delivery_date)

THEN 'Late'


ELSE 'On Time'


END AS Delivery_Performance,


AVG(r.review_score)

AS Average_Rating,


COUNT(*) AS Reviews


FROM stg.orders s


JOIN fact.Reviews r

ON s.order_id=r.order_id


GROUP BY


CASE

WHEN

TRY_CONVERT(datetime,s.order_delivered_customer_date)

>

TRY_CONVERT(datetime,s.order_estimated_delivery_date)

THEN 'Late'


ELSE 'On Time'

END;



--------------------------------------------------
-- 10. Delivery Delay Length
--------------------------------------------------

SELECT

AVG(

DATEDIFF(

DAY,

TRY_CONVERT(datetime,order_estimated_delivery_date),

TRY_CONVERT(datetime,order_delivered_customer_date)

)

)

AS Average_Delay_Days


FROM stg.orders


WHERE

TRY_CONVERT(datetime,order_delivered_customer_date)

>

TRY_CONVERT(datetime,order_estimated_delivery_date);