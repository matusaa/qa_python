Тестирование BooksCollector

Проверка метода add_new_book
1. test_add_empty_name_book - Проверка невозможности добавить книгу с пустым именем

Проверка метода add_new_book и get_books_genre
2. test_add_duplicate_book - Проверка невозможности добавить дубликат книги

Проверка метода set_book_genre
3. test_set_valid_genre - Проверка установки жанра для существующей книги

Проверка метода get_book_genre
4. test_get_book_genre_book_without_genre - Проверка невозможности получения жанра от книги не содержащей жанр

Проверка метода get_books_with_specific_genre
5. test_get_books_with_specific_genre_existing_book - Проверка получения списка книг по определенному жанру

Проверка метода get_books_for_children
6. test_get_books_for_children_no_children_books - Проверка невозможности выборки книг, если рейтингне для детей
7. test_get_books_for_children_with_children_books - Проверка получения списка книг подходящих детям

Проверка метода add_book_in_favorites
8. test_add_non_existing_book_to_favorites - Проверка невозможности добавления несуществующей книги в избранное

Проверка метода delete_book_from_favorites
9. test_delete_book_from_favorites_existing_book - Проверка удаления из избранного существующей книги

Проверка метода get_list_of_favorites_books
10. test_get_list_of_favorites_books_empty_list - Проверка получения пустого списка избранных книг, если в нем нет книг
