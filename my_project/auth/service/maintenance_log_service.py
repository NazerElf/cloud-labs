from .general_service import GeneralService
from ..dao.MaintenanceLog_dao import get_all_maintenance_logs, get_maintenance_log_by_id, create_maintenance_log, update_maintenance_log, delete_maintenance_log

class MaintenanceLogService(GeneralService):
    def get_all(self):
        return get_all_maintenance_logs()

    def get_by_id(self, id):
        return get_maintenance_log_by_id(id)

    def create(self, data):
        return create_maintenance_log(data)

    def update(self, id, data):
        return update_maintenance_log(id, data)

    def delete(self, id):
        return delete_maintenance_log(id)
