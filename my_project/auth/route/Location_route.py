from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.Location_controller import (
    get_locations,
    get_location,
    create_location_route,
    update_location_route,
    delete_location_route,
    get_sensors_for_location_route,
    insert_location_route,
    batch_insert_locations_route
)

location_ns = Namespace('locations', description='Location operations')

location_model = location_ns.model('Location', {
    'idLocation': fields.Integer(readonly=True),
    'name': fields.String,
    'latitude': fields.String,
    'longitude': fields.String,
    'region': fields.String
})

location_input_model = location_ns.model('LocationInput', {
    'name': fields.String(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'region': fields.String(required=True)
})

# Needs sensor model for nested return? Or generic
sensor_simple_model = location_ns.model('SensorSimple', {
    'idSensor': fields.Integer,
    'sensor_type': fields.String,
    'installation_date': fields.String,
    'status': fields.String,
    'last_maintenance': fields.String
})

@location_ns.route('/')
class LocationList(Resource):
    @location_ns.doc('list_locations')
    @location_ns.marshal_list_with(location_model)
    def get(self):
        """List all locations"""
        return get_locations()

    @location_ns.doc('create_location')
    @location_ns.expect(location_input_model)
    def post(self):
        """Create a new location"""
        return create_location_route()

@location_ns.route('/<int:id>')
@location_ns.param('id', 'The location identifier')
class LocationResource(Resource):
    @location_ns.doc('get_location')
    def get(self, id):
        """Get location by ID"""
        return get_location(id)

    @location_ns.doc('update_location')
    @location_ns.expect(location_input_model)
    def put(self, id):
        """Update location"""
        return update_location_route(id)

    @location_ns.doc('delete_location')
    def delete(self, id):
        """Delete location"""
        return delete_location_route(id)

@location_ns.route('/<int:id>/sensors')
class LocationSensors(Resource):
    @location_ns.doc('get_location_sensors')
    @location_ns.marshal_list_with(sensor_simple_model)
    def get(self, id):
        """Get sensors for a specific location"""
        return get_sensors_for_location_route(id)

@location_ns.route('/insert')
class LocationInsert(Resource):
    @location_ns.doc('insert_location_sql')
    @location_ns.expect(location_input_model)
    def post(self):
        """Insert location (SQL)"""
        return insert_location_route()

@location_ns.route('/batch_insert')
class LocationBatchInsert(Resource):
    @location_ns.doc('batch_insert_locations')
    def post(self):
        """Batch insert random locations"""
        return batch_insert_locations_route()

def register_location_namespace(api):
    api.add_namespace(location_ns)
