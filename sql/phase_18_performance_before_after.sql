-- ==========================================
-- PHASE 18
-- BEFORE OPTIMIZATION
-- Seller Performance Analysis
-- ==========================================


SET STATISTICS TIME ON;
SET STATISTICS IO ON;


SELECT

    s.seller_id,

    COUNT(DISTINCT oi.order_id) AS Total_Orders,

    COUNT(oi.product_key) AS Products_Sold,

    SUM(oi.price) AS Merchandise_Value,

    SUM(oi.freight_value) AS Freight_Value,

    AVG(r.review_score) AS Average_Review_Score


FROM fact.OrderItems oi


JOIN dim.Seller s

ON oi.seller_key = s.seller_key


LEFT JOIN fact.Reviews r

ON oi.order_id = r.order_id


GROUP BY

s.seller_id


ORDER BY

Merchandise_Value DESC;



SET STATISTICS TIME OFF;
SET STATISTICS IO OFF;



-- ==========================================
-- AFTER OPTIMIZATION
-- Seller Performance Analysis
-- ==========================================


SET STATISTICS TIME ON;
SET STATISTICS IO ON;


WITH SellerSales AS
(

SELECT

    seller_key,

    COUNT(DISTINCT order_id) AS Total_Orders,

    COUNT(*) AS Products_Sold,

    SUM(price) AS Merchandise_Value,

    SUM(freight_value) AS Freight_Value


FROM fact.OrderItems


GROUP BY

seller_key

),


SellerReviews AS

(

SELECT

    order_id,

    AVG(review_score) AS Average_Review_Score


FROM fact.Reviews


GROUP BY order_id

)


SELECT


s.seller_id,


ss.Total_Orders,

ss.Products_Sold,

ss.Merchandise_Value,

ss.Freight_Value,


AVG(sr.Average_Review_Score)
AS Average_Review_Score


FROM SellerSales ss


JOIN dim.Seller s

ON ss.seller_key = s.seller_key


LEFT JOIN fact.OrderItems oi

ON ss.seller_key = oi.seller_key


LEFT JOIN SellerReviews sr

ON oi.order_id = sr.order_id


GROUP BY

s.seller_id,

ss.Total_Orders,

ss.Products_Sold,

ss.Merchandise_Value,

ss.Freight_Value;



SET STATISTICS TIME OFF;
SET STATISTICS IO OFF;

-- Supporting indexes

CREATE INDEX IX_OrderItems_SellerKey
ON fact.OrderItems(seller_key);


CREATE INDEX IX_OrderItems_OrderID
ON fact.OrderItems(order_id);


CREATE INDEX IX_Reviews_OrderID
ON fact.Reviews(order_id);