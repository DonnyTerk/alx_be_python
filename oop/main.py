from library_system import Book, EBook, PrintBook, Library

library = Library()

b1 = Book("Pride and Prejudice", "Jane Austen")
b2 = EBook("Snow Crash", "Neal Stephenson", 500)
b3 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.list_books()
