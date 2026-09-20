/*
Phase 09:
Create Fact Tables

Based on Phase 08 Fact Grain Design
*/


CREATE TABLE fact.Orders
(
    order_key INT IDENTITY(1,1) PRIMARY KEY,

    order_id VARCHAR(50) NOT NULL,

    customer_key INT NOT NULL,
    date_key INT NOT NULL,
    geography_key INT,

    order_status VARCHAR(30),

    order_count INT DEFAULT 1,

    delivery_days INT
);
GO



CREATE TABLE fact.OrderItems
(
    order_item_key INT IDENTITY(1,1) PRIMARY KEY,

    order_id VARCHAR(50) NOT NULL,

    product_key INT NOT NULL,
    seller_key INT NOT NULL,

    price DECIMAL(10,2),

    freight_value DECIMAL(10,2),

    quantity INT DEFAULT 1
);
GO



CREATE TABLE fact.Payments
(
    payment_key INT IDENTITY(1,1) PRIMARY KEY,

    order_id VARCHAR(50) NOT NULL,

    payment_sequential INT,

    payment_type VARCHAR(50),

    payment_installments INT,

    payment_value DECIMAL(10,2)
);
GO



CREATE TABLE fact.Reviews
(
    review_key INT IDENTITY(1,1) PRIMARY KEY,

    order_id VARCHAR(50) NOT NULL,

    review_score INT,

    review_creation_date DATETIME,

    review_answer_timestamp DATETIME
);
GO