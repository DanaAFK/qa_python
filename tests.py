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
        assert len(collector.get_books_rating()) == 2

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.collector = BooksCollector()

    @pytest.mark.parametrize("book_name", ['Расёмон', 'о' * 40 ])
    def test_add_new_book_valid_book_name_true(self,book_name):
        self.collector.add_new_book(book_name)

        assert book_name in self.collector.get_books_genre() and self.collector.get_books_genre()[book_name] == ''






