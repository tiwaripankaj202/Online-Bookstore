-- 06_triggers.sql
-- Simple Oracle triggers for integrity and validation.

CREATE OR REPLACE TRIGGER trg_books_stock_check
BEFORE INSERT OR UPDATE OF stock ON books
FOR EACH ROW
BEGIN
    IF :NEW.stock < 0 THEN
        RAISE_APPLICATION_ERROR(-20009, 'Stock cannot be negative.');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_orders_quantity_check
BEFORE INSERT OR UPDATE OF quantity ON order_items
FOR EACH ROW
BEGIN
    IF :NEW.quantity <= 0 THEN
        RAISE_APPLICATION_ERROR(-20010, 'Order quantity must be greater than zero.');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_set_order_date
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF :NEW.order_date IS NULL THEN
        :NEW.order_date := SYSTIMESTAMP;
    END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_set_created_at
BEFORE INSERT OR UPDATE ON books
FOR EACH ROW
BEGIN
    IF :NEW.created_at IS NULL THEN
        :NEW.created_at := SYSTIMESTAMP;
    END IF;
END;
/
