from flask import request
from flask_jwt_extended import create_access_token
from ..dao.User_dao import get_user_by_username

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {"message": "Username and password are required"}, 400

    user = get_user_by_username(username)

    if user and user.password == password:
        access_token = create_access_token(identity=user.idUser)
        return {"access_token": access_token}, 200

    return {"message": "Invalid credentials"}, 401
