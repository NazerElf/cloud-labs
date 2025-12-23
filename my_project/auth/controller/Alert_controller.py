from flask import request
from models import db
from ..service.alert_service import AlertService

alert_service = AlertService()

def get_alerts():
    alerts = alert_service.get_all()
    alerts_data = [
        {
            'idAlert': alert.idAlert,
            'alert_time': alert.alert_time,
            'alert_level': alert.alert_level,
            'description': alert.description,
            'sensor_id': alert.Sensors_idSensor
        } for alert in alerts
    ]
    return alerts_data, 200

def get_alert(id):
    alert = alert_service.get_by_id(id)
    if alert:
        alert_data = {
            'idAlert': alert.idAlert,
            'alert_time': alert.alert_time,
            'alert_level': alert.alert_level,
            'description': alert.description,
            'sensor_id': alert.Sensors_idSensor
        }
        return alert_data, 200
    return {'error': 'Alert not found'}, 404

def create_alert_route():
    data = request.get_json()
    new_alert = alert_service.create(data)
    return {'message': 'Alert created successfully', 'alert_id': new_alert.idAlert}, 201

def update_alert_route(id):
    data = request.get_json()
    alert = alert_service.update(id, data)
    if alert:
        return {'message': 'Alert updated successfully'}, 200
    return {'error': 'Alert not found'}, 404

def delete_alert_route(id):
    alert = alert_service.get_by_id(id)
    if not alert:
        return {'error': 'Alert not found'}, 404

    try:
        db.session.delete(alert)
        db.session.commit()
        return {'message': 'Alert deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete alert', 'details': str(e)}, 500
