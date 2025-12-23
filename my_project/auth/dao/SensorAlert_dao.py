from sqlalchemy import text
from models import db, Sensor, Alert


def insert_sensor_alert(sensor_name, alert_description):
    try:
        # Отримати sensor_id
        sensor = Sensor.query.filter_by(sensor_type=sensor_name).first()
        if not sensor:
            raise ValueError(f"Sensor with name '{sensor_name}' not found.")

        # Отримати alert_id
        alert = Alert.query.filter_by(description=alert_description).first()
        if not alert:
            raise ValueError(f"Alert with description '{alert_description}' not found.")

        # Перевірити, чи існує вже запис
        query = db.session.execute(
            text("SELECT COUNT(*) FROM sensor_alert WHERE sensor_id = :sensor_id AND alert_id = :alert_id"),
            {"sensor_id": sensor.idSensor, "alert_id": alert.idAlert}
        ).scalar()

        if query > 0:
            raise ValueError("The relationship already exists in the sensor_alert table.")

        # Додати новий запис
        db.session.execute(
            text("INSERT INTO sensor_alert (sensor_id, alert_id) VALUES (:sensor_id, :alert_id)"),
            {"sensor_id": sensor.idSensor, "alert_id": alert.idAlert}
        )
        db.session.commit()
        return {"message": "Sensor alert relationship added successfully."}
    except ValueError as ve:
        db.session.rollback()
        return {"error": str(ve)}
    except Exception as e:
        db.session.rollback()
        return {"error": "An unexpected error occurred.", "details": str(e)}