# qa_python

1. test_add_empty_name_book - Проверка невозможности добавить книгу с пустым именем
2. test_add_duplicate_book - Проверка невозможности добавить дубликат книги
3. test_set_valid_genre - Проверка установки жанра для существующей книги
4. test_get_book_genre_book_without_genre - Проверка невозможности получения жанра от книги не содержащей жанр
5. test_get_books_with_specific_genre_existing_book - Проверка получения списка книг по определенному жанру
6. test_get_books_for_children_no_children_books - Проверка невозможности выборки книг, если рейтинг не для детей
7. test_get_books_for_children_with_children_books - Проверка получения списка книг подходящих детям
8. test_add_non_existing_book_to_favorites - Проверка невозможности добавления несуществующей книги в избранное
9. test_delete_book_from_favorites_existing_book - Проверка удаления из избранного существующей книги
10. test_get_list_of_favorites_books_empty_list - Проверка получения пустого списка избранных книг, если в нем нет книг
