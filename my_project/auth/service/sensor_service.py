from .general_service import GeneralService
from ..dao.Sensor_dao import get_all_sensors, get_sensor_by_id, create_sensor, update_sensor, delete_sensor

class SensorService(GeneralService):
    def get_all(self):
        return get_all_sensors()

    def get_by_id(self, id):
        return get_sensor_by_id(id)

    def create(self, data):
        return create_sensor(data)

    def update(self, id, data):
        return update_sensor(id, data)

    def delete(self, id):
        return delete_sensor(id)
