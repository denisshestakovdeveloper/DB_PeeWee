from models.BaseModel import BaseModel
from models.LibModel import LibModel
from models.BookModel import BookModel
from peewee import PrimaryKeyField, ForeignKeyField

class LibBookModel(BaseModel):
    lib_book_id = PrimaryKeyField(primary_key=True, column_name="lib_book_id")
    book_id = ForeignKeyField(BookModel, column_name="book_id")
    lib_id = ForeignKeyField(LibModel, column_name="lib_id")

    class Meta:
        table_name = "lib_book"



