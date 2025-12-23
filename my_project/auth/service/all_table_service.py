from .general_service import GeneralService
from ..dao.AllTable_dao import calculate_stat, split_table

class AllTableService(GeneralService):
    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass

    def calculate_statistics(self, col_name, table_name, operation):
        return calculate_stat(col_name, table_name, operation)

    def split_tables(self):
        return split_table()
