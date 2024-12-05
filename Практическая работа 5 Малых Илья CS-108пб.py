import pickle

# Класс, представляющий книгу
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' автор: {self.author} ({self.year}) - Жанр: {self.genre}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# Класс, представляющий читателя
class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            raise ValueError(f"Книга '{book.title}' не была взята {self.name}")

    def __str__(self):
        return f"{self.name} (ID: {self.reader_id}), Взятые книги: {[str(book) for book in self.borrowed_books]}"

# Класс, представляющий библиотеку
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError(f"Книга '{book.title}' не найдена в библиотеке")

    def register_reader(self, reader):
        self.readers.append(reader)

    def lend_book(self, reader, book):
        if book in self.books:
            reader.borrow_book(book)
            self.books.remove(book)
        else:
            raise ValueError(f"Книга '{book.title}' не доступна")

    def return_book(self, reader, book):
        reader.return_book(book)
        self.books.append(book)

    def find_book(self, title=None, author=None):
        found_books = [
            book for book in self.books
            if (title is None or book.title.lower() == title.lower()) and
            (author is None or book.author.lower() == author.lower())
        ]
        return found_books

    def get_reader_books(self, reader):
        return reader.borrowed_books

    def save_state(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_state(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Пример использования библиотеки
if __name__ == "__main__":
    # Создание библиотеки
    library = Library("Городская Библиотека")

    # Добавляем книги
    book1 = Book("Великий Гэтсби", "Фрэнсис Скотт Фицджеральд", 1925, "Роман")
    book2 = Book("1984", "Джордж Оруэлл", 1949, "Антиутопия")
    library.add_book(book1)
    library.add_book(book2)

    # Регистрируем читателя
    reader1 = Reader("Алиса", 1)
    library.register_reader(reader1)

    # Логика взаимодействия с библиотекой
    print(f"Книги в библиотеке: {[str(book) for book in library.books]}")

    # Читатель берет книгу
    library.lend_book(reader1, book1)
    print(f"Книги, взятые {reader1.name}: {[str(book) for book in reader1.borrowed_books]}")

    # Читатель возвращает книгу
    library.return_book(reader1, book1)
    print(f"Книги в библиотеке после возврата: {[str(book) for book in library.books]}")
    print(f"Книги, взятые {reader1.name} после возврата: {[str(book) for book in reader1.borrowed_books]}")
    
    # Сохранение состояния библиотеки
    library.save_state('library_state.pkl')
    print("Состояние библиотеки сохранено.")
    
    # Загрузка состояния библиотеки
    loaded_library = Library.load_state('library_state.pkl')
    print("Состояние библиотеки загружено.")
    print(f"Книги в загруженной библиотеке: {[str(book) for book in loaded_library.books]}")
