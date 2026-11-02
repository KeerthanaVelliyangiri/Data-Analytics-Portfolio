# KPI Analysis

# 1. Total Orders

SELECT COUNT(DISTINCT order_id) AS total_orders
FROM orders;

# 2.Average Customer Review Score

SELECT ROUND(AVG(review_score), 2) AS average_review_score
FROM reviews
WHERE review_score IS NOT NULL;

# 3. Delivered Orders

SELECT COUNT(DISTINCT order_id) AS delivered_orders
FROM orders
WHERE order_status = 'delivered';

# 4. On-Time Delivery Rate

SELECT ROUND(COUNT(CASE
	WHEN order_delivered_customer_date <= order_estimated_delivery_date
	THEN 1
	END) * 100.0 / COUNT(*),2) AS on_time_delivery_rate_pct
FROM orders
WHERE order_status = 'delivered'
AND order_delivered_customer_date IS NOT NULL
AND order_estimated_delivery_date IS NOT NULL;

# 5 . Delayed Delivery Rate

SELECT ROUND(COUNT(CASE
	WHEN order_delivered_customer_date > order_estimated_delivery_date
	THEN 1
	END) * 100.0 / COUNT(*),2) AS delayed_delivery_rate_pct
FROM orders
WHERE order_status = 'delivered'
AND order_delivered_customer_date IS NOT NULL
AND order_estimated_delivery_date IS NOT NULL;


# Business Analysis

# 1.Monthly Customer Satisfaction Trend

SELECT
    DATE_FORMAT(review_creation_date, '%Y-%m') AS review_month,
    ROUND(AVG(review_score), 2) AS average_review_score
FROM reviews
WHERE review_score IS NOT NULL
GROUP BY review_month
ORDER BY review_month;

# 2.Customer Review Score Distribution

SELECT review_score,COUNT(DISTINCT order_id) AS reviewed_orders
FROM reviews
WHERE review_score IS NOT NULL
GROUP BY review_score
ORDER BY review_score;

# 3.Delivery Performance

SELECT
    CASE
        WHEN order_delivered_customer_date <= order_estimated_delivery_date
        THEN 'On Time'
        ELSE 'Delayed'
    END AS delivery_status,
    COUNT(*) AS total_orders
FROM orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
GROUP BY delivery_status;

# 4. Average Review Score by Product Category

SELECT p.product_category_name,ROUND(AVG(r.review_score), 2) AS average_review_score
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN reviews r
ON oi.order_id = r.order_id
GROUP BY p.product_category_name
ORDER BY average_review_score DESC;

# 5. Lowest-Rated Product Categories

SELECT p.product_category_name,ROUND(AVG(r.review_score), 2) AS average_review_score
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN reviews r
ON oi.order_id = r.order_id
GROUP BY p.product_category_name
ORDER BY average_review_score ASC
LIMIT 10;

# 6. Seller Satisfaction Comparison

SELECT oi.seller_id,ROUND(AVG(r.review_score), 2) AS average_review_score
FROM order_items oi
JOIN reviews r
ON oi.order_id = r.order_id
GROUP BY oi.seller_id
ORDER BY average_review_score DESC;

# 7. Delivery Delays vs Customer Review Score

SELECT
    CASE
        WHEN o.order_delivered_customer_date <= o.order_estimated_delivery_date
        THEN 'On Time'
        ELSE 'Delayed'
    END AS delivery_status,
    r.review_score,COUNT(*) AS total_orders
FROM orders o
JOIN reviews r
ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
GROUP BY delivery_status, r.review_score
ORDER BY delivery_status, r.review_score;

# 8. Monthly Review Count

SELECT DATE_FORMAT(review_creation_date, '%Y-%m') AS review_month,COUNT(*) AS total_reviews
FROM reviews
GROUP BY review_month
ORDER BY review_month;

# 9.Customer Review Score Distribution

SELECT
    review_score,
    COUNT(*) AS total_reviews
FROM reviews
WHERE review_score IS NOT NULL
GROUP BY review_score
ORDER BY review_score;

# 10. Customer Satisfaction by Review Score

SELECT
    CASE
        WHEN review_score >= 4 THEN 'Positive'
        WHEN review_score = 3 THEN 'Neutral'
        ELSE 'Negative'
    END AS customer_satisfaction,
    COUNT(*) AS total_reviews
FROM reviews
WHERE review_score IS NOT NULL
GROUP BY customer_satisfaction;

