#!/usr/bin/python3
from classes.book import Book

class Library:
    def __init__(self, books: list):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to library.")

    def find_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
        print(f"Book named '{title}' was not found.")
        return Book(title='', author='', is_checked_out=True)
        # implies that no book was found ^

    def list_available_books(self):
        for book in self.books:
            if not book.is_checked_out:
                print(book.title)
