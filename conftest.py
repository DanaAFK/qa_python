import pytest

from main import BooksCollector

@pytest.fixture(autouse=True)
def class_object():
    return BooksCollector()
@pytest.fixture
def book_name():
    book_name = 'Ворота Расёмон'
    return book_name

@pytest.fixture
def genre():
    genre = 'Фантастика'
    return genre

@pytest.fixture
def add_book_with_genre(class_object, book_name, genre):
    class_object.add_new_book(book_name)
    class_object.set_book_genre(book_name, genre)

@pytest.fixture
def add_book_to_favorites(class_object, add_book_with_genre, book_name):
        class_object.add_book_in_favorites(book_name)










