from flask import request
from models import db
from ..service.event_log_service import EventLogService

event_log_service = EventLogService()

# Отримати всі EventLog
def get_event_logs():
    event_logs = event_log_service.get_all()
    event_logs_data = [
        {
            'idEvent_Log': event_log.idEvent_Log,
            'event_time': str(event_log.event_time),
            'event_type': event_log.event_type,
            'description': event_log.description,
            'Users_idUser': event_log.Users_idUser,
            'Sensors_idSensor': event_log.Sensors_idSensor
        } for event_log in event_logs
    ]
    return event_logs_data, 200

# Отримати EventLog за ID
def get_event_log(id):
    event_log = event_log_service.get_by_id(id)
    if event_log:
        event_log_data = {
            'idEvent_Log': event_log.idEvent_Log,
            'event_time': str(event_log.event_time),
            'event_type': event_log.event_type,
            'description': event_log.description,
            'Users_idUser': event_log.Users_idUser,
            'Sensors_idSensor': event_log.Sensors_idSensor
        }
        return event_log_data, 200
    return {'error': 'EventLog not found'}, 404

# Створити новий EventLog
def create_event_log_route():
    data = request.get_json()
    new_event_log = event_log_service.create(data)
    return {'message': 'EventLog created successfully', 'event_log_id': new_event_log.idEvent_Log}, 201

# Оновити EventLog
def update_event_log_route(id):
    data = request.get_json()
    event_log = event_log_service.update(id, data)
    if event_log:
        return {'message': 'EventLog updated successfully'}, 200
    return {'error': 'EventLog not found'}, 404

# Видалити EventLog
def delete_event_log_route(id):
    event_log = event_log_service.get_by_id(id)
    if not event_log:
        return {'error': 'EventLog not found'}, 404

    try:
        db.session.delete(event_log)
        db.session.commit()
        return {'message': 'EventLog deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete EventLog', 'details': str(e)}, 500
