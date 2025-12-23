from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.Maintenance_controller import (
    get_maintenances,
    get_maintenance,
    create_maintenance_route,
    update_maintenance_route,
    delete_maintenance_route
)

maintenance_ns = Namespace('maintenances', description='Maintenance operations')

maintenance_model = maintenance_ns.model('Maintenance', {
    'idMaintenance': fields.Integer(readonly=True),
    'maintenance_date': fields.String,
    'comments': fields.String,
    'Sensors_idSensor': fields.Integer,
    'Users_idUser': fields.Integer
})

maintenance_input_model = maintenance_ns.model('MaintenanceInput', {
    'maintenance_date': fields.String,
    'comments': fields.String,
    'Sensors_idSensor': fields.Integer(required=True),
    'Users_idUser': fields.Integer(required=True)
})

@maintenance_ns.route('/')
class MaintenanceList(Resource):
    @maintenance_ns.doc('list_maintenances')
    @maintenance_ns.marshal_list_with(maintenance_model)
    def get(self):
        """List all maintenances"""
        return get_maintenances()

    @maintenance_ns.doc('create_maintenance')
    @maintenance_ns.expect(maintenance_input_model)
    def post(self):
        """Create a new maintenance"""
        return create_maintenance_route()

@maintenance_ns.route('/<int:id>')
@maintenance_ns.param('id', 'The maintenance identifier')
class MaintenanceResource(Resource):
    @maintenance_ns.doc('get_maintenance')
    def get(self, id):
        """Get maintenance by ID"""
        return get_maintenance(id)

    @maintenance_ns.doc('update_maintenance')
    @maintenance_ns.expect(maintenance_input_model)
    def put(self, id):
        """Update maintenance"""
        return update_maintenance_route(id)

    @maintenance_ns.doc('delete_maintenance')
    def delete(self, id):
        """Delete maintenance"""
        return delete_maintenance_route(id)

def register_maintenance_namespace(api):
    api.add_namespace(maintenance_ns)
