from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.Measurement_controller import (
    get_measurements,
    get_measurement,
    create_measurement_route,
    update_measurement_route,
    delete_measurement_route
)

measurement_ns = Namespace('measurements', description='Measurement operations')

measurement_model = measurement_ns.model('Measurement', {
    'idMeasurements': fields.Integer(readonly=True),
    'measurement_time': fields.String,
    'water_level': fields.String,
    'water_temperature': fields.String,
    'flow_rate': fields.String,
    'sensor_id': fields.Integer
})

measurement_input_model = measurement_ns.model('MeasurementInput', {
    'measurement_time': fields.String,
    'water_level': fields.Float,
    'water_temperature': fields.Float,
    'flow_rate': fields.Float,
    'Sensors_idSensor': fields.Integer(required=True)
})

@measurement_ns.route('/')
class MeasurementList(Resource):
    @measurement_ns.doc('list_measurements')
    @measurement_ns.marshal_list_with(measurement_model)
    def get(self):
        """List all measurements"""
        return get_measurements()

    @measurement_ns.doc('create_measurement')
    @measurement_ns.expect(measurement_input_model)
    def post(self):
        """Create a new measurement"""
        return create_measurement_route()

@measurement_ns.route('/<int:id>')
@measurement_ns.param('id', 'The measurement identifier')
class MeasurementResource(Resource):
    @measurement_ns.doc('get_measurement')
    def get(self, id):
        """Get measurement by ID"""
        return get_measurement(id)

    @measurement_ns.doc('update_measurement')
    @measurement_ns.expect(measurement_input_model)
    def put(self, id):
        """Update measurement"""
        return update_measurement_route(id)

    @measurement_ns.doc('delete_measurement')
    def delete(self, id):
        """Delete measurement"""
        return delete_measurement_route(id)

def register_measurement_namespace(api):
    api.add_namespace(measurement_ns)
