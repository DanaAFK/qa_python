# qa_python
Описание тестов для методов класса BooksCollector:
1. Метод add_new_book:

test_add_new_book_existing_book_not_add:
Проверяет, что книгу, уже существующую в словаре books_genre, невозможно добавить повторно.
test_add_new_book_invalid_book_name_not_add:
Используя параметризацию, проверяет, что книга с невалидным именем (пустое имя или имя длиннее 40 символов) не может быть добавлена в словарь books_genre.
test_add_new_book_success:
Проверяет успешное добавление книги с валидным именем в словарь books_genre.
2. Метод set_book_genre:

test_set_book_genre_success:
Проверяет, что книга успешно получает жанр, если она существует в словаре books_genre, и жанр является валидным.
test_set_book_genre_invalid_genre:
Проверяет, что невозможно установить невалидный жанр (жанр, отсутствующий в списке genre) для книги.
test_set_book_genre_non_existing_book:
Проверяет, что невозможно установить жанр для книги, которой нет в словаре books_genre.
3. Метод get_book_genre:

test_get_book_genre_success:
Проверяет, что метод корректно возвращает жанр для книги, если жанр установлен.
test_get_book_genre_no_genre:
Проверяет, что метод возвращает None или пустое значение, если для книги жанр не установлен.
test_get_book_genre_non_existing_book:
Проверяет, что метод возвращает None или пустое значение, если книга отсутствует в словаре books_genre.
4. Метод get_books_with_specific_genre:

test_get_books_with_specific_genre_success:
Проверяет, что метод возвращает корректный список книг для указанного жанра.
test_get_books_with_specific_genre_no_books:
Проверяет, что метод возвращает пустой список, если нет книг с указанным жанром.
test_get_books_with_specific_genre_invalid_genre:
Проверяет, что метод возвращает пустой список или None, если жанр не валидный (не входит в список genre).
5. Метод get_books_genre:

test_get_books_genre_empty:
Проверяет, что метод возвращает пустой словарь, если книги не были добавлены.
test_get_books_genre_one_book:
Проверяет, что метод возвращает словарь с одной книгой и соответствующим жанром.
test_get_books_genre_multiple_books:
Проверяет, что метод возвращает словарь с несколькими книгами и их жанрами.
6. Метод get_books_for_children:

test_get_books_for_children_no_books:
Проверяет, что метод возвращает пустой список, если нет книг, подходящих для детей.
test_get_books_for_children_with_books:
Проверяет, что метод возвращает список книг, которые подходят для детей (без возрастного ограничения).
test_get_books_for_children_with_restricted_books:
Проверяет, что метод не включает книги с жанрами, имеющими возрастное ограничение, в список детских книг.
7. Метод add_book_in_favorites:

test_add_book_in_favorites_success:
Проверяет успешное добавление книги в избранное.
test_add_book_in_favorites_twice:
Проверяет, что одну и ту же книгу нельзя добавить в избранное дважды.
test_add_book_in_favorites_non_existing_book:
Проверяет, что невозможно добавить в избранное книгу, которая отсутствует в словаре books_genre.
8. Метод delete_book_from_favorites:

test_delete_book_from_favorites_success:
Проверяет успешное удаление книги из избранного.
test_delete_book_from_favorites_not_in_favorites:
Проверяет, что удаление книги, не находящейся в избранном, не вызывает ошибок и не изменяет список избранного.
test_delete_book_from_favorites_non_existing_book:
Проверяет, что попытка удаления несуществующей книги (которая отсутствует в словаре books_genre) не вызывает ошибок и не изменяет список избранного.
9. Метод get_list_of_favorites_books:

test_get_list_of_favorites_books_empty:
Проверяет, что метод возвращает пустой список, если в избранное не добавлено ни одной книги.
test_get_list_of_favorites_books_one_book:
Проверяет, что метод возвращает список с одной книгой, если только она была добавлена в избранное.
test_get_list_of_favorites_books_multiple_books:
Проверяет, что метод возвращает список с несколькими книгами, если они были добавлены в избранное.
