from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.Alert_controller import (
    get_alerts,
    get_alert,
    create_alert_route,
    update_alert_route,
    delete_alert_route
)

alert_ns = Namespace('alerts', description='Alert operations')

alert_model = alert_ns.model('Alert', {
    'idAlert': fields.Integer(readonly=True),
    'alert_time': fields.String,
    'alert_level': fields.String,
    'description': fields.String,
    'sensor_id': fields.Integer
})

alert_input_model = alert_ns.model('AlertInput', {
    'alert_time': fields.String,
    'alert_level': fields.String,
    'description': fields.String,
    'Sensors_idSensor': fields.Integer(required=True)
})

@alert_ns.route('/')
class AlertList(Resource):
    @alert_ns.doc('list_alerts')
    @alert_ns.marshal_list_with(alert_model)
    def get(self):
        """List all alerts"""
        return get_alerts()

    @alert_ns.doc('create_alert')
    @alert_ns.expect(alert_input_model)
    def post(self):
        """Create a new alert"""
        return create_alert_route()

@alert_ns.route('/<int:id>')
@alert_ns.param('id', 'The alert identifier')
class AlertResource(Resource):
    @alert_ns.doc('get_alert')
    def get(self, id):
        """Get alert by ID"""
        return get_alert(id)

    @alert_ns.doc('update_alert')
    @alert_ns.expect(alert_input_model)
    def put(self, id):
        """Update alert"""
        return update_alert_route(id)

    @alert_ns.doc('delete_alert')
    def delete(self, id):
        """Delete alert"""
        return delete_alert_route(id)

def register_alert_namespace(api):
    api.add_namespace(alert_ns)
