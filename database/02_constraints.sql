-- 02_constraints.sql
-- Additional constraints and indexes for integrity and performance.

PROMPT Adding constraints and indexes...

ALTER TABLE customers
    ADD CONSTRAINT chk_customer_email CHECK (email LIKE '%@%');

ALTER TABLE admins
    ADD CONSTRAINT chk_admin_username CHECK (username IS NOT NULL);

CREATE INDEX idx_books_category ON books(category);
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_cart_customer ON cart(customer_id);
CREATE INDEX idx_cart_items_cart ON cart_items(cart_id);
CREATE INDEX idx_cart_items_book ON cart_items(book_id);

PROMPT Constraints and indexes added successfully.
