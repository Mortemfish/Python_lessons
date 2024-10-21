import pickle

# Класс, представляющий книгу
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.genre}"

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
            raise ValueError(f"Book '{book.title}' not borrowed by {self.name}")

    def __str__(self):
        return f"{self.name} (ID: {self.reader_id}), Borrowed books: {[str(book) for book in self.borrowed_books]}"

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
            raise ValueError(f"Book '{book.title}' not found in the library")

    def register_reader(self, reader):
        self.readers.append(reader)

    def lend_book(self, reader, book):
        if book in self.books:
            reader.borrow_book(book)
            self.books.remove(book)
        else:
            raise ValueError(f"Book '{book.title}' is not available")

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
    # Создаем библиотеку
    library = Library("City Library")

    # Добавляем книги
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    book2 = Book("1984", "George Orwell", 1949, "Dystopian")
    library.add_book(book1)
    library.add_book(book2)

    # Регистрируем читателя
    reader1 = Reader("Alice", 1)
    library.register_reader(reader1)

    # Выдаем книгу
    print(f"Lending '{book1.title}' to {reader1.name}")
    library.lend_book(reader1, book1)

    # Проверяем взятые книги читателя
    print("Books borrowed by reader1:", library.get_reader_books(reader1))

    # Возвращаем книгу
    print(f"Returning '{book1.title}' from {reader1.name}")
    library.return_book(reader1, book1)

    # Поиск книги по автору
    found_books = library.find_book(author="George Orwell")
    print("Found books by George Orwell:")
    for book in found_books:
        print(book)

    # Сохранение состояния
    print("Saving library state to 'library_state.pkl'")
    library.save_state("library_state.pkl")

    # Загрузка состояния
    print("Loading library state from 'library_state.pkl'")
    library = Library.load_state("library_state.pkl")

    # Проверка загрузки состояния
    print("Books in the library after loading:")
    for book in library.books:
        print(book)

    print("Registered readers:")
    for reader in library.readers:
        print(reader)
