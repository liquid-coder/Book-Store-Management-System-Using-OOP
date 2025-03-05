<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Store Management System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1 {
            text-align: center;
            color: #4CAF50;
        }
        h2 {
            color: #333;
        }
        ul {
            list-style-type: none;
        }
        li {
            margin: 10px 0;
        }
        .features, .technologies, .project-structure {
            margin-bottom: 20px;
        }
        .features li, .technologies li, .project-structure li {
            margin-left: 20px;
        }
    </style>
</head>
<body>

   <h1>🍽️ Book Store Management System</h1>

  <p>This project is a <strong>Book Store Management System</strong> built using <strong>Object-Oriented Programming (OOP)</strong> principles in Python. It provides a simple and efficient way to manage a bookstore's inventory, allowing users to add, remove, search, and view books seamlessly.</p>

  <section class="features">
        <h2>✨ Features</h2>
        <ul>
            <li>✅ <strong>Add New Books</strong> – Insert book details such as title, author, genre, and quantity.</li>
            <li>✅ <strong>Remove Books</strong> – Delete books from inventory using a unique ID or title.</li>
            <li>✅ <strong>Search Books</strong> – Find books by title, author, or category.</li>
            <li>✅ <strong>View Inventory</strong> – Display all available books in an organized format.</li>
            <li>✅ <strong>Data Persistence</strong> – Stores book details securely using JSON for easy retrieval.</li>
        </ul>
    </section>

  <section class="project-structure">
        <h2>🏗️ Project Structure</h2>
        <pre>
📦 Book-Store-Management-System
├── 📄 main.py         # entry point of the system
├── 📄 add_book.py     # user can add books
├── 📄 remove_book.py  # remove any books by providing book id
├── 📄 search_book.py  # search any book by providing book id
├── 📄 view_books.py   # show the current list of books
├── 📄 book_data.py    # stores book information and inventory operations
└── 📄 books.json      # json file where the book details are stored
        </pre>
    </section>

  <section class="technologies">
        <h2>📂 Technologies Used</h2>
        <ul>
            <li><strong>Python</strong></li>
            <li><strong>OOP (Encapsulation, Inheritance, Polymorphism)</strong></li>
        </ul>
    </section>

</body>
</html>
