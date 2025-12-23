from models import db
from models import Measurement

# Отримати всі вимірювання
def get_all_measurements():
    return Measurement.query.all()

# Отримати вимірювання за ID
def get_measurement_by_id(id):
    return Measurement.query.get(id)

# Створити нове вимірювання
def create_measurement(data):
    new_measurement = Measurement(
        measurement_time=data.get('measurement_time'),
        water_level=data.get('water_level'),
        water_temperature=data.get('water_temperature'),
        flow_rate=data.get('flow_rate'),
        Sensors_idSensor=data.get('Sensors_idSensor')
    )
    db.session.add(new_measurement)
    db.session.commit()
    return new_measurement

# Оновити вимірювання за ID
def update_measurement(id, data):
    measurement = get_measurement_by_id(id)
    if measurement:
        measurement.measurement_time = data.get('measurement_time', measurement.measurement_time)
        measurement.water_level = data.get('water_level', measurement.water_level)
        measurement.water_temperature = data.get('water_temperature', measurement.water_temperature)
        measurement.flow_rate = data.get('flow_rate', measurement.flow_rate)
        measurement.Sensors_idSensor = data.get('Sensors_idSensor', measurement.Sensors_idSensor)
        db.session.commit()
        return measurement
    return None

# Видалити вимірювання за ID
def delete_measurement(id):
    measurement = get_measurement_by_id(id)
    if measurement:
        db.session.delete(measurement)
        db.session.commit()
        return True
    return False
