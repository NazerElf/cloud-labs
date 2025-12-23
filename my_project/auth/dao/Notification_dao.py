from models import db
from models import Notification

# Отримати всі сповіщення
def get_all_notifications():
    return Notification.query.all()

# Отримати сповіщення за ID
def get_notification_by_id(id):
    return Notification.query.get(id)

# Створити нове сповіщення
def create_notification(data):
    new_notification = Notification(
        sent_time=data.get('sent_time'),
        method=data.get('method'),
        Users_idUser=data.get('Users_idUser'),
        Alerts_idAlert=data.get('Alerts_idAlert')
    )
    db.session.add(new_notification)
    db.session.commit()
    return new_notification

# Оновити сповіщення за ID
def update_notification(id, data):
    notification = get_notification_by_id(id)
    if notification:
        notification.sent_time = data.get('sent_time', notification.sent_time)
        notification.method = data.get('method', notification.method)
        notification.Users_idUser = data.get('Users_idUser', notification.Users_idUser)
        notification.Alerts_idAlert = data.get('Alerts_idAlert', notification.Alerts_idAlert)
        db.session.commit()
        return notification
    return None

# Видалити сповіщення за ID
def delete_notification(id):
    notification = get_notification_by_id(id)
    if notification:
        db.session.delete(notification)
        db.session.commit()
        return True
    return False
