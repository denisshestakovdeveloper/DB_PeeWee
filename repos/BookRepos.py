from models.BookModel import BookModel

class BookRepos:
    @staticmethod
    def get_books():
        return BookModel.select().order_by(BookModel.book_id)
