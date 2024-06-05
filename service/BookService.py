from models.BookModel import BookModel

class BookService:

    @staticmethod
    def create_book():
        book_name = input("Введите наименование книги\n")
        book_author = input("Введите автора книги\n")

        book = BookModel().create(book_name=book_name, book_author=book_author)
        return book

    @staticmethod
    def update_book(book_id):
        book = BookModel.select().where(BookModel.book_id == book_id).get()

        new_name = input(f"Введите новое имя книги (Enter - оставить старое {book.book_name}): ")
        if new_name != "":
            book.book_name = new_name

        new_author = input(f"Введите новое имя автора (Enter - оставить старое {book.book_author}): ")
        if new_author != "":
            book.book_author = new_author

        book.save()

    @staticmethod
    def delete_book(book_id):
        book = BookModel.select().where(BookModel.book_id == book_id).get()
        book.delete_instance()
