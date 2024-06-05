from models.BaseModel import BaseModel
from peewee import PrimaryKeyField, CharField

class LibModel(BaseModel):
    lib_id = PrimaryKeyField(primary_key=True, column_name="lib_id")
    lib_name = CharField(max_length=50, column_name="lib_name")
    lib_address = CharField(max_length=250, column_name="lib_address")

    class Meta:
        table_name = "lib"
