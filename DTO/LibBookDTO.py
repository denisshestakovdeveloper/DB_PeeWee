class LibBookDTO:
    def __init__(self, lib_model):
        self.lib_model = lib_model
        self.books = []

    def add_book(self, book):
        self.books.append(book)

