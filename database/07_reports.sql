-- 07_reports.sql
-- Reporting queries for sales and order summaries.

PROMPT Best-selling books
SELECT b.title,
       SUM(oi.quantity) AS total_quantity
FROM order_items oi
JOIN books b ON b.book_id = oi.book_id
GROUP BY b.title
ORDER BY total_quantity DESC;

PROMPT Total sales
SELECT NVL(SUM(total_amount), 0) AS total_sales
FROM orders;

PROMPT Sales by category
SELECT b.category,
       NVL(SUM(oi.quantity * oi.price), 0) AS category_sales
FROM order_items oi
JOIN books b ON b.book_id = oi.book_id
GROUP BY b.category
ORDER BY category_sales DESC;

PROMPT Order count
SELECT COUNT(*) AS order_count
FROM orders;

PROMPT Pending orders
SELECT *
FROM orders
WHERE status = 'Pending'
ORDER BY order_date;

PROMPT Delivered orders
SELECT *
FROM orders
WHERE status = 'Delivered'
ORDER BY order_date;

PROMPT Sales trends by month
SELECT TO_CHAR(order_date, 'YYYY-MM') AS sales_month,
       SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY sales_month;
