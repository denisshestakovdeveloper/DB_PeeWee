from models.LibModel import LibModel
from models.LibBookModel import LibBookModel
from models.BookModel import BookModel
from DTO.LibBookDTO import LibBookDTO

class LibBookService:
    @staticmethod
    def add_book_to_lib(lib_id, book_id):
        lib_model = LibModel.select().where(LibModel.lib_id == lib_id).get()
        book_model = BookModel.select().where(BookModel.book_id == book_id).get()
        lib_book = LibBookModel().create(lib_id=lib_model, book_id=book_model)
        return lib_book

    @staticmethod
    def get_books_for_lib(lib_id):
        lib_model = LibModel().select().where(LibModel.lib_id == lib_id).get()
        lib_book_dto = LibBookDTO(lib_model)
        lib_books = LibBookModel.select().where(LibBookModel.lib_id == lib_id)
        for lib_book in lib_books:
            lib_book_dto.add_book(lib_book.book_id)
        return lib_book_dto
