/*
Phase 09:
Create staging tables

Purpose:
Temporary landing area for prepared Python output files.
*/


CREATE TABLE stg.customers
(
    customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
);
GO


CREATE TABLE stg.orders
(
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(30),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME
);
GO


CREATE TABLE stg.order_items
(
    order_id VARCHAR(50),
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATETIME,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2)
);
GO


CREATE TABLE stg.payments
(
    order_id VARCHAR(50),
    payment_sequential INT,
    payment_type VARCHAR(50),
    payment_installments INT,
    payment_value DECIMAL(10,2)
);
GO


CREATE TABLE stg.products
(
    product_id VARCHAR(50),
    product_category_name VARCHAR(100),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);
GO


CREATE TABLE stg.sellers
(
    seller_id VARCHAR(50),
    seller_zip_code_prefix INT,
    seller_city VARCHAR(100),
    seller_state VARCHAR(10)
);
GO


CREATE TABLE stg.category_translation
(
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100)
);
GO


CREATE TABLE stg.reviews
(
    review_id VARCHAR(50),
    order_id VARCHAR(50),
    review_score INT,
    review_comment_title VARCHAR(255),
    review_comment_message VARCHAR(MAX),
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME
);
GO


CREATE TABLE stg.geolocation
(
    geolocation_zip_code_prefix INT,
    geolocation_lat DECIMAL(10,7),
    geolocation_lng DECIMAL(10,7),
    geolocation_city VARCHAR(100),
    geolocation_state VARCHAR(10)
);
GO