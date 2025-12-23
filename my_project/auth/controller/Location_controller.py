from flask import request
from models import db, Location
from ..service.location_service import LocationService
from sqlalchemy import text

location_service = LocationService()

def get_locations():
    locations = location_service.get_all()
    locations_data = [
        {
            'idLocation': location.idLocation,
            'name': location.name,
            'latitude': str(location.latitude),
            'longitude': str(location.longitude),
            'region': location.region
        } for location in locations
    ]
    return locations_data, 200

def get_location(id):
    location = location_service.get_by_id(id)
    if location:
        location_data = {
            'idLocation': location.idLocation,
            'name': location.name,
            'latitude': str(location.latitude),
            'longitude': str(location.longitude),
            'region': location.region
        }
        return location_data, 200
    return {'error': 'Location not found'}, 404

def get_sensors_for_location_route(id):
    sensors = location_service.get_sensors(id)
    if sensors is not None:
        sensors_data = [
            {
                'idSensor': sensor.idSensor,
                'sensor_type': sensor.sensor_type,
                'installation_date': str(sensor.installation_date),
                'status': sensor.status,
                'last_maintenance': str(sensor.last_maintenance)
            } for sensor in sensors
        ]
        return sensors_data, 200
    return {'error': 'Location not found or no sensors available'}, 404

def create_location_route():
    data = request.get_json()
    new_location = location_service.create(data)
    return {'message': 'Location created successfully', 'location_id': new_location.idLocation}, 201

def update_location_route(id):
    data = request.get_json()
    location = location_service.update(id, data)
    if location:
        return {'message': 'Location updated successfully'}, 200
    return {'error': 'Location not found'}, 404

def delete_location_route(id):
    location = location_service.get_by_id(id)
    if not location:
        return {'error': 'Location not found'}, 404

    try:
        db.session.delete(location)
        db.session.commit()
        return {'message': 'Location deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete location', 'details': str(e)}, 500

def insert_location_route():
    data = request.get_json()
    name = data.get('name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    region = data.get('region')

    if not (name and latitude and longitude and region):
        return {'error': 'All fields are required'}, 400

    success = location_service.insert(name, latitude, longitude, region)
    if success:
        return {'message': 'Location inserted successfully'}, 201
    else:
        return {'error': 'Failed to insert location'}, 500

def batch_insert_locations_route():
    try:
        for i in range(1, 11):
            name = f"Noname{i}"
            latitude = db.session.execute(text("SELECT RAND() * 90")).scalar()
            longitude = db.session.execute(text("SELECT RAND() * 180")).scalar()
            region = f"Region{i}"

            new_location = Location(name=name, latitude=latitude, longitude=longitude, region=region)
            db.session.add(new_location)

        db.session.commit()
        return {"message": "Batch insert of locations completed successfully."}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": "An unexpected error occurred.", "details": str(e)}, 500