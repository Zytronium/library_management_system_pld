#!/usr/bin/python3

from classes.book import Book

class Member:
    def __init__(self, name: str, borrowed_books:list):
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
        book.is_checked_out = True
        print(f"{self.name} borrowed book '{book.title}'")

    def return_book(self, book: Book):
        self.borrowed_books.remove(book)
        book.is_checked_out = False
        print(f"{self.name} returned book '{book.title}'")
