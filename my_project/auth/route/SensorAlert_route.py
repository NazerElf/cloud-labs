from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.SensorAlert_controller import (
    create_sensor_alert_route
)

sensor_alert_ns = Namespace('sensor_alerts', description='Sensor Alert interactions')

sensor_alert_input_model = sensor_alert_ns.model('SensorAlertInput', {
    'sensor_name': fields.String(required=True),
    'alert_description': fields.String(required=True)
})

@sensor_alert_ns.route('/')
class SensorAlertResource(Resource):
    @sensor_alert_ns.doc('create_sensor_alert')
    @sensor_alert_ns.expect(sensor_alert_input_model)
    def post(self):
        """Create a new sensor alert (Procedure Call)"""
        return create_sensor_alert_route()

def register_sensor_alert_namespace(api):
    api.add_namespace(sensor_alert_ns)