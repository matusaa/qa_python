import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_empty_name_book(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_add_duplicate_book(self, collector):
        collector.add_new_book('Маска')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("genre", ["Комедии", "Фантастика", "Детективы"])
    def test_set_valid_genre(self, collector, genre):
        collector.set_book_genre('Маска', genre)
        assert collector.get_book_genre('Маска') == genre

    def test_get_book_genre_book_without_genre(self, collector):
        assert collector.get_book_genre('Маска') == ''

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Звездные войны"]),
        ("Ужасы", ["Пила-6"]),
        ("Детективы", [])
    ])
    def test_get_books_with_specific_genre_existing_book(self, collector_withs_genres, genre, expected_books):
        assert collector_withs_genres.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_for_children_no_children_books(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Пила-6': 'Ужасы',
            'Шерлок Холмс': 'Детективы',
        }
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_children_books(self, collector_withs_genres):
        assert collector_withs_genres.get_books_for_children() == ['Звездные войны']

    def test_add_non_existing_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.favorites

    @pytest.mark.parametrize("book_to_delete, expected_favorites", [
        ("Звездные войны", ["Пила-6"]),
        ("Пила-6", ["Звездные войны"]),
    ])
    def test_delete_book_from_favorites_existing_book(self, collector_withs_genres, book_to_delete, expected_favorites):
        collector_withs_genres.add_book_in_favorites('Звездные войны')
        collector_withs_genres.add_book_in_favorites('Пила-6')
        collector_withs_genres.delete_book_from_favorites(book_to_delete)
        assert collector_withs_genres.favorites == expected_favorites

    def test_get_list_of_favorites_books_empty_list(self, collector_withs_genres):
        assert collector_withs_genres.get_list_of_favorites_books() == []
