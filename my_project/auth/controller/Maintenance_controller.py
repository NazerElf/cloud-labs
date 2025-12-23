from flask import request
from models import db
from ..service.maintenance_service import MaintenanceService

maintenance_service = MaintenanceService()

# Отримати всі Maintenance
def get_maintenances():
    maintenances = maintenance_service.get_all()
    maintenances_data = [
        {
            'idMaintenance': maintenance.idMaintenance,
            'maintenance_date': str(maintenance.maintenance_date),
            'comments': maintenance.comments,
            'Sensors_idSensor': maintenance.Sensors_idSensor,
            'Users_idUser': maintenance.Users_idUser
        } for maintenance in maintenances
    ]
    return maintenances_data, 200

# Отримати Maintenance за ID
def get_maintenance(id):
    maintenance = maintenance_service.get_by_id(id)
    if maintenance:
        maintenance_data = {
            'idMaintenance': maintenance.idMaintenance,
            'maintenance_date': str(maintenance.maintenance_date),
            'comments': maintenance.comments,
            'Sensors_idSensor': maintenance.Sensors_idSensor,
            'Users_idUser': maintenance.Users_idUser
        }
        return maintenance_data, 200
    return {'error': 'Maintenance not found'}, 404

# Створити нове Maintenance
def create_maintenance_route():
    data = request.get_json()
    new_maintenance = maintenance_service.create(data)
    return {'message': 'Maintenance created successfully', 'maintenance_id': new_maintenance.idMaintenance}, 201

# Оновити Maintenance
def update_maintenance_route(id):
    data = request.get_json()
    maintenance = maintenance_service.update(id, data)
    if maintenance:
        return {'message': 'Maintenance updated successfully'}, 200
    return {'error': 'Maintenance not found'}, 404

# Видалити Maintenance
def delete_maintenance_route(id):
    maintenance = maintenance_service.get_by_id(id)
    if not maintenance:
        return {'error': 'Maintenance not found'}, 404

    try:
        db.session.delete(maintenance)
        db.session.commit()
        return {'message': 'Maintenance deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete Maintenance', 'details': str(e)}, 500
