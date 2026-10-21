# Online Bookstore Management System

A simple, beginner-friendly bookstore project built using Python Flask, HTML, CSS, JavaScript, and Oracle Database. The project supports both a demo mode and an Oracle-connected mode, so it can run even before Oracle is configured.

## Features

- Customer registration and login
- Book browsing, search, and category filtering
- Book details page
- Shopping cart with add, update, and remove operations
- Checkout and order placement
- Order history and order status viewing
- Admin login, dashboard, book management, and order management
- Sales and reporting pages
- Oracle-ready PL/SQL scripts for database logic

## Technology Used

- Python Flask
- HTML5, CSS3, JavaScript
- Oracle Database
- PL/SQL
- Python `oracledb` driver
- Python `dotenv` for environment variables

## Folder Structure

```text
Online_Bookstore/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── books.html
│   ├── book_details.html
│   ├── cart.html
│   ├── checkout.html
│   ├── orders.html
│   ├── profile.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── admin_books.html
│   ├── admin_orders.html
│   └── reports.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── database/
│   ├── 01_tables.sql
│   ├── 02_constraints.sql
│   ├── 03_sample_data.sql
│   ├── 04_procedures.sql
│   ├── 05_functions.sql
│   ├── 06_triggers.sql
│   ├── 07_reports.sql
│   └── 08_test_queries.sql
└── tests/
    └── test_cases.md
```

## Python Installation

### Windows PowerShell

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Oracle Setup

1. Install Oracle Database or Oracle XE.
2. Create a database schema or user for the bookstore project.
3. Update the environment variables in a `.env` file.
4. Run SQL scripts in the order listed below.

## Environment Variable Setup

Create a `.env` file in the project root:

```env
ORACLE_USER=your_username
ORACLE_PASSWORD=your_password
ORACLE_DSN=localhost:1521/XEPDB1
SECRET_KEY=change_this_secret_key
```

Copy `.env.example` to `.env` and modify the values.

## Database Script Execution Order

Run the SQL files in this order:

1. `database/01_tables.sql`
2. `database/02_constraints.sql`
3. `database/03_sample_data.sql`
4. `database/04_procedures.sql`
5. `database/05_functions.sql`
6. `database/06_triggers.sql`
7. `database/07_reports.sql`
8. `database/08_test_queries.sql`

### Oracle SQL execution example

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

## Start the Flask App

```powershell
python app.py
```

Then open the browser at:

```text
http://127.0.0.1:5000/
```

## Demo Admin Credentials

For local demo mode, use:

- Username: `admin`
- Password: `admin123`

Demo customer example:

- Name: `Pankaj Tiwari`
- Email: `tiwaripankajo6202@gmail.com`
- Phone: `+91 8828322156`
- Password: `pankaj123`

## Project Workflow

1. User opens the homepage.
2. User registers or logs in.
3. User browses books and adds items to the cart.
4. User checks out to place an order.
5. Admin logs in to manage books and order status.
6. Reports show key sales information.

## Viva Explanation

This project demonstrates:

- Frontend design using HTML, CSS, and JavaScript
- Backend development with Flask
- Authentication and sessions
- Database integration with Oracle
- PL/SQL procedures and functions
- Business logic for orders and inventory
- Reporting using SQL queries

## Common Errors and Solutions

### 1. ModuleNotFoundError: flask

Run:

```powershell
pip install -r requirements.txt
```

### 2. Oracle connection error

Check the `.env` file values and confirm Oracle is active.

### 3. Database not found

Make sure the Oracle service is running and the DSN is correct.

### 4. Admin login fails

Use the demo admin username/password shown above.

## Future Enhancements

- Payment gateway integration
- Email notifications
- Customer reviews and ratings
- Search suggestions
- PDF invoice generation
- Role-based access control

## Notes

- The project is designed to work in demo mode if Oracle is unavailable.
- Oracle features are included in SQL scripts and configuration placeholders.
- Core database logic is implemented using PL/SQL where appropriate.
