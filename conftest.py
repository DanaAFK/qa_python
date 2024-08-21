import pytest
@pytest.fixture
def book_name(self):
    book_name = 'Ворота Расёмон'
    return book_name

@pytest.fixture
def genre(self):
    genre = 'Фантастика'
    return genre

@pytest.fixture
def add_book_with_genre(self, book_name, genre):
    self.collector.add_new_book(book_name)
    self.collector.set_book_genre(book_name, genre)

@pytest.fixture
def add_book_to_favorites(self, add_book_with_genre, book_name):
        self.collector.add_book_in_favorites(book_name)







