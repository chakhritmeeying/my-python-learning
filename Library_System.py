class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")


library = Library()
library.add_book(Book("ABC", "Pixels"))
library.add_book(Book("CBA", "Miyuki"))
library.display_books()
