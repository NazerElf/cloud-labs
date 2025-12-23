from models import db
from models import Weather

# Отримати всі дані про погоду
def get_all_weather():
    return Weather.query.all()

# Отримати дані про погоду за ID
def get_weather_by_id(id):
    return Weather.query.get(id)

# Створити нові дані про погоду
def create_weather(data):
    new_weather = Weather(
        weather_time=data.get('weather_time'),
        precipitation=data.get('precipitation'),
        wind_speed=data.get('wind_speed'),
        temperature=data.get('temperature'),
        Locations_idLocation=data.get('Locations_idLocation')
    )
    db.session.add(new_weather)
    db.session.commit()
    return new_weather

# Оновити дані про погоду за ID
def update_weather(id, data):
    weather = get_weather_by_id(id)
    if weather:
        weather.weather_time = data.get('weather_time', weather.weather_time)
        weather.precipitation = data.get('precipitation', weather.precipitation)
        weather.wind_speed = data.get('wind_speed', weather.wind_speed)
        weather.temperature = data.get('temperature', weather.temperature)
        weather.Locations_idLocation = data.get('Locations_idLocation', weather.Locations_idLocation)
        db.session.commit()
        return weather
    return None

# Видалити дані про погоду за ID
def delete_weather(id):
    weather = get_weather_by_id(id)
    if weather:
        db.session.delete(weather)
        db.session.commit()
        return True
    return False
