CREATE DATABASE IF NOT EXISTS olistecom;

USE olistecom;

-- 1. CUSTOMERS TABLE

CREATE TABLE customers (
    customer_id CHAR(32) NOT NULL,
    customer_unique_id CHAR(32) NOT NULL,
    customer_zip_code_prefix CHAR(5),
    customer_city VARCHAR(100),
    customer_state CHAR(2),
    PRIMARY KEY (customer_id)
);

describe customers;

-- 2. SELLERS TABLE

CREATE TABLE sellers (
    seller_id CHAR(32) NOT NULL,
    seller_zip_code_prefix CHAR(5),
    seller_city VARCHAR(100),
    seller_state CHAR(2),
    PRIMARY KEY (seller_id)
);

describe sellers;

-- 3. PRODUCTS TABLE

CREATE TABLE products (
    product_id CHAR(32) NOT NULL,
    product_category_name VARCHAR(100),
    product_name_lenght INT NULL,
    product_description_lenght INT NULL,
    product_photos_qty INT NULL,
    product_weight_g INT NULL,
    product_length_cm INT NULL,
    product_height_cm INT NULL,
    product_width_cm INT NULL,
    PRIMARY KEY (product_id)
);

-- 4. ORDERS TABLE

CREATE TABLE orders (
    order_id CHAR(32) NOT NULL,
    customer_id CHAR(32) NOT NULL,
    order_status VARCHAR(20) NOT NULL,
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME NULL,
    order_delivered_carrier_date DATETIME NULL,
    order_delivered_customer_date DATETIME NULL,
    order_estimated_delivery_date DATETIME,
    PRIMARY KEY (order_id),
    CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
describe orders;

-- 5. ORDER ITEMS TABLE

CREATE TABLE order_items (
    order_id CHAR(32) NOT NULL,
    order_item_id INT NOT NULL,
    product_id CHAR(32) NOT NULL,
    seller_id CHAR(32) NOT NULL,
    shipping_limit_date DATETIME,
    price DECIMAL(10,2) NOT NULL,
    freight_value DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id,order_item_id),
    CONSTRAINT fk_items_orders
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    CONSTRAINT fk_items_products
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),
    CONSTRAINT fk_items_sellers
        FOREIGN KEY (seller_id)
        REFERENCES sellers(seller_id)
);

describe order_items;


-- 6. PAYMENTS TABLE

CREATE TABLE payments (
    order_id CHAR(32) NOT NULL,
    payment_sequential INT NOT NULL,
    payment_type VARCHAR(30) NOT NULL,
    payment_installments INT NOT NULL,
    payment_value DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, payment_sequential),
    CONSTRAINT fk_payments_orders
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

describe payments;

-- 7. REVIEWS TABLE

CREATE TABLE reviews (
    review_id CHAR(32) NOT NULL,
    order_id CHAR(32) NOT NULL,
    review_score INT NOT NULL,
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME,
    PRIMARY KEY (review_id, order_id),
    CONSTRAINT fk_reviews_orders
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

describe reviews;

SET FOREIGN_KEY_CHECKS = 0;

select * from customers;
select count(*) from customers;

select * from sellers;
select count(*) from sellers;

select * from products;
select count(*) from products;

select * from orders;
select count(*) from products;

select * from order_items;
select count(*) from order_items;

select * from payments;
select count(*) from payments;

select * from reviews;
select count(*) from reviews;

SET FOREIGN_KEY_CHECKS = 1;










