from flask_restx import Namespace, Resource, fields
from flask import request
from my_project.auth.controller.Sensor_controller import (
    get_sensors,
    get_sensor,
    create_sensor_route,
    update_sensor_route,
    delete_sensor_route,
    insert_sensor_route
)

sensor_ns = Namespace('sensors', description='Sensor operations')

# Model Definition
sensor_model = sensor_ns.model('Sensor', {
    'id': fields.Integer(readonly=True, description='The sensor unique identifier'),
    'sensor_type': fields.String(required=True, description='Type of sensor (e.g. Temperature)'),
    'installation_date': fields.String(description='Date of installation (YYYY-MM-DD)'),
    'status': fields.String(description='Status (Active/Inactive)'),
    'last_maintenance': fields.String(description='Last maintenance date'),
    'location_id': fields.Integer(required=True, attribute='location_id', description='Location ID')
})

sensor_input_model = sensor_ns.model('SensorInput', {
    'sensor_type': fields.String(required=True),
    'installation_date': fields.String(),
    'status': fields.String(),
    'last_maintenance': fields.String(),
    'Locations_idLocation': fields.Integer(required=True, description='Location ID')
})

@sensor_ns.route('/')
class SensorList(Resource):
    @sensor_ns.doc('list_sensors')
    @sensor_ns.marshal_list_with(sensor_model)
    def get(self):
        """List all sensors"""
        return get_sensors()

    @sensor_ns.doc('create_sensor')
    @sensor_ns.expect(sensor_input_model)
    def post(self):
        """Create a new sensor"""
        return create_sensor_route()

@sensor_ns.route('/<int:id>')
@sensor_ns.param('id', 'The sensor identifier')
@sensor_ns.response(404, 'Sensor not found')
class SensorResource(Resource):
    @sensor_ns.doc('get_sensor')
    def get(self, id):
        """Fetch a sensor given its identifier"""
        # The controller returns tuple (data, 200) or ({error}, 404)
        # Standard Flask-RESTX might expect object.
        # Since controller returns tuples, we can return them directly.
        # But for documentation (marshal_with), it expects the object part.
        # Our controller returns (dict, status). Restx handles this.
        return get_sensor(id)

    @sensor_ns.doc('update_sensor')
    @sensor_ns.expect(sensor_input_model)
    def put(self, id):
        """Update a sensor given its identifier"""
        return update_sensor_route(id)

    @sensor_ns.doc('delete_sensor')
    def delete(self, id):
        """Delete a sensor given its identifier"""
        return delete_sensor_route(id)

@sensor_ns.route('/insert_sensor')
class SensorInsert(Resource):
    @sensor_ns.doc('insert_sensor_sql')
    @sensor_ns.expect(sensor_input_model)
    def post(self):
        """Insert sensor using direct SQL (Lab requirements)"""
        return insert_sensor_route()

def register_sensor_namespace(api):
    api.add_namespace(sensor_ns)

