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
    def test_add_new_book_valid_book_name_add(self,book_name):
        self.collector.add_new_book(book_name)

        assert book_name in self.collector.get_books_genre() and self.collector.get_books_genre()[book_name] == ''

    def test_add_new_book_existing_book_not_add(self):
        self.collector.add_new_book('1984')
        self.collector.add_new_book('1984')

        assert len(self.collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name",['','o' * 41])
    def test_add_new_book_invalid_book_name_not_add(self,book_name):
        self.collector.add_new_book(book_name)

        assert len(self.collector.get_books_genre()) == 0 and book_name not in self.collector.get_books_genre()



    def test_set_book_genre_existing_book_set_genre(self):
        book_name = 'Руководство по ремонту ВАЗ 2017'
        self.collector.add_new_book(book_name)

        genre = 'Фантастика'
        self.collector.set_book_genre(book_name, genre)

        assert self.collector.get_book_genre(book_name) == genre

    def test_set_book_genre_non_existent_book_no_genre(self):
        book_name = 'Новая книга'
        genre = 'Фантастика'

        self.collector.set_book_genre(book_name, genre)

        assert book_name not in self.collector.get_books_genre()

    @pytest.mark.parametrize("invalid_genre", ['Триллер', 'Кино'])
    def test_set_book_genre_invalid_gener_false(self,invalid_genre):
        book_name = 'Звонок'
        self.collector.add_new_book(book_name)

        self.collector.set_book_genre(book_name,invalid_genre)

        assert self.collector.get_book_genre(book_name) == ''



