from models import db
from models import Alert

# Отримати всі попередження
def get_all_alerts():
    return Alert.query.all()

# Отримати попередження за ID
def get_alert_by_id(id):
    return Alert.query.get(id)

# Створити нове попередження
def create_alert(data):
    new_alert = Alert(
        alert_time=data.get('alert_time'),
        alert_level=data.get('alert_level'),
        description=data.get('description'),
        Sensors_idSensor=data.get('Sensors_idSensor')
    )
    db.session.add(new_alert)
    db.session.commit()
    return new_alert

# Оновити попередження за ID
def update_alert(id, data):
    alert = get_alert_by_id(id)
    if alert:
        alert.alert_time = data.get('alert_time', alert.alert_time)
        alert.alert_level = data.get('alert_level', alert.alert_level)
        alert.description = data.get('description', alert.description)
        alert.Sensors_idSensor = data.get('Sensors_idSensor', alert.Sensors_idSensor)
        db.session.commit()
        return alert
    return None

# Видалити попередження за ID
def delete_alert(id):
    alert = get_alert_by_id(id)
    if alert:
        db.session.delete(alert)
        db.session.commit()
        return True
    return False
