from .general_service import GeneralService
from ..dao.Measurement_dao import get_all_measurements, get_measurement_by_id, create_measurement, update_measurement, delete_measurement

class MeasurementService(GeneralService):
    def get_all(self):
        return get_all_measurements()

    def get_by_id(self, id):
        return get_measurement_by_id(id)

    def create(self, data):
        return create_measurement(data)

    def update(self, id, data):
        return update_measurement(id, data)

    def delete(self, id):
        return delete_measurement(id)
