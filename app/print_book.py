from abc import ABC, abstractmethod

from app.book import Book


class AbstractPrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrintBook(AbstractPrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintBook(AbstractPrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
