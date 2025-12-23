from models import db
from models import EventLog

# Отримати всі EventLog
def get_all_event_logs():
    return EventLog.query.all()

# Отримати EventLog за ID
def get_event_log_by_id(id):
    return EventLog.query.get(id)

# Створити новий EventLog
def create_event_log(data):
    new_event_log = EventLog(
        event_time=data.get('event_time'),
        event_type=data.get('event_type'),
        description=data.get('description'),
        Users_idUser=data.get('Users_idUser'),
        Sensors_idSensor=data.get('Sensors_idSensor')
    )
    db.session.add(new_event_log)
    db.session.commit()
    return new_event_log

# Оновити EventLog
def update_event_log(id, data):
    event_log = get_event_log_by_id(id)
    if event_log:
        event_log.event_time = data.get('event_time', event_log.event_time)
        event_log.event_type = data.get('event_type', event_log.event_type)
        event_log.description = data.get('description', event_log.description)
        event_log.Users_idUser = data.get('Users_idUser', event_log.Users_idUser)
        event_log.Sensors_idSensor = data.get('Sensors_idSensor', event_log.Sensors_idSensor)
        db.session.commit()
        return event_log
    return None

# Видалити EventLog
def delete_event_log(id):
    event_log = get_event_log_by_id(id)
    if event_log:
        db.session.delete(event_log)
        db.session.commit()
        return True
    return False
