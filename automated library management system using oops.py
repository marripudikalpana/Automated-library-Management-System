from datetime import datetime, timedelta


# ---------------- BOOK CLASS ---------------- #

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} | {self.author} | ₹{self.price} | {status}"


# ---------------- USER CLASS ---------------- #

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# ---------------- LIBRARY CLASS ---------------- #

class Library:
    def __init__(self):
        self.books = []
        self.users = {}
        self.current_user = None

    # ---------- VALIDATIONS ---------- #

    def is_registered(self, username):
        return username in self.users

    def is_logged_in(self):
        return self.current_user is not None

    # ---------- USER METHODS ---------- #

    def register(self, username, password):
        if self.is_registered(username):
            print("User already exists. Please login.")
        else:
            self.users[username] = User(username, password)
            print("Registration successful. Now login.")

    def login(self, username, password):
        if not self.is_registered(username):
            print("Please register first before login")
            return

        if self.users[username].password == password:
            self.current_user = username
            print("Login successful")
        else:
            print("Incorrect password")

    def logout(self):
        if self.is_logged_in():
            self.current_user = None
            print("Logged out successfully")
        else:
            print("No user is logged in")

    # ---------- BOOK METHODS ---------- #

    def add_book(self, title, author, price):
        if not self.is_logged_in():
            print("Login required to add books")
            return

        self.books.append(Book(title, author, price))
        print("Book added successfully")

    def show_books(self):
        if not self.is_logged_in():
            print("Login required")
            return

        if not self.books:
            print("No books available")
            return

        for i, book in enumerate(self.books, 1):
            print(i, ".", book)

    def borrow_book(self, title):
        if not self.is_logged_in():
            print("Login required")
            return

        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    book.borrowed_by = self.current_user
                    book.due_date = datetime.now() + timedelta(days=7)
                    print("Book borrowed. Return before:", book.due_date.date())
                else:
                    print("Book already borrowed")
                return
        print("Book not found")

    def return_book(self, title):
        if not self.is_logged_in():
            print("Login required")
            return

        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    book.borrowed_by = None
                    book.due_date = None
                    print("Book returned successfully")
                else:
                    print("Book was not borrowed")
                return
        print("Book not found")

    def remove_book(self, title):
        if not self.is_logged_in():
            print("Login required")
            return

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed")
                return
        print("Book not found")

    def search_book(self, query):
        if not self.is_logged_in():
            print("Login required")
            return

        found = False
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No books found")

    def show_overdue_books(self):
        if not self.is_logged_in():
            print("Login required")
            return

        today = datetime.now()
        found = False
        for book in self.books:
            if book.due_date and book.due_date < today:
                print(book, "| Due:", book.due_date.date())
                found = True
        if not found:
            print("No overdue books")

    def stats(self):
        if not self.is_logged_in():
            print("Login required")
            return

        total = len(self.books)
        available = sum(1 for b in self.books if b.is_available)
        borrowed = total - available

        print("Total books:", total)
        print("Available books:", available)
        print("Borrowed books:", borrowed)


# ---------------- MAIN PROGRAM ---------------- #

library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Add Book")
    print("4. Show Books")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Remove Book")
    print("8. Search Book")
    print("9. Show Overdue Books")
    print("10. Show Stats")
    print("11. Logout")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        library.register(input("Username: "), input("Password: "))

    elif choice == '2':
        library.login(input("Username: "), input("Password: "))

    elif choice == '3':
        library.add_book(input("Title: "), input("Author: "), float(input("Price: ")))

    elif choice == '4':
        library.show_books()

    elif choice == '5':
        library.borrow_book(input("Book name: "))

    elif choice == '6':
        library.return_book(input("Book name: "))

    elif choice == '7':
        library.remove_book(input("Book name: "))

    elif choice == '8':
        library.search_book(input("Search: "))

    elif choice == '9':
        library.show_overdue_books()

    elif choice == '10':
        library.stats()

    elif choice == '11':
        library.logout()

    elif choice == '12':
        print("Thank you!")
        break

    else:
        print("Invalid choice")
