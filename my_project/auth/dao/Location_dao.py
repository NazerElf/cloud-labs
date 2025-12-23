from models import db
from models import Location, Sensor
from sqlalchemy.sql import text

# Отримати всі локації
def get_all_locations():
    return Location.query.all()

# Отримати локацію за ID
def get_location_by_id(id):
    return Location.query.get(id)

def get_sensors_for_location(id):
    location = Location.query.get(id)
    if location:
        return location.sensors  # Це повертає всі сенсори для цієї локації
    return None

def insert_location(name, latitude, longitude, region):
    sql = text("""
        INSERT INTO locations (name, latitude, longitude, region)
        VALUES (:name, :latitude, :longitude, :region)
    """)
    try:
        db.session.execute(sql, {
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'region': region
        })
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Error inserting location: {e}")
        return False

# Створити нову локацію
def create_location(data):
    new_location = Location(
        name=data.get('name'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        region=data.get('region')
    )
    db.session.add(new_location)
    db.session.commit()
    return new_location

# Оновити локацію за ID
def update_location(id, data):
    location = get_location_by_id(id)
    if location:
        location.name = data.get('name', location.name)
        location.latitude = data.get('latitude', location.latitude)
        location.longitude = data.get('longitude', location.longitude)
        location.region = data.get('region', location.region)
        db.session.commit()
        return location
    return None

# Видалити локацію за ID
def delete_location(id):
    location = get_location_by_id(id)
    if location:
        db.session.delete(location)
        db.session.commit()
        return True
    return False
