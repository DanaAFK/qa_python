import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def class_object(self):
        collector = BooksCollector()
        return collector

    def test_add_new_book_add_two_books(self, class_object):
        class_object.add_new_book('Гордость и предубеждение и зомби')
        class_object.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(class_object.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", ['1984', 'о' * 40 ])
    def test_add_new_book_valid_book_name_add(self, class_object, book_name):
        class_object.add_new_book(book_name)

        assert book_name in class_object.get_books_genre() and class_object.get_books_genre()[book_name] == ''

    def test_add_new_book_existing_book_not_add(self, class_object, book_name):
        class_object.add_new_book(book_name)
        class_object.add_new_book(book_name)

        assert len(class_object.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name",['','o' * 41])
    def test_add_new_book_invalid_book_name_not_add(self, class_object, book_name):
        class_object.add_new_book(book_name)

        assert len(class_object.get_books_genre()) == 0 and book_name not in class_object.get_books_genre()

    def test_set_book_genre_existing_book_set_genre(self, class_object, book_name,genre):
        class_object.add_new_book(book_name)
        class_object.set_book_genre(book_name, genre)

        assert class_object.get_book_genre(book_name) == genre

    def test_set_book_genre_non_existent_book_no_genre(self, class_object, book_name,genre):
        class_object.set_book_genre(book_name, genre)

        assert book_name not in class_object.get_books_genre()

    @pytest.mark.parametrize("invalid_genre", ['Триллер', 'Кино'])
    def test_set_book_genre_invalid_gener_false(self, class_object, invalid_genre):
        book_name = 'Звонок'
        class_object.add_new_book(book_name)

        class_object.set_book_genre(book_name,invalid_genre)

        assert class_object.get_book_genre(book_name) == ''

    def test_get_book_genre_existing_book_with_genre_get_genre(self, class_object, book_name, genre):

        class_object.add_new_book(book_name)
        class_object.set_book_genre(book_name, genre)
        class_object.get_book_genre(book_name)

        assert class_object.get_book_genre(book_name) == genre

    def test_get_book_genre_existing_book_without_genre_get_empty_string(self, class_object, book_name):

        class_object.add_new_book(book_name)
        class_object.get_book_genre(book_name)

        assert class_object.get_book_genre(book_name) == ''

    def test_get_book_genre_non_existent_book_is_none(self, class_object):
        book_name = 'Азазель'

        class_object.get_book_genre(book_name)

        assert class_object.get_book_genre(book_name) is None

    def test_get_books_with_specific_genre_get_list_books_for_specific_genre(self, class_object, add_book_with_genre, book_name, genre):
        class_object.get_books_with_specific_genre(genre)

        assert class_object.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_with_specific_genre_without_book_get_empty_list(self, class_object, genre):
        class_object.get_books_with_specific_genre(genre)

        assert class_object.get_books_with_specific_genre(genre) == []

    def test_get_books_with_specific_genre_invalid_genre_get_empty_list(self, class_object, add_book_with_genre, book_name, genre):
        invalid_genre = 'non-fiction'
        class_object.get_books_with_specific_genre(invalid_genre)

        assert class_object.get_books_with_specific_genre(invalid_genre) == []

    def test_get_books_with_specific_genre_book_match_genre(self, class_object, add_book_with_genre, book_name, genre):
        another_book = 'Руководство по сборке ВАЗ 2017'
        another_genre = 'Ужасы'

        class_object.add_new_book(another_book)
        class_object.set_book_genre(another_book,another_genre)

        class_object.get_books_with_specific_genre(genre)
        class_object.get_books_with_specific_genre(another_genre)

        assert class_object.get_books_with_specific_genre(genre) == [book_name] and class_object.get_books_with_specific_genre(another_genre) ==[another_book]

    def test_get_books_genre_dictionary_empty_get_empty(self, class_object):
        class_object.get_books_genre()

        assert class_object.get_books_genre() == {}

    def test_get_books_genre_dictionary_with_one_book_get_this_book(self, class_object, add_book_with_genre, book_name, genre):
        class_object.get_books_genre()

        assert class_object.get_books_genre() == {book_name: genre}

    def test_get_books_genre_dictionary_with_several_books_get_this_books(self, class_object, add_book_with_genre, book_name, genre):
        another_book = 'Руководство по сборке ВАЗ 2017'
        another_genre = 'Ужасы'
        class_object.add_new_book(another_book)
        class_object.set_book_genre(another_book,another_genre)

        class_object.get_books_genre()
        expected_books_genre = {
            book_name: genre,
            another_book: another_genre
        }
        assert class_object.get_books_genre() == expected_books_genre

    def test_get_books_for_children_no_books_get_empty_list(self, class_object):
        class_object.get_books_for_children()
        assert class_object.get_books_for_children() == []

    def test_get_books_for_children_possible_book_get_book_list(self, class_object, add_book_with_genre, book_name):
        class_object.get_books_for_children()
        assert class_object.get_books_for_children() == [book_name]

    def test_get_books_for_children_possible_and_limited_books_get_list_possible_books(self, class_object, add_book_with_genre, genre, book_name):
        another_book = 'Руководство по сборке ВАЗ 2017'
        another_genre = 'Ужасы'
        class_object.add_new_book(another_book)
        class_object.set_book_genre(another_book, another_genre)

        class_object.get_books_for_children()

        assert class_object.get_books_for_children() == [book_name]

    def test_get_books_for_children_limited_book_get_empty_list(self, class_object):
        another_book = 'Руководство по сборке ВАЗ 2017'
        another_genre = 'Ужасы'
        class_object.add_new_book(another_book)
        class_object.set_book_genre(another_book, another_genre)

        class_object.get_books_for_children()

        assert class_object.get_books_for_children() == []

    def test_add_book_in_favorites_registered_book_add_favorites_list(self, class_object, add_book_with_genre, book_name):
        class_object.add_book_in_favorites(book_name)
        favorites_list = class_object.get_list_of_favorites_books()
        assert book_name in favorites_list

    def test_add_book_in_favorites_favorite_book_not_add_again_list(self, class_object, add_book_with_genre, book_name):
        class_object.add_book_in_favorites(book_name)
        class_object.add_book_in_favorites(book_name)

        favorites_list = class_object.get_list_of_favorites_books()

        assert favorites_list.count(book_name) == 1

    def test_add_book_in_favorites_non_existing_book_not_in_favorites(self, class_object, book_name):
        class_object.add_book_in_favorites(book_name)
        favorites_list = class_object.get_list_of_favorites_books()

        assert book_name not in favorites_list

    def test_delete_book_from_favorites_book_delete_success(self, class_object, add_book_with_genre, add_book_to_favorites, book_name):
        class_object.delete_book_from_favorites(book_name)
        favorites_list = class_object.get_list_of_favorites_books()

        assert book_name not in favorites_list

    def test_delete_book_from_favorites_not_in_favorites_not_delete(self, class_object, add_book_with_genre, book_name):
        class_object.delete_book_from_favorites(book_name)
        favorites_list = class_object.get_list_of_favorites_books()

        assert book_name not in favorites_list

    def test_delete_book_from_favorites_non_existing_book_not_delete(self, class_object):
        another_book = 'Руководство по сборке ВАЗ 2017'
        class_object.delete_book_from_favorites(another_book)
        favorites_list = class_object.get_list_of_favorites_books()

        assert another_book not in favorites_list

    def test_get_list_of_favorites_books_all_books_in_list(self, class_object, add_book_with_genre, add_book_to_favorites, book_name):
        another_book = 'Руководство по сборке ВАЗ 2017'
        another_genre = 'Ужасы'
        class_object.add_new_book(another_book)
        class_object.set_book_genre(another_book, another_genre)

        class_object.add_book_in_favorites(another_book)

        favorites_list = class_object.get_list_of_favorites_books()

        assert favorites_list == [book_name, another_book]



























