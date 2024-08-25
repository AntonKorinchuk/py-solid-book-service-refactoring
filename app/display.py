from abc import ABC, abstractmethod

from app.book import Book


class AbstractDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(AbstractDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(AbstractDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
