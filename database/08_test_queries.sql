-- 08_test_queries.sql
-- Test queries to validate correctness.

SELECT * FROM customers;
SELECT * FROM books;
SELECT * FROM cart;
SELECT * FROM cart_items;
SELECT * FROM orders;
SELECT * FROM order_items;

SELECT get_book_stock(1) AS stock_for_book_1 FROM dual;
SELECT calculate_order_total(1) AS order_total FROM dual;
SELECT get_cart_total(1) AS cart_total FROM dual;
SELECT get_total_sales AS total_sales FROM dual;
