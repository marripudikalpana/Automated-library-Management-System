library = []

def add_book(title, author):
    library.append({"title": title, "author": author, "is_available": True})
    print("Book added:", title, "by", author)

def show_all_books():
    print("\nLibrary Inventory")
    if not library:
        print("Library is empty")
        return
    for i, book in enumerate(library, 1):
        if book["is_available"]:
            status = "Available"
        else:
            status = "Borrowed"
        print(i, ".", book["title"], "|", book["author"], "|", status)

def borrow_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            if book["is_available"]:
                book["is_available"] = False
                print("You borrowed:", book["title"])
            else:
                print("Book already borrowed")
            return
    print("Book not found")

def return_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            book["is_available"] = True
            print("Book returned:", book["title"])
            return
    print("Book not found")

def remove_book(title):
    for i, book in enumerate(library):
        if book["title"].lower() == title.lower():
            library.pop(i)
            print("Book removed:", title)
            return
    print("Book not found")

def search_book(query):
    print("\nSearch Results:")
    found = False
    for book in library:
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            print(book["title"], "by", book["author"])
            found = True
    if not found:
        print("No books found")

while True:
    print("\n1 Add Book")
    print("2 Show Books")
    print("3 Borrow Book")
    print("4 Return Book")
    print("5 Remove Book")
    print("6 Search Book")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        add_book(title, author)

    elif choice == '2':
        show_all_books()

    elif choice == '3':
        title = input("Enter book name: ")
        borrow_book(title)

    elif choice == '4':
        title = input("Enter book name: ")
        return_book(title)

    elif choice == '5':
        title = input("Enter book name: ")
        remove_book(title)

    elif choice == '6':
        query = input("Enter search text: ")
        search_book(query)

    elif choice == '7':
        print("Thank you for visiting! Happy reading!")
        break

    else:
        print("Invalid choice")
