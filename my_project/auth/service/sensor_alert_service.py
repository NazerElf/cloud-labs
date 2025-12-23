from .general_service import GeneralService
# Note: insert_sensor_alert returns a dict, no standard CRUD object, so it's a bit specific.
# We inherit GeneralService but methods might raise NotImplementedError or be unused if not fit.
# Ideally GeneralService would be flexible or we just don't inherit it if it's too different.
# For consistency with other services, I'll inherit and leave unused methods as pass or not implemented.
from ..dao.SensorAlert_dao import insert_sensor_alert

class SensorAlertService(GeneralService):
    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def create(self, data):
        sensor_name = data.get('sensor_name')
        alert_description = data.get('alert_description')
        return insert_sensor_alert(sensor_name, alert_description)

    def update(self, id, data):
        pass

    def delete(self, id):
        pass
