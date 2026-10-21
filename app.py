import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

try:
    import oracledb  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - handled at runtime for demo mode
    oracledb = None

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change_this_secret_key")

DEMO_CUSTOMERS = [
    {
        "customer_id": 1,
        "name": "Pankaj Tiwari",
        "email": "tiwaripankajo6202@gmail.com",
        "password": generate_password_hash("pankaj123"),
        "phone": "+91 8828322156",
        "address": "India",
    },
    {
        "customer_id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "password": generate_password_hash("bob123"),
        "phone": "9123456789",
        "address": "Hyderabad, India",
    },
]

DEMO_BOOKS = [
    {
        "book_id": 1,
        "title": "Python Programming",
        "author": "John Smith",
        "category": "Programming",
        "price": 499.0,
        "stock": 12,
        "description": "Beginner-friendly Python programming guide with hands-on examples.",
        "image_url": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 2,
        "title": "Data Science Fundamentals",
        "author": "Maria Lopez",
        "category": "Data Science",
        "price": 650.0,
        "stock": 8,
        "description": "Learn the foundations of data analysis, statistics, and visualization.",
        "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 3,
        "title": "Machine Learning Basics",
        "author": "Arun Kumar",
        "category": "AI",
        "price": 720.0,
        "stock": 5,
        "description": "A practical introduction to supervised learning and model building.",
        "image_url": "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 4,
        "title": "Clean Code",
        "author": "Robert Martin",
        "category": "Software Engineering",
        "price": 560.0,
        "stock": 15,
        "description": "Write readable, maintainable, and professional software with confidence.",
        "image_url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 5,
        "title": "Artificial Intelligence",
        "author": "Aisha Rahman",
        "category": "AI",
        "price": 780.0,
        "stock": 7,
        "description": "A clear overview of AI concepts, search algorithms, and intelligent systems.",
        "image_url": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 6,
        "title": "Database Management Systems",
        "author": "David Lee",
        "category": "Database",
        "price": 610.0,
        "stock": 10,
        "description": "Understand relational databases, SQL, normalization, and indexing.",
        "image_url": "https://images.unsplash.com/photo-1544383838-bca9c0d8a10f?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 7,
        "title": "Algorithms Made Easy",
        "author": "Priya Nair",
        "category": "Computer Science",
        "price": 690.0,
        "stock": 9,
        "description": "Learn algorithmic thinking through common patterns and examples.",
        "image_url": "https://images.unsplash.com/photo-1516979187454-437ec7d4b78c?auto=format&fit=crop&w=800&q=80",
    },
    {
        "book_id": 8,
        "title": "Web Development with Python",
        "author": "Sanjay Mehta",
        "category": "Web Development",
        "price": 590.0,
        "stock": 11,
        "description": "Build dynamic web apps with Flask, HTML, CSS, and JavaScript.",
        "image_url": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
    },
]

DEMO_ORDERS = [
    {
        "order_id": 1001,
        "customer_id": 1,
        "customer_name": "Alice Johnson",
        "order_date": "2026-09-20",
        "total_amount": 1048.0,
        "status": "Delivered",
        "items": [
            {"book_id": 1, "title": "Python Programming", "quantity": 2, "price": 499.0},
            {"book_id": 4, "title": "Clean Code", "quantity": 1, "price": 560.0},
        ],
    },
    {
        "order_id": 1002,
        "customer_id": 1,
        "customer_name": "Alice Johnson",
        "order_date": "2026-09-22",
        "total_amount": 650.0,
        "status": "Processing",
        "items": [{"book_id": 2, "title": "Data Science Fundamentals", "quantity": 1, "price": 650.0}],
    },
]

DEMO_ADMIN = {"admin_id": 1, "username": "admin", "password": generate_password_hash("admin123")}


def is_oracle_configured():
    return all(
        [
            os.getenv("ORACLE_USER"),
            os.getenv("ORACLE_PASSWORD"),
            os.getenv("ORACLE_DSN"),
        ]
    )


def oracle_status_message():
    if not is_oracle_configured():
        return "Oracle is not configured yet. The app is running in demo mode."

    if not oracledb:
        return "oracledb is not installed. Install requirements and configure Oracle environment variables."

    try:
        conn = oracledb.connect(
            user=os.getenv("ORACLE_USER"),
            password=os.getenv("ORACLE_PASSWORD"),
            dsn=os.getenv("ORACLE_DSN"),
        )
        conn.close()
        return "Oracle connection successful."
    except Exception as exc:
        return f"Oracle connection failed: {exc}. The app is running in demo mode."


app.jinja_env.globals["oracle_status_message"] = oracle_status_message


def get_customer_by_email(email):
    for customer in DEMO_CUSTOMERS:
        if customer["email"].lower() == email.lower():
            return customer
    return None


def get_customer_by_id(customer_id):
    for customer in DEMO_CUSTOMERS:
        if customer["customer_id"] == int(customer_id):
            return customer
    return None


def get_book_by_id(book_id):
    for book in DEMO_BOOKS:
        if book["book_id"] == int(book_id):
            return book
    return None


def get_cart():
    return session.setdefault("cart", {})


def get_cart_total(cart):
    total = 0.0
    for item in cart.values():
        book = get_book_by_id(item["book_id"])
        if book:
            total += float(book["price"]) * int(item["quantity"])
    return round(total, 2)


def get_orders_for_customer(customer_id):
    customer_orders = []
    for order in DEMO_ORDERS:
        if order["customer_id"] == int(customer_id):
            customer_orders.append(order)
    return customer_orders


def get_admin_by_username(username):
    if DEMO_ADMIN["username"].lower() == username.lower():
        return DEMO_ADMIN
    return None


def customer_required(view_func):
    def wrapper(*args, **kwargs):
        if "customer_id" not in session:
            flash("Please log in first.", "error")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)

    wrapper.__name__ = view_func.__name__
    return wrapper


def admin_required(view_func):
    def wrapper(*args, **kwargs):
        if "admin_id" not in session:
            flash("Please log in as admin.", "error")
            return redirect(url_for("admin_login"))
        return view_func(*args, **kwargs)

    wrapper.__name__ = view_func.__name__
    return wrapper


@app.route("/")
def home():
    books = DEMO_BOOKS[:4]
    return render_template("index.html", books=books)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip()
        password = request.form.get("password") or ""

        if not email or not password:
            flash("Email and password are required.", "error")
            return redirect(url_for("login"))

        customer = get_customer_by_email(email)
        if customer and check_password_hash(customer["password"], password):
            session["customer_id"] = customer["customer_id"]
            session["customer_name"] = customer["name"]
            flash("Login successful.", "success")
            return redirect(url_for("books"))

        flash("Invalid email or password.", "error")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("customer_id", None)
    session.pop("customer_name", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip()
        password = request.form.get("password") or ""
        phone = (request.form.get("phone") or "").strip()
        address = (request.form.get("address") or "").strip()

        if not name or not email or not password or not phone or not address:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("register"))

        if get_customer_by_email(email):
            flash("Email already exists. Please use another email.", "error")
            return redirect(url_for("register"))

        new_customer = {
            "customer_id": len(DEMO_CUSTOMERS) + 1,
            "name": name,
            "email": email,
            "password": generate_password_hash(password),
            "phone": phone,
            "address": address,
        }
        DEMO_CUSTOMERS.append(new_customer)
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/books")
def books():
    category = request.args.get("category", "all").strip()
    search = request.args.get("q", "").strip().lower()

    items = DEMO_BOOKS
    if category != "all":
        items = [book for book in items if book["category"].lower() == category.lower()]
    if search:
        items = [
            book
            for book in items
            if search in book["title"].lower() or search in book["author"].lower() or search in book["category"].lower()
        ]

    categories = sorted({book["category"] for book in DEMO_BOOKS})
    return render_template("books.html", books=items, categories=categories, selected_category=category, search_query=search)


@app.route("/book/<int:book_id>")
def book_details(book_id):
    book = get_book_by_id(book_id)
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for("books"))
    return render_template("book_details.html", book=book)


@app.route("/cart")
@customer_required
def cart():
    cart_items = []
    cart = get_cart()
    for item in cart.values():
        book = get_book_by_id(item["book_id"])
        if book:
            cart_items.append({**book, "quantity": item["quantity"]})
    total = get_cart_total(cart)
    return render_template("cart.html", cart_items=cart_items, total=total)


@app.route("/cart/add", methods=["POST"])
def cart_add():
    if "customer_id" not in session:
        flash("Please log in to add books to your cart.", "error")
        return redirect(url_for("login"))

    book_id = request.form.get("book_id")
    quantity = int(request.form.get("quantity", 1))
    if not book_id:
        flash("Invalid book selection.", "error")
        return redirect(url_for("books"))

    book = get_book_by_id(book_id)
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for("books"))

    if quantity <= 0:
        flash("Quantity must be greater than zero.", "error")
        return redirect(url_for("book_details", book_id=book["book_id"]))

    cart = get_cart()
    cart_item = cart.get(str(book_id), {"book_id": int(book_id), "quantity": 0})
    cart_item["quantity"] = int(cart_item.get("quantity", 0)) + quantity
    cart[str(book_id)] = cart_item
    session["cart"] = cart
    flash(f"{book['title']} added to cart.", "success")
    return redirect(url_for("cart"))


@app.route("/cart/update", methods=["POST"])
def cart_update():
    if "customer_id" not in session:
        flash("Please log in to update your cart.", "error")
        return redirect(url_for("login"))

    cart = get_cart()
    book_id = request.form.get("book_id")
    quantity = int(request.form.get("quantity", 0))
    if not book_id:
        flash("Invalid cart update.", "error")
        return redirect(url_for("cart"))

    if quantity <= 0:
        cart.pop(str(book_id), None)
        flash("Item removed from cart.", "success")
        session["cart"] = cart
        return redirect(url_for("cart"))

    book = get_book_by_id(book_id)
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for("cart"))
    if quantity > book["stock"]:
        flash("Requested quantity exceeds stock available.", "error")
        return redirect(url_for("cart"))

    cart[str(book_id)] = {"book_id": int(book_id), "quantity": quantity}
    session["cart"] = cart
    flash("Cart updated successfully.", "success")
    return redirect(url_for("cart"))


@app.route("/cart/remove", methods=["POST"])
def cart_remove():
    if "customer_id" not in session:
        flash("Please log in to remove items.", "error")
        return redirect(url_for("login"))

    book_id = request.form.get("book_id")
    if not book_id:
        flash("Invalid item.", "error")
        return redirect(url_for("cart"))

    cart = get_cart()
    cart.pop(str(book_id), None)
    session["cart"] = cart
    flash("Item removed from cart.", "success")
    return redirect(url_for("cart"))


@app.route("/checkout")
@customer_required
def checkout():
    cart = get_cart()
    if not cart:
        flash("Your cart is empty.", "error")
        return redirect(url_for("cart"))

    customer = get_customer_by_id(session["customer_id"])
    cart_items = []
    total = 0.0
    for item in cart.values():
        book = get_book_by_id(item["book_id"])
        if book:
            subtotal = float(book["price"]) * int(item["quantity"])
            total += subtotal
            cart_items.append({"book": book, "quantity": item["quantity"], "subtotal": round(subtotal, 2)})

    return render_template("checkout.html", customer=customer, cart_items=cart_items, total=round(total, 2))


@app.route("/orders")
@customer_required
def orders():
    orders = get_orders_for_customer(session["customer_id"])
    return render_template("orders.html", orders=orders)


@app.route("/order/<int:order_id>")
@customer_required
def order_details(order_id):
    order = next((o for o in DEMO_ORDERS if o["order_id"] == order_id), None)
    if not order:
        flash("Order not found.", "error")
        return redirect(url_for("orders"))
    if order["customer_id"] != session["customer_id"]:
        flash("You cannot access this order.", "error")
        return redirect(url_for("orders"))
    return render_template("orders.html", order=order)


@app.route("/profile")
@customer_required
def profile():
    customer = get_customer_by_id(session["customer_id"])
    return render_template("profile.html", customer=customer)


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        admin = get_admin_by_username(username)
        if admin and check_password_hash(admin["password"], password):
            session["admin_id"] = admin["admin_id"]
            session["admin_username"] = admin["username"]
            flash("Admin login successful.", "success")
            return redirect(url_for("admin_dashboard"))

        flash("Invalid admin credentials.", "error")
        return redirect(url_for("admin_login"))

    return render_template("admin_login.html")


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_id", None)
    session.pop("admin_username", None)
    flash("Admin logged out.", "success")
    return redirect(url_for("home"))


@app.route("/admin")
@admin_required
def admin_dashboard():
    total_books = len(DEMO_BOOKS)
    total_orders = len(DEMO_ORDERS)
    total_sales = sum(float(order["total_amount"]) for order in DEMO_ORDERS)
    return render_template(
        "admin_dashboard.html",
        total_books=total_books,
        total_orders=total_orders,
        total_sales=round(total_sales, 2),
        recent_orders=DEMO_ORDERS[:3],
    )


@app.route("/admin/books")
@admin_required
def admin_books():
    return render_template("admin_books.html", books=DEMO_BOOKS)


@app.route("/admin/books/add", methods=["POST"])
@admin_required
def admin_books_add():
    title = (request.form.get("title") or "").strip()
    author = (request.form.get("author") or "").strip()
    category = (request.form.get("category") or "").strip()
    price = float(request.form.get("price") or 0)
    stock = int(request.form.get("stock") or 0)
    description = (request.form.get("description") or "").strip()
    image_url = (request.form.get("image_url") or "").strip() or "https://images.unsplash.com/photo-1541963463532-d68292c34b19?auto=format&fit=crop&w=800&q=80"

    if not title or not author or not category or price <= 0 or stock < 0:
        flash("All required fields must be valid.", "error")
        return redirect(url_for("admin_books"))

    new_book = {
        "book_id": len(DEMO_BOOKS) + 1,
        "title": title,
        "author": author,
        "category": category,
        "price": round(price, 2),
        "stock": stock,
        "description": description,
        "image_url": image_url,
    }
    DEMO_BOOKS.append(new_book)
    flash("Book added successfully.", "success")
    return redirect(url_for("admin_books"))


@app.route("/admin/books/edit/<int:book_id>", methods=["GET", "POST"])
@admin_required
def admin_books_edit(book_id):
    book = get_book_by_id(book_id)
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for("admin_books"))

    if request.method == "POST":
        book["title"] = (request.form.get("title") or book["title"]).strip()
        book["author"] = (request.form.get("author") or book["author"]).strip()
        book["category"] = (request.form.get("category") or book["category"]).strip()
        book["price"] = round(float(request.form.get("price") or book["price"]), 2)
        book["stock"] = int(request.form.get("stock") or book["stock"])
        book["description"] = (request.form.get("description") or book["description"]).strip()
        book["image_url"] = (request.form.get("image_url") or book["image_url"]).strip() or book["image_url"]
        flash("Book updated successfully.", "success")
        return redirect(url_for("admin_books"))

    return render_template("admin_books.html", edit_book=book, books=DEMO_BOOKS)


@app.route("/admin/books/delete/<int:book_id>", methods=["POST"])
@admin_required
def admin_books_delete(book_id):
    book = get_book_by_id(book_id)
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for("admin_books"))

    DEMO_BOOKS[:] = [b for b in DEMO_BOOKS if b["book_id"] != book_id]
    flash(f"{book['title']} deleted successfully.", "success")
    return redirect(url_for("admin_books"))


@app.route("/admin/orders")
@admin_required
def admin_orders():
    return render_template("admin_orders.html", orders=DEMO_ORDERS)


@app.route("/admin/orders/update/<int:order_id>", methods=["POST"])
@admin_required
def admin_orders_update(order_id):
    order = next((o for o in DEMO_ORDERS if o["order_id"] == order_id), None)
    if not order:
        flash("Order not found.", "error")
        return redirect(url_for("admin_orders"))

    status = (request.form.get("status") or order["status"]).strip()
    allowed_status = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
    if status not in allowed_status:
        flash("Invalid order status.", "error")
        return redirect(url_for("admin_orders"))

    order["status"] = status
    flash("Order status updated successfully.", "success")
    return redirect(url_for("admin_orders"))


@app.route("/admin/reports")
@admin_required
def admin_reports():
    total_sales = sum(float(order["total_amount"]) for order in DEMO_ORDERS)
    best_sellers = []
    category_sales = {}
    for order in DEMO_ORDERS:
        for item in order["items"]:
            best_sellers.append(item)
            category = get_book_by_id(item["book_id"])["category"] if get_book_by_id(item["book_id"]) else "Unknown"
            category_sales[category] = category_sales.get(category, 0) + item["quantity"] * item["price"]

    return render_template(
        "reports.html",
        total_sales=round(total_sales, 2),
        sales_by_category=sorted(category_sales.items()),
        best_sellers=best_sellers,
        pending_orders=sum(1 for order in DEMO_ORDERS if order["status"] == "Pending"),
        delivered_orders=sum(1 for order in DEMO_ORDERS if order["status"] == "Delivered"),
        order_count=len(DEMO_ORDERS),
    )


@app.route("/checkout", methods=["POST"])
@customer_required
def place_order():
    cart = get_cart()
    if not cart:
        flash("Your cart is empty.", "error")
        return redirect(url_for("cart"))

    order_items = []
    total = 0.0
    for item in cart.values():
        book = get_book_by_id(item["book_id"])
        if not book:
            flash(f"Book {item['book_id']} not found.", "error")
            return redirect(url_for("cart"))
        quantity = int(item["quantity"])
        if quantity <= 0:
            flash("Invalid quantity found in cart.", "error")
            return redirect(url_for("cart"))
        if quantity > book["stock"]:
            flash(f"Insufficient stock for {book['title']}.", "error")
            return redirect(url_for("cart"))

        subtotal = float(book["price"]) * quantity
        total += subtotal
        order_items.append({"book_id": book["book_id"], "quantity": quantity, "price": float(book["price"]), "title": book["title"]})

    new_order = {
        "order_id": max((o["order_id"] for o in DEMO_ORDERS), default=1000) + 1,
        "customer_id": session["customer_id"],
        "customer_name": session["customer_name"],
        "order_date": datetime.now().strftime("%Y-%m-%d"),
        "total_amount": round(total, 2),
        "status": "Pending",
        "items": order_items,
    }

    for item in order_items:
        for book in DEMO_BOOKS:
            if book["book_id"] == item["book_id"]:
                book["stock"] = max(0, book["stock"] - item["quantity"])
                break

    DEMO_ORDERS.append(new_order)
    session["cart"] = {}
    flash("Order placed successfully.", "success")
    return redirect(url_for("orders"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html", books=DEMO_BOOKS[:4]), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 
