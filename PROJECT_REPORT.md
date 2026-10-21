# Online Bookstore Management System

## Project Report

**Project title:** Online Bookstore Management System  
**Application name:** Query & Quill  
**Submitted by:** [Student name]  
**Roll number:** [Roll number]  
**Course / department:** [Course and department]  
**Institution:** [College name]  
**Academic year:** [Academic year]  
**Project guide:** [Guide name]

> Replace the bracketed fields with your college and student details before submission.

---

## Certificate

This is to certify that **[Student name]**, bearing roll number **[Roll number]**, has completed the project titled **“Online Bookstore Management System”** under my guidance, in partial fulfillment of the requirements for **[course / degree]** during the academic year **[academic year]**.

**Project guide:** ____________________  
**Head of department:** ____________________  
**Date:** ____________________  
**College seal:** ____________________

## Declaration

I declare that this project report, titled **“Online Bookstore Management System,”** is a record of the project work completed by me. The work is submitted in partial fulfillment of the requirements for **[course / degree]**. Sources, frameworks, and tools used in the project have been identified where applicable.

**Student name:** [Student name]  
**Signature:** ____________________  
**Date:** ____________________

## Acknowledgement

I would like to thank **[project guide name]**, the faculty members of **[department name]**, and **[college name]** for their guidance and support. I also acknowledge the documentation and developer communities for Flask, Python, Oracle Database, HTML, CSS, and JavaScript, which helped in developing this project.

## Abstract

The Online Bookstore Management System is a web application for browsing books and demonstrating the main activities of an online bookstore. Customers can create an account, sign in, search and filter the catalogue, view book information, manage a shopping cart, place an order, and inspect their order history. An administrator can use a separate portal to manage books, update order status, and review sales summaries.

The application is built with Python and Flask. Its pages use HTML templates rendered with Jinja, with CSS and JavaScript providing the visual design and interactive behavior. The project also includes Oracle SQL and PL/SQL scripts describing a relational database, integrity constraints, sample data, business procedures, calculation functions, triggers, reports, and test queries.

The current web application runs in demo mode and stores its operational sample data in Python in-memory lists and the Flask session. Oracle connection variables and a connection-status check are present, and the SQL layer is prepared, but the current customer, catalogue, cart, order, and administration routes are not yet backed by Oracle CRUD operations. Therefore, the application demonstrates the user workflows, while the SQL scripts provide a separate Oracle database implementation foundation. No live payment service is included.

## Table of Contents

1. Introduction
2. Problem Statement
3. Objectives and Scope
4. Requirements
5. Technologies Used
6. System Design
7. Database Design and SQL
8. Implementation
9. Development History
10. Testing and Verification
11. Limitations and Security Considerations
12. Future Enhancements
13. Conclusion
14. References
15. Appendix: Setup and Demonstration

## 1. Introduction

Bookstores need to keep a catalogue of books and make it easy for customers to find titles, review prices and availability, and follow their orders. A web-based bookstore can present these activities through one interface and give administrators a place to maintain catalogue and order information.

This project creates a learning-oriented bookstore application with two user areas:

- **Customer storefront:** book discovery, account access, cart and order workflows.
- **Administration portal:** catalogue maintenance, order-status management, and report summaries.

The project combines a Flask web application with a planned Oracle relational schema. The Flask app can be launched locally without an Oracle server, which makes it convenient for demonstration and development.

## 2. Problem Statement

A manual bookstore workflow can make catalogue updates, stock checks, order tracking, and sales summaries difficult to manage consistently. The project addresses this problem by demonstrating a centralized web interface in which:

- customers can find books by title, author, or category;
- cart and checkout logic checks quantities against the available sample stock;
- orders can be reviewed through customer and administrator pages; and
- a relational database design is provided for persistent storage and reporting.

## 3. Objectives and Scope

### 3.1 Objectives

1. Build a browser-accessible bookstore using Flask.
2. Provide customer registration, login, logout, and profile pages.
3. Display a searchable, category-filterable book catalogue.
4. Implement cart addition, quantity updates, removal, and checkout.
5. Check stock before accepting a demo order and reduce stock after placement.
6. Provide administrator pages to add, edit, and delete books and update order status.
7. Summarize order and sales information for the administrator.
8. Design Oracle tables and PL/SQL objects for the same bookstore domain.
9. Improve the storefront's responsive behavior, navigation, theme selection, and accessibility.

### 3.2 Scope

The current implementation is a local academic prototype. It demonstrates core bookstore workflows with sample data. The included database scripts describe a more persistent Oracle-backed design, but connecting every Flask operation to that schema remains future work.

Payments, shipment-provider integration, email delivery, production account recovery, and deployment to a public hosting environment are outside the current implementation.

## 4. Requirements

### 4.1 Functional requirements

| ID | Requirement |
|---|---|
| FR-01 | The visitor can view the homepage and featured books. |
| FR-02 | The visitor can browse the catalogue and search by title, author, or category. |
| FR-03 | The visitor can filter books by category and open a book detail page. |
| FR-04 | A customer can register and sign in using an email address and password. |
| FR-05 | A signed-in customer can add books to a cart, change quantities, and remove items. |
| FR-06 | Checkout validates the cart and available stock before creating a demo order. |
| FR-07 | A customer can view their order history and order details. |
| FR-08 | An administrator can sign in and manage the book catalogue. |
| FR-09 | An administrator can view orders and change an order's status. |
| FR-10 | An administrator can view sales and order summary information. |

### 4.2 Non-functional requirements

- **Usability:** consistent navigation, clear feedback messages, and responsive layouts.
- **Maintainability:** page templates, static assets, application logic, and database scripts are organized separately.
- **Data validation:** form and business rules reject missing or invalid values in the supported flows.
- **Portability for demonstration:** demo mode does not require an Oracle server.
- **Accessibility basics:** semantic page structure, a skip link, accessible labels, and keyboard-operable navigation behavior.
- **Security awareness:** password hashes are used for the Flask demo accounts; deployment-grade session, database, and credential configuration still needs hardening.

### 4.3 System requirements

- Python 3 and pip
- Flask and the packages listed in `requirements.txt`
- A modern web browser
- Optional for database-script execution: Oracle Database and Oracle SQL Developer or SQLcl
- Optional for future application-to-database integration: the Python `oracledb` driver

## 5. Technologies Used

| Technology | Role in the project |
|---|---|
| Python | Application language and demo business logic |
| Flask | Routing, request handling, sessions, flash messages, and template rendering |
| Jinja | Dynamic HTML templates |
| HTML5 | Page structure and forms |
| CSS3 | Layout, responsive styling, themes, and visual components |
| JavaScript | Theme preference, mobile navigation, and small client-side interactions |
| Oracle Database | Target relational database described by the included SQL/PLSQL scripts |
| SQL and PL/SQL | Schema definition, constraints, indexes, procedures, functions, triggers, and reports |
| `python-dotenv` | Loading local environment configuration from a `.env` file |
| Werkzeug security utilities | Password hashing and password-hash verification in Flask demo flows |

## 6. System Design

### 6.1 High-level architecture

```text
Customer / Administrator
          |
          v
      Web browser
          |
          v
 Flask routes and session state
          |
          +---- Jinja templates
          |       +---- HTML
          |       +---- CSS
          |       +---- JavaScript
          |
          +---- Current demo data
          |       +---- Python in-memory lists
          |       +---- Flask session cart
          |
          +---- Oracle connection status check
                  (does not currently back the CRUD routes)

 Separate Oracle SQL/PLSQL implementation foundation:
 tables, constraints, sample data, procedures, functions,
 triggers, reports, and test queries
```

The application separates requests into Flask routes, renders pages with templates, and styles behavior through files in `static/`. Login state and the demo cart are maintained in the Flask session. Catalogue, customer, and order records used by the current routes are held in in-memory Python structures.

The Oracle connection status is displayed by a helper that checks the configured environment variables, the optional driver, and whether a connection can be opened. This check does not imply that the bookstore pages are reading or writing their data in Oracle.

### 6.2 Main user workflows

#### Customer workflow

1. Open the homepage and view featured books.
2. Browse, search, or filter the catalogue.
3. Open a book detail page.
4. Register or sign in.
5. Add one or more books to the session-based cart.
6. Review, update, or remove cart items.
7. Proceed to checkout.
8. The server verifies that each book exists, each quantity is positive, and requested stock is available.
9. The application creates a demo order, reduces the matching in-memory stock, clears the cart, and shows the order in the customer's history.

#### Administrator workflow

1. Sign in through the separate administrator login page.
2. Review the dashboard summary.
3. Add, edit, or delete catalogue entries.
4. Review current demo orders and update their status to one of the allowed values.
5. View the reports page for sales, category, and order summaries.

### 6.3 Main routes

The Flask application includes route groups for:

- public pages: `/`, `/books`, and `/book/<book_id>`;
- customer pages: `/register`, `/login`, `/logout`, `/cart`, `/checkout`, `/orders`, `/order/<order_id>`, and `/profile`;
- administrator pages: `/admin/login`, `/admin`, `/admin/books`, `/admin/orders`, and `/admin/reports`;
- cart actions: `/cart/add`, `/cart/update`, and `/cart/remove`;
- order placement: `POST /checkout`.

Customer and administrator decorators restrict protected pages to the matching session login.

## 7. Database Design and SQL

### 7.1 Data entities

The Oracle schema models these main entities:

| Table | Purpose |
|---|---|
| `customers` | Customer contact information and stored password-hash field |
| `admins` | Administrator usernames and password field |
| `books` | Book details, category, price, stock, description, and image URL |
| `cart` | A cart associated with a customer |
| `cart_items` | Books and quantities belonging to a cart |
| `orders` | Customer order header, date, amount, status, and shipping address |
| `order_items` | Books, quantities, and purchase-time prices in each order |

### 7.2 Relationships

```text
customers 1 -------- many orders
customers 1 -------- many carts (schema permits multiple carts)
carts     1 -------- many cart_items
books     1 -------- many cart_items
orders    1 -------- many order_items
books     1 -------- many order_items
```

Foreign keys connect customer records to carts and orders, carts to cart items, and orders and books to order items. Checks constrain positive prices, non-negative stock, positive quantities, and the allowed order-status values.

### 7.3 SQL and PL/SQL script contents

The `database/` directory contains:

| File | Purpose |
|---|---|
| `00_bootstrap.sql` | Alternate starter script that creates a subset of the core schema and inserts an administrator fixture |
| `01_tables.sql` | Creates the customers, admins, books, carts, cart items, orders, and order items tables |
| `02_constraints.sql` | Adds an email check and lookup indexes |
| `03_sample_data.sql` | Inserts sample administrators, books, and customers |
| `04_procedures.sql` | Defines registration, book-management, cart, order-placement, and order-status procedures |
| `05_functions.sql` | Defines stock, order-total, cart-total, and sales calculations |
| `06_triggers.sql` | Adds stock, quantity, and timestamp validation/defaulting triggers |
| `07_reports.sql` | Provides SQL queries for best sellers, sales, category totals, order counts, and monthly trends |
| `08_test_queries.sql` | Supplies table and function queries for manual database verification |

The normal full-script sequence is `01_tables.sql` through `08_test_queries.sql`. `00_bootstrap.sql` is an alternate starter and should not be run before `01_tables.sql` in the same schema because both create overlapping tables. The bootstrap file is also a subset and is not a replacement for the complete script sequence.

### 7.4 Example database logic

The schema enforces basic business rules at the database level:

```sql
price NUMBER(10,2) NOT NULL CHECK (price > 0),
stock NUMBER(5) NOT NULL CHECK (stock >= 0),
status VARCHAR2(20) DEFAULT 'Pending' NOT NULL
    CHECK (status IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled'))
```

The order-placement procedure is designed to check stock, calculate an order total, create an order and its line items, decrement stock, clear the cart items, and commit the transaction. On an error, it rolls back and re-raises the error.

The reports script also demonstrates grouped sales calculations, for example:

```sql
SELECT b.category,
       NVL(SUM(oi.quantity * oi.price), 0) AS category_sales
FROM order_items oi
JOIN books b ON b.book_id = oi.book_id
GROUP BY b.category
ORDER BY category_sales DESC;
```

The scripts define the Oracle database layer, but the web application's current routes do not call these procedures or issue Oracle CRUD queries. The current app and database scripts are therefore related project components, not yet a fully integrated persistence path.

## 8. Implementation

### 8.1 Backend

`app.py` configures Flask, loads environment variables, defines demo records, and declares the public, customer, and administrator routes. Werkzeug's password-hash helpers are used for the demo registration/login flow. Flask sessions hold customer/admin login markers and the current cart.

The checkout route recalculates the cart total from current sample prices, validates stock, constructs an order, decrements in-memory book stock, clears the session cart, and redirects to the customer's orders page. The administrator dashboard and reports calculate their summaries from the same in-memory data.

### 8.2 Frontend

HTML pages are rendered from the `templates/` directory and share a base template for navigation, flash notifications, theme handling, and footer content. CSS in `static/css/style.css` provides the storefront and administration styling, including responsive layouts. JavaScript in `static/js/script.js` supports interactions such as the mobile navigation and persistent light/dark theme selection.

The UI redesign was intended to make the bookstore feel cohesive across the public storefront, customer pages, and administrator pages. It also includes responsive navigation, clear action feedback, and accessible navigation affordances.

### 8.3 Project organization

```text
Online_Bookstore/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── templates/       # Jinja page templates
├── static/
│   ├── css/         # Application styles
│   ├── js/          # Browser interactions
│   └── images/      # Local image assets, if used
├── database/        # Oracle SQL and PL/SQL scripts
└── tests/
    └── test_cases.md
```

## 9. Development History

The project evolved in a sequence of practical implementation stages:

1. **Initial project setup:** A Flask application was organized with page templates, static assets, a requirements file, and project documentation.
2. **Application startup and database-configuration issue:** The initial concern was that the app should not fail simply because Oracle was not installed or configured. Optional Oracle-driver handling and a demo-mode status message allow the Flask application to run without a database connection.
3. **Database design and SQL addition:** Oracle scripts were added for the schema, sample records, constraints and indexes, stored procedures, functions, triggers, reports, and test queries.
4. **Demo workflows:** Sample books, customers, and orders enabled demonstration of browsing, registration/login, cart, checkout, order history, and administration without setting up Oracle.
5. **UI/UX redesign:** The storefront, customer pages, and admin pages received a coordinated visual refresh. Responsive behavior, theme persistence, and mobile navigation interactions were included.
6. **Template rendering correction:** The order-detail template's line-item lookup was changed to use the dictionary key (`order['items']`) explicitly, avoiding a collision with the dictionary's built-in `items` method.
7. **Verification:** The redesigned application was smoke-checked through Flask requests and browser checks. The validation performed in the development session covered 16 checked pages, mobile navigation behavior, theme persistence, and horizontal overflow at a 390-pixel viewport.

This history shows the project moving from startup/database availability concerns to a runnable learning prototype, then to a more complete set of workflows and a redesigned user interface.

## 10. Testing and Verification

### 10.1 Verification performed

Previous development-session checks reported:

- HTTP 200 responses from 16 checked public, customer, and admin pages, including an order-details route;
- no horizontal page overflow in the checked 390-pixel mobile viewport;
- mobile navigation opened and closed with the Escape key; and
- selected theme preference persisted in browser local storage.

These results are application/UI smoke checks. They do **not** establish that Oracle database operations were run successfully, that every functional test case below was individually executed, or that the system is production-ready.

### 10.2 Functional test plan

The repository's `tests/test_cases.md` lists these proposed manual test cases. Its actual-result and status cells are blank, so they should be completed after the student runs each case in the submission environment.

| Test | Scenario | Expected result |
|---|---|---|
| TC-01 | Register with valid customer details | Account is created and sign-in can be attempted |
| TC-02 | Sign in with valid credentials | Customer session is created |
| TC-03 | Sign in with invalid credentials | Login fails and an error message is displayed |
| TC-04 | Search for a known book title | Matching catalogue entry is displayed |
| TC-05 | Add an available book to the cart | Cart shows the selected book and quantity |
| TC-06 | Update a cart quantity | Cart quantity and total are recalculated |
| TC-07 | Remove a cart item | Item no longer appears in the cart |
| TC-08 | Check out with a valid cart | A demo order is created |
| TC-09 | Request more copies than available | Checkout/update is rejected with a stock message |
| TC-10 | Place an order successfully | Order appears in customer order history |
| TC-11 | View order history | Only the signed-in customer's orders are listed |
| TC-12 | Sign in through the administrator portal | Admin dashboard opens |
| TC-13 | Add a valid book as administrator | Book appears in the admin catalogue |
| TC-14 | Edit a book | Updated book information is displayed |
| TC-15 | Delete a book | Book is removed from the demo catalogue |
| TC-16 | Update an order status | New allowed status appears in the order list |
| TC-17 | View reports | Current demo order and sales summaries are displayed |

## 11. Limitations and Security Considerations

1. **Demo data is not persistent.** Python in-memory customer, book, and order lists reset when the Flask process restarts. The cart uses the Flask session.
2. **Oracle routes are not integrated.** The application can check whether Oracle is configured and reachable, but the operational routes still use demo data. Running SQL scripts alone does not make the app read/write those tables.
3. **No payment processing.** Checkout creates a demonstration order and is not connected to a payment provider.
4. **Prototype authentication.** Session settings, administrator provisioning, account recovery, rate limiting, and production authentication controls need further work.
5. **Demo credentials are not production secrets.** Sample passwords and seed data exist for classroom demonstration. The sample SQL data includes plaintext password examples; these must not be used for real accounts. Production storage must use properly generated password hashes and secrets must be kept out of source control.
6. **Configuration must be hardened.** Set a strong private `SECRET_KEY`, protect `.env`, and disable Flask debug mode before any deployment.
7. **Some invalid numeric form values may need better handling.** Production-grade request validation should handle malformed price and quantity input explicitly and return clear user feedback.
8. **SQL scripts should be run in a clean, appropriately privileged development schema.** The bootstrap script overlaps with the main table script; use only one schema-creation path.
9. **Oracle logic has not been verified against a live Oracle database as part of the reported UI checks.** The procedures and reports should be compiled and exercised in Oracle before claiming integration.
10. **External book cover images rely on remote URLs.** A production deployment should consider image licensing, availability, and locally managed or approved media.

## 12. Future Enhancements

- Connect Flask data-access functions to Oracle using the `oracledb` driver and parameterized SQL or stored-procedure calls.
- Replace in-memory records with persistent database reads and writes.
- Add transactional integration tests for checkout, stock updates, and rollback behavior.
- Store only password hashes in the Oracle seed/setup process and securely provision administrator accounts.
- Add CSRF protection, stronger session cookie settings, input validation, and rate limiting.
- Add payment-provider integration using a test/sandbox environment first.
- Add email notifications, order invoices, and customer reviews.
- Improve report filtering and add charts or downloadable reports.
- Add pagination and stronger catalogue search for larger inventories.
- Deploy behind a production WSGI server with HTTPS and managed secrets.

## 13. Conclusion

The Online Bookstore Management System demonstrates the main structure of a web-based bookstore: catalogue browsing, customer account flows, cart management, checkout, order history, and administrator operations. Flask and Jinja provide the web application structure, while the redesigned CSS and JavaScript improve the interface and responsive behavior. The accompanying Oracle SQL/PLSQL scripts document a relational design and database-side business logic.

The most important implementation boundary is that the current web routes use in-memory demo data rather than Oracle persistence. The project is therefore suitable as a running classroom prototype and as a foundation for database integration, but it should not be described as a live Oracle-backed or production commerce system until that integration and security hardening have been implemented and tested.

## 14. References

- Flask documentation: <https://flask.palletsprojects.com/>
- Python documentation: <https://docs.python.org/3/>
- Oracle Database documentation: <https://docs.oracle.com/en/database/>
- Oracle Database Python driver documentation: <https://python-oracledb.readthedocs.io/>
- Werkzeug documentation: <https://werkzeug.palletsprojects.com/>

## 15. Appendix: Setup and Demonstration

### 15.1 Start the local demo

From PowerShell in the project directory:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/` in a browser. This starts the current Flask demo; Oracle is not required for the demo routes.

### 15.2 Optional Oracle script execution

Use Oracle SQL Developer or SQLcl while connected to a development schema. Run the complete schema sequence in this order:

```sql
@database/01_tables.sql
@database/02_constraints.sql
@database/03_sample_data.sql
@database/04_procedures.sql
@database/05_functions.sql
@database/06_triggers.sql
@database/07_reports.sql
@database/08_test_queries.sql
```

Do not run `00_bootstrap.sql` first in the same schema: it creates overlapping tables. For a database-focused demonstration, record the Oracle version, schema used, script output, and results of the test queries in the submission copy.
