from flask import request
from models import db
from ..service.maintenance_log_service import MaintenanceLogService

maintenance_log_service = MaintenanceLogService()

# Отримати всі Maintenance Logs
def get_maintenance_logs():
    logs = maintenance_log_service.get_all()
    logs_data = [
        {
            'idMaintenanceLog': log.idMaintenanceLog,
            'maintenance_date': str(log.maintenance_date),
            'comments': log.comments,
            'sensor_id': log.sensor_id
        } for log in logs
    ]
    return logs_data, 200

# Отримати Maintenance Log за ID
def get_maintenance_log(id):
    log = maintenance_log_service.get_by_id(id)
    if log:
        log_data = {
            'idMaintenanceLog': log.idMaintenanceLog,
            'maintenance_date': str(log.maintenance_date),
            'comments': log.comments,
            'sensor_id': log.sensor_id
        }
        return log_data, 200
    return {'error': 'Maintenance log not found'}, 404

# Створити новий Maintenance Log
def create_maintenance_log_route():
    data = request.get_json()
    new_log = maintenance_log_service.create(data)
    return {'message': 'Maintenance log created successfully', 'maintenance_log_id': new_log.idMaintenanceLog}, 201

# Оновити Maintenance Log
def update_maintenance_log_route(id):
    data = request.get_json()
    log = maintenance_log_service.update(id, data)
    if log:
        return {'message': 'Maintenance log updated successfully'}, 200
    return {'error': 'Maintenance log not found'}, 404

# Видалити Maintenance Log
def delete_maintenance_log_route(id):
    log = maintenance_log_service.get_by_id(id)
    if not log:
        return {'error': 'Maintenance log not found'}, 404

    try:
        db.session.delete(log)
        db.session.commit()
        return {'message': 'Maintenance log deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete maintenance log', 'details': str(e)}, 500
