class Book:
    """
    A class to model a book, using magic methods for custom behavior.
    """
    def __init__(self, title: str, author: str, year: int):
        """Initializes the Book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Returns a human-readable string representation."""
        # Format: (title) by (author), published in (year)
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a string that can recreate the Book instance."""
        # Format: Book('title', 'author', year)
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Prints a message when the Book object is deleted."""
        # Format: Deleting (title of the book)
        print(f"Deleting {self.title}")