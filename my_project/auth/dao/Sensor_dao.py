from models import db, Sensor
from flask import abort
from sqlalchemy import text

# Отримати всі сенсори
def get_all_sensors():
    return Sensor.query.all()

# Отримати сенсор за ID
def get_sensor_by_id(sensor_id):
    return Sensor.query.get(sensor_id)

# Створити новий сенсор
def create_sensor(data):
    required_fields = ['sensor_type', 'installation_date', 'status', 'last_maintenance', 'Locations_idLocation']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")

    new_sensor = Sensor(
        sensor_type=data['sensor_type'],
        installation_date=data['installation_date'],
        status=data['status'],
        last_maintenance=data['last_maintenance'],
        Locations_idLocation=data['Locations_idLocation']
    )
    db.session.add(new_sensor)
    db.session.commit()
    return new_sensor

# Оновити сенсор
def update_sensor(sensor_id, data):
    sensor = Sensor.query.get(sensor_id)
    if not sensor:
        return None

    sensor.sensor_type = data.get('sensor_type', sensor.sensor_type)
    sensor.installation_date = data.get('installation_date', sensor.installation_date)
    sensor.status = data.get('status', sensor.status)
    sensor.last_maintenance = data.get('last_maintenance', sensor.last_maintenance)
    sensor.Locations_idLocation = data.get('Locations_idLocation', sensor.Locations_idLocation)

    db.session.commit()
    return sensor

# Видалити сенсор
def delete_sensor(sensor_id):
    sensor = Sensor.query.get(sensor_id)
    if sensor:
        db.session.delete(sensor)
        db.session.commit()

# Вставка сенсора через SQL
def insert_sensor(sensor_type, installation_date, status, last_maintenance, Locations_idLocation):
    sql = text("""
            CALL InsertIntoSensor(:sensor_type, :installation_date, :status, :last_maintenance, :Locations_idLocation)
        """)

    db.session.execute(sql, {'sensor_type': sensor_type, 'installation_date': installation_date,
                             'status': status, 'last_maintenance': last_maintenance, 'Locations_idLocation': Locations_idLocation})
    db.session.commit()
