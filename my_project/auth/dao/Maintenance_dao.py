from models import db
from models import Maintenance

# Отримати всі Maintenance
def get_all_maintenance():
    return Maintenance.query.all()

# Отримати Maintenance за ID
def get_maintenance_by_id(id):
    return Maintenance.query.get(id)

# Створити нове Maintenance
def create_maintenance(data):
    new_maintenance = Maintenance(
        maintenance_date=data.get('maintenance_date'),
        comments=data.get('comments'),
        Sensors_idSensor=data.get('Sensors_idSensor'),
        Users_idUser=data.get('Users_idUser')
    )
    db.session.add(new_maintenance)
    db.session.commit()
    return new_maintenance

# Оновити Maintenance
def update_maintenance(id, data):
    maintenance = get_maintenance_by_id(id)
    if maintenance:
        maintenance.maintenance_date = data.get('maintenance_date', maintenance.maintenance_date)
        maintenance.comments = data.get('comments', maintenance.comments)
        maintenance.Sensors_idSensor = data.get('Sensors_idSensor', maintenance.Sensors_idSensor)
        maintenance.Users_idUser = data.get('Users_idUser', maintenance.Users_idUser)
        db.session.commit()
        return maintenance
    return None

# Видалити Maintenance
def delete_maintenance(id):
    maintenance = get_maintenance_by_id(id)
    if maintenance:
        db.session.delete(maintenance)
        db.session.commit()
        return True
    return False
