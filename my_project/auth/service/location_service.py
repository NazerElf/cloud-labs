from .general_service import GeneralService
from ..dao.Location_dao import get_all_locations, get_location_by_id, create_location, update_location, delete_location, get_sensors_for_location, insert_location

class LocationService(GeneralService):
    def get_all(self):
        return get_all_locations()

    def get_by_id(self, id):
        return get_location_by_id(id)

    def create(self, data):
        return create_location(data)

    def update(self, id, data):
        return update_location(id, data)

    def delete(self, id):
        return delete_location(id)
    
    def get_sensors(self, id):
        return get_sensors_for_location(id)

    def insert(self, name, latitude, longitude, region):
        return insert_location(name, latitude, longitude, region)
