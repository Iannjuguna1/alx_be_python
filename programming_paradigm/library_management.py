# library_management.py

class Book:
    # A class representing a book with a title, author, and checked-out status

    def __init__(self, title, author):
        # Initialize title, author and mark book as available by default
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        # Mark the book as checked out
        self._is_checked_out = True

    def return_book(self):
        # Mark the book as returned (available)
        self._is_checked_out = False

    def is_available(self):
        # Return True if the book is not checked out
        return not self._is_checked_out


class Library:
    # A class representing a library that manages a collection of books

    def __init__(self):
        # Initialize an empty list to hold books
        self._books = []

    def add_book(self, book):
        # Add a book to the library collection
        self._books.append(book)

    def check_out_book(self, title):
        # Look for the book by title and check it out if available
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If the book is not available or not found, do nothing (as per spec)

    def return_book(self, title):
        # Look for the book by title and return it
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # If the book is not checked out or not found, do nothing

    def list_available_books(self):
        # Print all books that are currently available
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

