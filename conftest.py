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







