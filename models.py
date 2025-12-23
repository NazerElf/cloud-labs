from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Location(db.Model):
    __tablename__ = 'locations'
    idLocation = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Numeric(9, 6), nullable=True)
    longitude = db.Column(db.Numeric(9, 6), nullable=True)
    region = db.Column(db.String(100), nullable=True)

    sensors = db.relationship('Sensor', backref='location', lazy=True)
    weather = db.relationship('Weather', backref='location', lazy=True)


class Sensor(db.Model):
    __tablename__ = 'sensors'
    idSensor = db.Column(db.Integer, primary_key=True)
    sensor_type = db.Column(db.String(50), nullable=True)
    installation_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=True)
    last_maintenance = db.Column(db.Date, nullable=True)
    Locations_idLocation = db.Column(db.Integer, db.ForeignKey('locations.idLocation'), nullable=False)

    alerts = db.relationship('Alert', backref='sensor', lazy=True)
    measurements = db.relationship('Measurement', backref='sensor', lazy=True)
    maintenance = db.relationship('Maintenance', backref='sensor', lazy=True)
    thresholds = db.relationship('Threshold', backref='sensor', lazy=True)


class Alert(db.Model):
    __tablename__ = 'alerts'
    idAlert = db.Column(db.Integer, primary_key=True)
    alert_time = db.Column(db.DateTime, nullable=True)
    alert_level = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text, nullable=True)
    Sensors_idSensor = db.Column(db.Integer, db.ForeignKey('sensors.idSensor'), nullable=False)


class User(db.Model):
    __tablename__ = 'users'
    idUser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)

    notifications = db.relationship('Notification', backref='user', lazy=True)
    event_log = db.relationship('EventLog', backref='user', lazy=True)
    maintenance = db.relationship('Maintenance', backref='user', lazy=True)


class EventLog(db.Model):
    __tablename__ = 'event_log'
    idEvent_Log = db.Column(db.Integer, primary_key=True)
    event_time = db.Column(db.DateTime, nullable=True)
    event_type = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    Users_idUser = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)
    Sensors_idSensor = db.Column(db.Integer, db.ForeignKey('sensors.idSensor'), nullable=False)


class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    idMaintenance = db.Column(db.Integer, primary_key=True)
    maintenance_date = db.Column(db.Date, nullable=True)
    comments = db.Column(db.Text, nullable=True)
    Sensors_idSensor = db.Column(db.Integer, db.ForeignKey('sensors.idSensor'), nullable=False)
    Users_idUser = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)


class Measurement(db.Model):
    __tablename__ = 'measurements'
    idMeasurements = db.Column(db.Integer, primary_key=True)
    measurement_time = db.Column(db.DateTime, nullable=True)
    water_level = db.Column(db.Numeric(5, 2), nullable=True)
    water_temperature = db.Column(db.Numeric(4, 2), nullable=True)
    flow_rate = db.Column(db.Numeric(6, 2), nullable=True)
    Sensors_idSensor = db.Column(db.Integer, db.ForeignKey('sensors.idSensor'), nullable=False)


class Notification(db.Model):
    __tablename__ = 'notifications'
    idNotifications = db.Column(db.Integer, primary_key=True)
    sent_time = db.Column(db.DateTime, nullable=True)
    method = db.Column(db.String(20), nullable=True)
    Users_idUser = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)
    Alerts_idAlert = db.Column(db.Integer, db.ForeignKey('alerts.idAlert'), nullable=False)


class Threshold(db.Model):
    __tablename__ = 'thresholds'
    idThresholds = db.Column(db.Integer, primary_key=True)
    water_level_min = db.Column(db.Numeric(5, 2), nullable=True)
    water_level_max = db.Column(db.Numeric(5, 2), nullable=True)
    flow_rate_max = db.Column(db.Numeric(6, 3), nullable=True)
    Sensors_idSensor = db.Column(db.Integer, db.ForeignKey('sensors.idSensor'), nullable=False)


class Weather(db.Model):
    __tablename__ = 'weather'
    idWeather = db.Column(db.Integer, primary_key=True)
    weather_time = db.Column(db.DateTime, nullable=True)
    precipitation = db.Column(db.Numeric(5, 2), nullable=True)
    wind_speed = db.Column(db.Numeric(4, 2), nullable=True)
    temperature = db.Column(db.Numeric(4, 2), nullable=True)
    Locations_idLocation = db.Column(db.Integer, db.ForeignKey('locations.idLocation'), nullable=False)

class MaintenanceLog(db.Model):
    __tablename__ = 'maintenance_log'
    idMaintenanceLog = db.Column(db.Integer, primary_key=True, autoincrement=True)
    maintenance_date = db.Column(db.Date, nullable=False)
    comments = db.Column(db.Text, nullable=False)
    sensor_id = db.Column(db.Integer, nullable=False)