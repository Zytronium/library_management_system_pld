#!/usr/bin/python3
from random import randint
from time import sleep
from classes.book import Book
from classes.library import Library
from classes.member import Member

book1 = Book("Book 1", "Rick Astley", False)
book2 = Book("Book 2", "Rick The Pickle", True)
book3 = Book("Book 3", "Jobama", True)
book4 = Book("Book 4", "Jack", True)
book5 = Book("Book 5", "You", False)

main_library = Library([book1, book2, book3, book4, book5])

# print(len(main_library.books))
# print(main_library.books[0].title)
# print(main_library.books[4].title)

person1 = Member("Alexander", [book4])
person2 = Member("Jake", [book3, book2])
person3 = Member("Megan", [])
person4 = Member("Joe", [])

all_members = [person1, person2, person3, person4]

for i in range(100):
    rand_member = all_members[randint(0, 3)]
    if randint(0, 1) == 0:
        if len(rand_member.borrowed_books) > 0:
            rand_member.return_book(rand_member.borrowed_books[randint(0, len(rand_member.borrowed_books) - 1)])
            sleep(0.5)
    elif len(main_library.find_available_books()) > 0:
        rand_member.borrow_book(main_library.find_available_books()[randint(0, len(main_library.find_available_books()) -1 )])
        sleep(0.5)



