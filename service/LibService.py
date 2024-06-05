from models.LibModel import LibModel

class LibService:

    @staticmethod
    def create_lib():
        lib_name = input("Введите наименование библиотеки\n")
        lib_address = input("Введите адрес библиотеки\n")

        lib = LibModel().create(lib_name=lib_name, lib_address=lib_address)
        return lib
