from repos.LibRepos import LibRepos
from repos.BookRepos import BookRepos

from service.LibBookService import LibBookService
from service.LibService import LibService
from service.BookService import BookService

if __name__ == '__main__':
    while True:
        user_chose = int(input("1 - Добавить библиотеку\n2 - Добавить книгу\n3 - Просмотреть все книги\n4 - Просмотреть все библиотеки\n5 - Привязать книгу к библиотеке\n6 - Просмотреть книги в библиотеке\n7 - Редактировать книгу\n8 - Удалить книгу\n"))
        if user_chose == 0:
            break
        elif user_chose == 1:
            LibService.create_lib()
        elif user_chose == 2:
            BookService.create_book()
        elif user_chose == 3:
            all_books = BookRepos.get_books()
            for book in all_books:
                print(f"Идентификатор: {book.book_id} Наименование: {book.book_name} Автор: {book.book_author}")
        elif user_chose == 4:
            all_libs = LibRepos.get_libs()
            for lib in all_libs:
                print(f"Идентификатор: {lib.lib_id} Наименование: {lib.lib_name} Адрес: {lib.lib_address}")
        elif user_chose == 5:
            lib_id = int(input("Введите id библиотеки: "))
            book_id = int(input("Введите id книги: "))
            LibBookService.add_book_to_lib(lib_id, book_id)
        elif user_chose == 6:
            lib_id = int(input("Введите id библиотеки: "))
            lib_books = LibBookService.get_books_for_lib(lib_id)
            for book in lib_books.books:
                print(f"Идентификатор: {book.book_id} Наименование: {book.book_name} Автор: {book.book_author}")
        elif user_chose == 7:
            book_id = int(input("Введите id книги: "))
            book = BookService.update_book(book_id)
        elif user_chose == 8:
            book_id = int(input("Введите id книги: "))
            alert= input("Внимание! Книга будет удалена безвозвратно! Продолжить (д/н): ")
            if alert == "д":
                book = BookService.delete_book(book_id)