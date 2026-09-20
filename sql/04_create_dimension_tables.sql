/*
Phase 09:
Create Dimension Tables

Based on Phase 08 Dimensional Model
*/


CREATE TABLE dim.Customer
(
    customer_key INT IDENTITY(1,1) PRIMARY KEY,

    customer_unique_id VARCHAR(50) NOT NULL,

    customer_city VARCHAR(100),
    customer_state VARCHAR(10),
    customer_zip_code_prefix INT
);
GO



CREATE TABLE dim.Category
(
    category_key INT IDENTITY(1,1) PRIMARY KEY,

    product_category_name VARCHAR(100),

    product_category_name_english VARCHAR(100)
);
GO



CREATE TABLE dim.Product
(
    product_key INT IDENTITY(1,1) PRIMARY KEY,

    product_id VARCHAR(50) NOT NULL,

    category_key INT,

    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);
GO


CREATE TABLE dim.Seller
(
    seller_key INT IDENTITY(1,1) PRIMARY KEY,

    seller_id VARCHAR(50) NOT NULL,

    seller_city VARCHAR(100),
    seller_state VARCHAR(10),
    seller_zip_code_prefix INT
);
GO



CREATE TABLE dim.Geography
(
    geography_key INT IDENTITY(1,1) PRIMARY KEY,

    geolocation_zip_code_prefix INT,

    geolocation_city VARCHAR(100),
    geolocation_state VARCHAR(10),

    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7)
);
GO



CREATE TABLE dim.Date
(
    date_key INT PRIMARY KEY,

    full_date DATE,

    day INT,
    month INT,
    quarter INT,
    year INT
);
GO