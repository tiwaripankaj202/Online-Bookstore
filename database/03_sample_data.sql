-- 03_sample_data.sql
-- Demo/sample data for bookstore application.

PROMPT Inserting sample admin and books...

INSERT INTO admins (username, password) VALUES ('admin', 'admin123');

INSERT INTO books (title, author, category, price, stock, description, image_url) VALUES
('Python Programming', 'John Smith', 'Programming', 499.00, 12, 'Beginner-friendly Python programming guide.', 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=800&q=80'),
('Data Science Fundamentals', 'Maria Lopez', 'Data Science', 650.00, 8, 'Learn the foundations of data analysis and statistics.', 'https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=800&q=80'),
('Machine Learning Basics', 'Arun Kumar', 'AI', 720.00, 5, 'Practical overview of supervised learning concepts.', 'https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80'),
('Clean Code', 'Robert Martin', 'Software Engineering', 560.00, 15, 'Write readable and maintainable code.', 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80'),
('Artificial Intelligence', 'Aisha Rahman', 'AI', 780.00, 7, 'A clear overview of AI and intelligent systems.', 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?auto=format&fit=crop&w=800&q=80'),
('Database Management Systems', 'David Lee', 'Database', 610.00, 10, 'Understand SQL, normalization and ER models.', 'https://images.unsplash.com/photo-1544383838-bca9c0d8a10f?auto=format&fit=crop&w=800&q=80'),
('Algorithms Made Easy', 'Priya Nair', 'Computer Science', 690.00, 9, 'Study algorithmic thinking with practical examples.', 'https://images.unsplash.com/photo-1516979187454-437ec7d4b78c?auto=format&fit=crop&w=800&q=80'),
('Web Development with Python', 'Sanjay Mehta', 'Web Development', 590.00, 11, 'Build modern apps using Flask and Python.', 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80');

INSERT INTO customers (name, email, password, phone, address) VALUES
('Alice Johnson', 'alice@example.com', 'alice123', '9876543210', 'Bangalore, India'),
('Bob Smith', 'bob@example.com', 'bob123', '9123456789', 'Hyderabad, India');

COMMIT;

PROMPT Sample data inserted successfully.
