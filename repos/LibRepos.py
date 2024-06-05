from models.LibModel import LibModel

class LibRepos:
    @staticmethod
    def get_libs():
        return LibModel.select().order_by(LibModel.lib_id)
