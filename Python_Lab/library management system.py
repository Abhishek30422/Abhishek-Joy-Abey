
# Library Management System using OOP

class Library:

    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        }

        self.books.append(book)
        print("Book added successfully!")

    # View all books
    def view_books(self):
        if len(self.books) == 0:
            print("No books available!")

        else:
            print("\n===== BOOK LIST =====")

            for book in self.books:
                print("Book ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])

                if book["available"]:
                    print("Status: Available")
                else:
                    print("Status: Borrowed")

                print("-------------------")

    # Search for a book
    def search_book(self):
        book_id = input("Enter Book ID to search: ")

        for book in self.books:
            if book["id"] == book_id:
                print("\nBook Found!")
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Available:", book["available"])
                return

        print("Book not found!")

    # Borrow a book
    def borrow_book(self):
        book_id = input("Enter Book ID to borrow: ")

        for book in self.books:
            if book["id"] == book_id:

                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed!")

                return

        print("Book not found!")

    # Return a book
    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book["id"] == book_id:

                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed!")

                return

        print("Book not found!")


# Create library object
library = Library()

# Main menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        print("Thank you for using the library!")
        break

    else:
        print("Invalid choice! Please try again.")
