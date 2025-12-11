# library_system.py

# --- Base Class: Book (Demonstrates the common attributes) ---
class Book:
    """Base class for all book types."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

# --- Derived Classes (Demonstrate Inheritance) ---

class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class (Book) constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the unique attribute
        self.file_size = file_size

    def __str__(self):
        """Custom string for listing EBooks."""
        return f"EBook: '{self.title}' by {self.author} ({self.file_size} KB)"

class PrintBook(Book):
    """Derived class for physical printed books."""
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class (Book) constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the unique attribute
        self.page_count = page_count

    def __str__(self):
        """Custom string for listing PrintBooks."""
        return f"PrintBook: '{self.title}' by {self.author} ({self.page_count} pages)"

# --- Composition Class: Library (Manages a collection of books) ---

class Library:
    """Manages a collection of various Book objects (Composition)."""
    def __init__(self):
        # Attribute 'books' is a list to store the instances. This is Composition.
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the collection."""
        self.books.append(book)
        print(f"Added: '{book.title}' to the library.")

    def list_books(self):
        """Prints the details of every book in the library."""
        print("\n--- Library Collection ---")
        if not self.books:
            print("The library is empty.")
            return
            
        for book in self.books:
            # We use the print() function, which automatically calls the __str__ 
            # method of the specific object (EBook, PrintBook, or base Book).
            print(book)
        print("--------------------------")