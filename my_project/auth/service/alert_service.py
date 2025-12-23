from .general_service import GeneralService
from ..dao.Alert_dao import get_all_alerts, get_alert_by_id, create_alert, update_alert, delete_alert

class AlertService(GeneralService):
    def get_all(self):
        return get_all_alerts()

    def get_by_id(self, id):
        return get_alert_by_id(id)

    def create(self, data):
        return create_alert(data)

    def update(self, id, data):
        return update_alert(id, data)

    def delete(self, id):
        return delete_alert(id)
