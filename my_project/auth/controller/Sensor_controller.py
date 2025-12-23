from flask import request
from ..service.sensor_service import SensorService

sensor_service = SensorService()

# Отримати всі сенсори
def get_sensors():
    sensors = sensor_service.get_all()
    sensors_data = [
        {
            'id': sensor.idSensor,
            'sensor_type': sensor.sensor_type,
            'installation_date': str(sensor.installation_date),
            'status': sensor.status,
            'last_maintenance': str(sensor.last_maintenance),
            'location_id': sensor.Locations_idLocation
        } for sensor in sensors
    ]
    return sensors_data, 200

# Отримати сенсор за ID
def get_sensor(id):
    sensor = sensor_service.get_by_id(id)
    if sensor:
        sensor_data = {
            'id': sensor.idSensor,
            'sensor_type': sensor.sensor_type,
            'installation_date': str(sensor.installation_date),
            'status': sensor.status,
            'last_maintenance': str(sensor.last_maintenance),
            'location_id': sensor.Locations_idLocation
        }
        return sensor_data, 200
    return {'error': 'Sensor not found'}, 404

# Створити сенсор
def create_sensor_route():
    data = request.get_json()
    new_sensor = sensor_service.create(data)
    # Return dict, conversion to json handled by framework
    return {'message': 'Sensor created successfully', 'sensor_id': new_sensor.idSensor}, 201

# Оновити сенсор
def update_sensor_route(id):
    data = request.get_json()
    sensor = sensor_service.update(id, data)
    if sensor:
        return {'message': 'Sensor updated successfully'}, 200
    return {'error': 'Sensor not found'}, 404

# Видалити сенсор
def delete_sensor_route(id):
    # Depending on DAO implementation, delete might return None or raise exception
    # Service wrapper should simplify this used here.
    # Looking at DAO, delete_sensor returns None.
    # Let's assume service.delete calls dao.delete
    # Wait, previous DAO delete_sensor(id) didn't return success boolean, it just did it.
    # Let's look at Sensor_dao again.
    # def delete_sensor(sensor_id): ... if sensor: db.session.delete...
    # It doesn't return anything.
    # We should probably update Service to return boolean or Controller to handle it.
    
    # Original controller code:
    # sensor = get_sensor_by_id(id)
    # if not sensor: return error
    # try: delete_sensor(id) ...
    
    # Let's keep logic in controller for now but use service for fetch and delete
    sensor = sensor_service.get_by_id(id)
    if not sensor:
        return {'error': 'Sensor not found'}, 404

    try:
        sensor_service.delete(id)
        return {'message': 'Sensor deleted successfully'}, 200
    except Exception as e:
        return {'error': 'Failed to delete sensor', 'details': str(e)}, 500

# Вставка сенсора через SQL
def insert_sensor_route():
    # Helper for procedure call, might not be in generic service
    # We can add specific method to SensorService or keep DAO import for this specific one
    # ideally move to service.
    from ..dao.Sensor_dao import insert_sensor
    # Temporarily import DAO here or add to service. Let's add to service later if needed.
    # For now, keep it as is or move to service. 
    # Let's stick to cleaning up main CRUD.
    
    data = request.get_json()

    if not all(key in data for key in ("sensor_type", "installation_date", "status", "last_maintenance", "Locations_idLocation")):
        return {"error": "Missing parameters"}, 400

    sensor_type = data['sensor_type']
    installation_date = data['installation_date']
    status = data['status']
    last_maintenance = data['last_maintenance']
    Locations_idLocation = data['Locations_idLocation']

    try:
        insert_sensor(sensor_type, installation_date, status, last_maintenance, Locations_idLocation)
        return {"message": "Sensor inserted successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
