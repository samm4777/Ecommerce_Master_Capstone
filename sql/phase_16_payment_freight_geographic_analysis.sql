/*
Phase 16:
Payment, Freight & Geographic Analysis
*/


/****************************************************
1. PAYMENT ANALYSIS
****************************************************/


-- Payment method usage and value contribution

SELECT
    payment_type,
    COUNT(DISTINCT order_id) AS Orders,
    SUM(payment_value) AS Total_Payment_Value,
    AVG(payment_value) AS Average_Payment_Value
FROM stg.payments
GROUP BY payment_type
ORDER BY Total_Payment_Value DESC;



-- Installment behaviour

SELECT
    payment_installments,
    COUNT(DISTINCT order_id) AS Orders,
    SUM(payment_value) AS Payment_Value,
    AVG(payment_value) AS Average_Order_Value
FROM stg.payments
GROUP BY payment_installments
ORDER BY payment_installments;



-- Payment concentration

SELECT

    COUNT(DISTINCT order_id) AS Total_Orders,

    SUM(payment_value) AS Total_Payment_Value,

    AVG(payment_value) AS Average_Order_Payment

FROM stg.payments;



/****************************************************
2. FREIGHT ANALYSIS
****************************************************/


-- Freight compared with product value

SELECT

    SUM(price) AS Merchandise_Value,

    SUM(freight_value) AS Freight_Value,

    (SUM(freight_value) /
     NULLIF(SUM(price),0))*100
     AS Freight_Percentage

FROM stg.order_items;



-- Freight burden by category

SELECT

    p.product_category_name,

    SUM(oi.price) AS Product_Value,

    SUM(oi.freight_value) AS Freight_Value,

    (SUM(oi.freight_value) /
     NULLIF(SUM(oi.price),0))*100
     AS Freight_Percentage

FROM stg.order_items oi

LEFT JOIN stg.products p
ON oi.product_id = p.product_id

GROUP BY
p.product_category_name

ORDER BY Freight_Percentage DESC;



-- Freight by seller

SELECT

    seller_id,

    SUM(price) AS Product_Value,

    SUM(freight_value) AS Freight_Value,

    (SUM(freight_value) /
     NULLIF(SUM(price),0))*100
     AS Freight_Percentage

FROM stg.order_items

GROUP BY seller_id

ORDER BY Freight_Percentage DESC;



/****************************************************
3. GEOGRAPHIC ANALYSIS
****************************************************/


-- Customers by state

SELECT

    customer_state,

    COUNT(*) AS Customers

FROM dim.Customer

GROUP BY customer_state

ORDER BY Customers DESC;



-- Sales by customer state

SELECT

    c.customer_state,

    COUNT(o.order_id) AS Orders,

    SUM(oi.price) AS Revenue

FROM fact.Orders o

JOIN dim.Customer c
ON o.customer_key = c.customer_key

JOIN fact.OrderItems oi
ON o.order_id = oi.order_id

GROUP BY c.customer_state

ORDER BY Revenue DESC;



-- Seller distribution

SELECT

    seller_state,

    COUNT(*) AS Sellers

FROM dim.Seller

GROUP BY seller_state

ORDER BY Sellers DESC;



-- Delivery performance by customer state


SELECT

    c.customer_state,

    AVG(o.delivery_days)
    AS Average_Delivery_Days,

    COUNT(o.order_id)
    AS Orders


FROM fact.Orders o

JOIN dim.Customer c

ON o.customer_key = c.customer_key


GROUP BY c.customer_state

ORDER BY Average_Delivery_Days DESC;