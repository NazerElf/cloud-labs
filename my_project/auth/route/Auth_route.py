from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.Auth_controller import login

auth_ns = Namespace('auth', description='Authentication operations')

login_model = auth_ns.model('Login', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.doc('login')
    @auth_ns.expect(login_model)
    def post(self):
        """User login"""
        return login()

def register_auth_namespace(api):
    api.add_namespace(auth_ns)
