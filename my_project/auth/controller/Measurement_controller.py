from flask import request
from models import db
from ..service.measurement_service import MeasurementService

measurement_service = MeasurementService()

def get_measurements():
    measurements = measurement_service.get_all()
    measurements_data = [
        {
            'idMeasurements': measurement.idMeasurements,
            'measurement_time': measurement.measurement_time,
            'water_level': str(measurement.water_level),
            'water_temperature': str(measurement.water_temperature),
            'flow_rate': str(measurement.flow_rate),
            'sensor_id': measurement.Sensors_idSensor
        } for measurement in measurements
    ]
    return measurements_data, 200

def get_measurement(id):
    measurement = measurement_service.get_by_id(id)
    if measurement:
        measurement_data = {
            'idMeasurements': measurement.idMeasurements,
            'measurement_time': measurement.measurement_time,
            'water_level': str(measurement.water_level),
            'water_temperature': str(measurement.water_temperature),
            'flow_rate': str(measurement.flow_rate),
            'sensor_id': measurement.Sensors_idSensor
        }
        return measurement_data, 200
    return {'error': 'Measurement not found'}, 404

def create_measurement_route():
    data = request.get_json()
    new_measurement = measurement_service.create(data)
    return {'message': 'Measurement created successfully', 'measurement_id': new_measurement.idMeasurements}, 201

def update_measurement_route(id):
    data = request.get_json()
    measurement = measurement_service.update(id, data)
    if measurement:
        return {'message': 'Measurement updated successfully'}, 200
    return {'error': 'Measurement not found'}, 404

def delete_measurement_route(id):
    measurement = measurement_service.get_by_id(id)
    if not measurement:
        return {'error': 'Measurement not found'}, 404

    try:
        db.session.delete(measurement)
        db.session.commit()
        return {'message': 'Measurement deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete measurement', 'details': str(e)}, 500
