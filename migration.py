from models.BookModel import BookModel
from models.LibModel import LibModel
from models.LibBookModel import LibBookModel

def apply():
    LibModel.create_table()
    BookModel.create_table()
    LibBookModel.create_table()

if __name__ == '__main__':
    apply()
