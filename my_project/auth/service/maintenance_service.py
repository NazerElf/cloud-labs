from .general_service import GeneralService
from ..dao.Maintenance_dao import get_all_maintenance, get_maintenance_by_id, create_maintenance, update_maintenance, delete_maintenance

class MaintenanceService(GeneralService):
    def get_all(self):
        return get_all_maintenance()

    def get_by_id(self, id):
        return get_maintenance_by_id(id)

    def create(self, data):
        return create_maintenance(data)

    def update(self, id, data):
        return update_maintenance(id, data)

    def delete(self, id):
        return delete_maintenance(id)
