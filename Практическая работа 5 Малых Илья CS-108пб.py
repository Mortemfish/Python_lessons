import pickle

# Классы Book, Reader и Library остаются без изменений

if __name__ == "__main__":
    # Создаем библиотеку
    library = Library("City Library")

    # Добавляем книги
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    book2 = Book("1984", "George Orwell", 1949, "Dystopian")
    library.add_book(book1)
    library.add_book(book2)

    # Регистрируем читателя
    reader_name = input("Введите имя читателя: ")
    reader_id = int(input("Введите ID читателя: "))
    reader1 = Reader(reader_name, reader_id)
    library.register_reader(reader1)

    while True:
        print("\n1. Выдать книгу")
        print("2. Вернуть книгу")
        print("3. Найти книгу")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги для выдачи: ")
            found_books = library.find_book(title=title)
            if found_books:
                print(f"Книги, найденные по запросу '{title}':")
                for book in found_books:
                    print(book)
                book_to_lend = found_books[0]
                library.lend_book(reader1, book_to_lend)
                print(f"Книга '{book_to_lend.title}' выдана читателю {reader1.name}")
            else:
                print("Книга не найдена.")
        
        elif choice == "2":
            title = input("Введите название книги для возврата: ")
            found_books = library.get_reader_books(reader1)
            book_to_return = None
            for book in found_books:
                if book.title.lower() == title.lower():
                    book_to_return = book
                    break
            if book_to_return:
                library.return_book(reader1, book_to_return)
                print(f"Книга '{book_to_return.title}' возвращена читателем {reader1.name}")
            else:
                print(f"У читателя {reader1.name} нет такой книги.")
        
        elif choice == "3":
            title = input("Введите название книги для поиска: ")
            found_books = library.find_book(title=title)
            if found_books:
                print(f"Найденные книги по запросу '{title}':")
                for book in found_books:
                    print(book)
            else:
                print("Книги не найдены.")

        elif choice == "4":
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")
