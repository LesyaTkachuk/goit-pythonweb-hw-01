from abc import ABC, abstractmethod
from typing import List
from log import logger


# Single-Responsibility Principle
# class Book has to do only one thing - to store information about a book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Interface Segregation Principle
# class LibraryInterface define interface method that should be implemented by Library class


# Liskov Substitution Principle
# any class that is a subclass of LibraryInterface can be used instead of Library class
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title, author, year):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass


# Open-Closed Principle
# class Library could be extended without changing the existing code
class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            logger.info(book)


# Dependency Inversion Principle
# class LibraryManager depends on Library class(an abstraction)
class LibraryManager:
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(title, author, year)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
