# 📚 Automated Library Management System (Using OOP in Python)
## 📌 Project Overview

This project is a console-based Library Management System built using Object-Oriented Programming (OOP) concepts in Python.
It allows users to manage books and perform operations like adding, borrowing, returning, and searching books with proper user authentication (register & login system).

## 🎯 Features

## 👤 User Management
- User Registration
- User Login
- Logout functionality
- Only logged-in users can perform operations

## 📖 Book Management
- Add new books
- View all books
- Search books (by title or author)
- Remove books

## 🔄 Borrowing System
- Borrow books
- Return books
- Track borrowed books
- Due date (7 days borrowing limit)

## ⏰ Overdue Tracking
Displays books that are not returned on time

## 🏗️ Project Structure
### 1. Book Class

Represents each book in the library.

 Attributes:

- Title
- Author
- Price
- Availability status
- Borrowed by
- Due date
### 2. User Class

Stores user login details.

Attributes:

- Username
- Password
### 3. Library Class

Main class that controls the system.

Responsibilities:

- Manage users
- Manage books
- Handle borrowing/returning
- Maintain login session
- Provide statistics

## 🔐 Authentication Rule
- User must register first
- Then login
- Without login → No operations allowed

## ⚙️ Functional Workflow
1. Start the program
2. Register a new user
3. Login with credentials
4. Perform operations like:
- Add books
- View books
- Borrow/Return books
- Search books
5.  Logout or Exit

## 🧠 Concepts Used
- Object-Oriented Programming (OOP)
   - Classes & Objects
   - Encapsulation
- Lists & Dictionaries (Data Structures)
- Conditional Statements
- Loops
- Functions/Methods
- Date & Time handling (datetime, timedelta)
## 🖥️ Menu Options
1. Register
2. Login
3. Add Book
4. Show Books
5. Borrow Book
6. Return Book
7. Remove Book
8. Search Book
9. Show Overdue Books
10. Show Stats
11. Logout
12. Exit
## ⚠️ Limitations
- Data is not stored permanently (no database)
- Runs only in command line
- No GUI interface
- Passwords are not encrypted

## 🚀 Future Improvements
- Add database (MySQL / SQLite)
- Build GUI (Tkinter / Web using Django)
- Add fine calculation for late returns
- Encrypt passwords
- Add multiple user roles (Admin/User)

## ✅ Conclusion

This project demonstrates how real-world applications can be built using Python OOP concepts. It clearly shows how to organize code using classes and manage data efficiently with lists and dictionaries.

The system ensures security through login, efficient book handling, and introduces concepts like due dates and overdue tracking, making it a strong foundation for building advanced applications like web-based library systems.
