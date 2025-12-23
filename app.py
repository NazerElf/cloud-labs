from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from models import db
from flask_restx import Api
from flask_jwt_extended import JWTManager

# Import namespace registration functions
from my_project.auth.route.Sensor_route import register_sensor_namespace
from my_project.auth.route.Location_route import register_location_namespace
from my_project.auth.route.Alert_route import register_alert_namespace
from my_project.auth.route.Measurement_route import register_measurement_namespace
from my_project.auth.route.User_route import register_user_namespace
from my_project.auth.route.EventLog_route import register_event_log_namespace
from my_project.auth.route.Maintenance_route import register_maintenance_namespace
from my_project.auth.route.MaintenanceLog_route import register_maintenance_log_namespace
from my_project.auth.route.SensorAlert_route import register_sensor_alert_namespace
from my_project.auth.route.AllTable_route import register_all_table_namespace
from my_project.auth.route.Auth_route import register_auth_namespace

load_dotenv()

def register_routes(api):
    register_auth_namespace(api)
    register_sensor_namespace(api)
    register_location_namespace(api)
    register_alert_namespace(api)
    register_measurement_namespace(api)
    register_user_namespace(api)
    register_event_log_namespace(api)
    register_maintenance_namespace(api)
    register_maintenance_log_namespace(api)
    register_sensor_alert_namespace(api)
    register_all_table_namespace(api)

app = Flask(__name__)
# Enable CORS
CORS(app)

app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**"
    }
}

# Initialize Flask-RESTX
api = Api(app, doc='/api/docs', title='Sensor API', description='Test',
          authorizations=authorizations, security='Bearer Auth')

register_routes(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)

