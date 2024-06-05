from models.BaseModel import BaseModel
from peewee import PrimaryKeyField, CharField

class BookModel(BaseModel):
    book_id = PrimaryKeyField(primary_key=True, column_name="book_id")
    book_name = CharField(max_length=50, column_name="book_name")
    book_author = CharField(max_length=250, column_name="book_author")

    class Meta:
        table_name = "book"
