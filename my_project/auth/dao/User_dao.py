from models import db
from models import User

# Отримати всіх користувачів
def get_all_users():
    return User.query.all()

# Отримати користувача за ID
def get_user_by_id(id):
    return User.query.get(id)

# Створити нового користувача
def create_user(data):
    new_user = User(
        username=data.get('username'),
        password=data.get('password'),
        role=data.get('role'),
        email=data.get('email'),
        phone_number=data.get('phone_number')
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

# Оновити користувача за ID
def update_user(id, data):
    user = get_user_by_id(id)
    if user:
        user.username = data.get('username', user.username)
        user.password = data.get('password', user.password)
        user.role = data.get('role', user.role)
        user.email = data.get('email', user.email)
        user.phone_number = data.get('phone_number', user.phone_number)
        db.session.commit()
        return user
    return None

# Видалити користувача за ID
def delete_user(id):
    user = get_user_by_id(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

# Отримати користувача за username
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
