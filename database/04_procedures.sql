-- 04_procedures.sql
-- PL/SQL procedures for customer registration, cart operations, and orders.

CREATE OR REPLACE PROCEDURE register_customer (
    p_name IN VARCHAR2,
    p_email IN VARCHAR2,
    p_password IN VARCHAR2,
    p_phone IN VARCHAR2,
    p_address IN VARCHAR2
) AS
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM customers
    WHERE LOWER(email) = LOWER(p_email);

    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Duplicate email: customer already exists.');
    END IF;

    INSERT INTO customers (name, email, password, phone, address)
    VALUES (p_name, p_email, p_password, p_phone, p_address);

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE add_book (
    p_title IN VARCHAR2,
    p_author IN VARCHAR2,
    p_category IN VARCHAR2,
    p_price IN NUMBER,
    p_stock IN NUMBER,
    p_description IN CLOB,
    p_image_url IN VARCHAR2
) AS
BEGIN
    INSERT INTO books (title, author, category, price, stock, description, image_url)
    VALUES (p_title, p_author, p_category, p_price, p_stock, p_description, p_image_url);

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE update_book (
    p_book_id IN NUMBER,
    p_title IN VARCHAR2,
    p_author IN VARCHAR2,
    p_category IN VARCHAR2,
    p_price IN NUMBER,
    p_stock IN NUMBER,
    p_description IN CLOB,
    p_image_url IN VARCHAR2
) AS
BEGIN
    UPDATE books
    SET title = p_title,
        author = p_author,
        category = p_category,
        price = p_price,
        stock = p_stock,
        description = p_description,
        image_url = p_image_url
    WHERE book_id = p_book_id;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'Book not found.');
    END IF;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE delete_book (p_book_id IN NUMBER) AS
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM order_items
    WHERE book_id = p_book_id;

    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'Cannot delete book because it has order history.');
    END IF;

    DELETE FROM books WHERE book_id = p_book_id;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'Book not found.');
    END IF;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE add_to_cart (
    p_customer_id IN NUMBER,
    p_book_id IN NUMBER,
    p_quantity IN NUMBER
) AS
    v_cart_id NUMBER;
    v_count NUMBER;
BEGIN
    IF p_quantity <= 0 THEN
        RAISE_APPLICATION_ERROR(-20005, 'Quantity must be greater than zero.');
    END IF;

    SELECT cart_id INTO v_cart_id
    FROM cart
    WHERE customer_id = p_customer_id;

    SELECT COUNT(*) INTO v_count
    FROM cart_items
    WHERE cart_id = v_cart_id AND book_id = p_book_id;

    IF v_count > 0 THEN
        UPDATE cart_items
        SET quantity = quantity + p_quantity
        WHERE cart_id = v_cart_id AND book_id = p_book_id;
    ELSE
        INSERT INTO cart_items (cart_id, book_id, quantity)
        VALUES (v_cart_id, p_book_id, p_quantity);
    END IF;

    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        INSERT INTO cart (customer_id) VALUES (p_customer_id);
        SELECT cart_id INTO v_cart_id
        FROM cart
        WHERE customer_id = p_customer_id;

        INSERT INTO cart_items (cart_id, book_id, quantity)
        VALUES (v_cart_id, p_book_id, p_quantity);
        COMMIT;
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE remove_from_cart (
    p_cart_id IN NUMBER,
    p_book_id IN NUMBER
) AS
BEGIN
    DELETE FROM cart_items
    WHERE cart_id = p_cart_id AND book_id = p_book_id;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20006, 'Item not found in cart.');
    END IF;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE place_order (
    p_customer_id IN NUMBER,
    p_shipping_address IN VARCHAR2
) AS
    v_cart_id NUMBER;
    v_total NUMBER := 0;
    v_order_id NUMBER;
    v_book_id NUMBER;
    v_quantity NUMBER;
    v_price NUMBER;
    v_stock NUMBER;
BEGIN
    SELECT cart_id INTO v_cart_id
    FROM cart
    WHERE customer_id = p_customer_id;

    FOR item_rec IN (
        SELECT ci.book_id, ci.quantity, b.price
        FROM cart_items ci
        JOIN books b ON ci.book_id = b.book_id
        WHERE ci.cart_id = v_cart_id
    ) LOOP
        SELECT stock INTO v_stock
        FROM books
        WHERE book_id = item_rec.book_id;

        IF item_rec.quantity > v_stock THEN
            RAISE_APPLICATION_ERROR(-20007, 'Insufficient stock for one or more books.');
        END IF;

        v_total := v_total + (item_rec.quantity * item_rec.price);
    END LOOP;

    INSERT INTO orders (customer_id, total_amount, shipping_address)
    VALUES (p_customer_id, v_total, p_shipping_address)
    RETURNING order_id INTO v_order_id;

    FOR item_rec IN (
        SELECT ci.book_id, ci.quantity, b.price
        FROM cart_items ci
        JOIN books b ON ci.book_id = b.book_id
        WHERE ci.cart_id = v_cart_id
    ) LOOP
        INSERT INTO order_items (order_id, book_id, quantity, price)
        VALUES (v_order_id, item_rec.book_id, item_rec.quantity, item_rec.price);

        UPDATE books
        SET stock = stock - item_rec.quantity
        WHERE book_id = item_rec.book_id;
    END LOOP;

    DELETE FROM cart_items WHERE cart_id = v_cart_id;
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

CREATE OR REPLACE PROCEDURE update_order_status (
    p_order_id IN NUMBER,
    p_status IN VARCHAR2
) AS
BEGIN
    UPDATE orders
    SET status = p_status
    WHERE order_id = p_order_id;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20008, 'Order not found.');
    END IF;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/
