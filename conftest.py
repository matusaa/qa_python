import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    book = BooksCollector()
    book.add_new_book('Маска')
    return book

@pytest.fixture
def collector_withs_genres():
    book = BooksCollector()
    book.add_new_book('Звездные войны')
    book.add_new_book('Пила-6')
    book.set_book_genre('Звездные войны','Фантастика')
    book.set_book_genre('Пила-6','Ужасы')
    return book