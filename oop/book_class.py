# book_class.py

class Book:
    # Constructor: initializes title, author, and year
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    # Destructor: prints a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # __str__: user-friendly string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # __repr__: developer-friendly, recreatable string
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

