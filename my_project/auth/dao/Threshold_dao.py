from models import db
from models import Threshold

# Отримати всі порогові значення
def get_all_thresholds():
    return Threshold.query.all()

# Отримати порогове значення за ID
def get_threshold_by_id(id):
    return Threshold.query.get(id)

# Створити нове порогове значення
def create_threshold(data):
    new_threshold = Threshold(
        water_level_min=data.get('water_level_min'),
        water_level_max=data.get('water_level_max'),
        flow_rate_max=data.get('flow_rate_max'),
        Sensors_idSensor=data.get('Sensors_idSensor')
    )
    db.session.add(new_threshold)
    db.session.commit()
    return new_threshold

# Оновити порогове значення за ID
def update_threshold(id, data):
    threshold = get_threshold_by_id(id)
    if threshold:
        threshold.water_level_min = data.get('water_level_min', threshold.water_level_min)
        threshold.water_level_max = data.get('water_level_max', threshold.water_level_max)
        threshold.flow_rate_max = data.get('flow_rate_max', threshold.flow_rate_max)
        threshold.Sensors_idSensor = data.get('Sensors_idSensor', threshold.Sensors_idSensor)
        db.session.commit()
        return threshold
    return None

# Видалити порогове значення за ID
def delete_threshold(id):
    threshold = get_threshold_by_id(id)
    if threshold:
        db.session.delete(threshold)
        db.session.commit()
        return True
    return False
