-- 05_functions.sql
-- PL/SQL functions for stock and sales calculations.

CREATE OR REPLACE FUNCTION get_book_stock (p_book_id IN NUMBER) RETURN NUMBER AS
    v_stock NUMBER;
BEGIN
    SELECT stock INTO v_stock
    FROM books
    WHERE book_id = p_book_id;

    RETURN v_stock;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 0;
END;
/

CREATE OR REPLACE FUNCTION calculate_order_total (p_order_id IN NUMBER) RETURN NUMBER AS
    v_total NUMBER := 0;
BEGIN
    SELECT NVL(SUM(quantity * price), 0) INTO v_total
    FROM order_items
    WHERE order_id = p_order_id;

    RETURN v_total;
EXCEPTION
    WHEN OTHERS THEN
        RETURN 0;
END;
/

CREATE OR REPLACE FUNCTION get_cart_total (p_customer_id IN NUMBER) RETURN NUMBER AS
    v_total NUMBER := 0;
BEGIN
    SELECT NVL(SUM(ci.quantity * b.price), 0) INTO v_total
    FROM cart c
    JOIN cart_items ci ON c.cart_id = ci.cart_id
    JOIN books b ON ci.book_id = b.book_id
    WHERE c.customer_id = p_customer_id;

    RETURN v_total;
EXCEPTION
    WHEN OTHERS THEN
        RETURN 0;
END;
/

CREATE OR REPLACE FUNCTION get_total_sales RETURN NUMBER AS
    v_total NUMBER := 0;
BEGIN
    SELECT NVL(SUM(total_amount), 0) INTO v_total
    FROM orders
    WHERE status IN ('Pending', 'Processing', 'Shipped', 'Delivered');

    RETURN v_total;
EXCEPTION
    WHEN OTHERS THEN
        RETURN 0;
END;
/
