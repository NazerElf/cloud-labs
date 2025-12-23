from flask import request
from models import db
from ..service.user_service import UserService

user_service = UserService()

def get_users():
    users = user_service.get_all()
    users_data = [
        {
            'idUser': user.idUser,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'phone_number': user.phone_number
        } for user in users
    ]
    return users_data, 200

def get_user(id):
    user = user_service.get_by_id(id)
    if user:
        user_data = {
            'idUser': user.idUser,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'phone_number': user.phone_number
        }
        return user_data, 200
    return {'error': 'User not found'}, 404

def create_user_route():
    data = request.get_json()
    new_user = user_service.create(data)
    return {'message': 'User created successfully', 'user_id': new_user.idUser}, 201

def update_user_route(id):
    data = request.get_json()
    user = user_service.update(id, data)
    if user:
        return {'message': 'User updated successfully'}, 200
    return {'error': 'User not found'}, 404

def delete_user_route(id):
    user = user_service.get_by_id(id)
    if not user:
        return {'error': 'User not found'}, 404

    try:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete user', 'details': str(e)}, 500
