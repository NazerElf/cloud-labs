from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.User_controller import (
    get_users,
    get_user,
    create_user_route,
    update_user_route,
    delete_user_route
)

user_ns = Namespace('users', description='User operations')

user_model = user_ns.model('User', {
    'idUser': fields.Integer(readonly=True),
    'username': fields.String,
    'email': fields.String,
    'role': fields.String,
    'phone_number': fields.String
})

user_input_model = user_ns.model('UserInput', {
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'role': fields.String,
    'phone_number': fields.String
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return get_users()

    @user_ns.doc('create_user')
    @user_ns.expect(user_input_model)
    def post(self):
        """Create a new user"""
        return create_user_route()

@user_ns.route('/<int:id>')
@user_ns.param('id', 'The user identifier')
class UserResource(Resource):
    @user_ns.doc('get_user')
    def get(self, id):
        """Get user by ID"""
        return get_user(id)

    @user_ns.doc('update_user')
    @user_ns.expect(user_input_model)
    def put(self, id):
        """Update user"""
        return update_user_route(id)

    @user_ns.doc('delete_user')
    def delete(self, id):
        """Delete user"""
        return delete_user_route(id)

def register_user_namespace(api):
    api.add_namespace(user_ns)
