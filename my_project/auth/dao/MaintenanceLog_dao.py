from models import db
from models import MaintenanceLog

# Отримати всі Maintenance Logs
def get_all_maintenance_logs():
    return MaintenanceLog.query.all()

# Отримати Maintenance Log за ID
def get_maintenance_log_by_id(id):
    return MaintenanceLog.query.get(id)

# Створити новий Maintenance Log
def create_maintenance_log(data):
    new_log = MaintenanceLog(
        maintenance_date=data.get('maintenance_date'),
        comments=data.get('comments'),
        sensor_id=data.get('sensor_id')
    )
    db.session.add(new_log)
    db.session.commit()
    return new_log

# Оновити Maintenance Log
def update_maintenance_log(id, data):
    log = get_maintenance_log_by_id(id)
    if log:
        log.maintenance_date = data.get('maintenance_date', log.maintenance_date)
        log.comments = data.get('comments', log.comments)
        log.sensor_id = data.get('sensor_id', log.sensor_id)
        db.session.commit()
        return log
    return None

# Видалити Maintenance Log
def delete_maintenance_log(id):
    log = get_maintenance_log_by_id(id)
    if log:
        db.session.delete(log)
        db.session.commit()
        return True
    return False
