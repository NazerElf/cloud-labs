from .general_service import GeneralService
from ..dao.User_dao import get_all_users, get_user_by_id, create_user, update_user, delete_user, get_user_by_username

class UserService(GeneralService):
    def get_all(self):
        return get_all_users()

    def get_by_id(self, id):
        return get_user_by_id(id)

    def create(self, data):
        return create_user(data)

    def update(self, id, data):
        return update_user(id, data)

    def delete(self, id):
        return delete_user(id)

    def get_by_username(self, username):
        return get_user_by_username(username)
