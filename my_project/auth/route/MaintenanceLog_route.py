from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.MaintenanceLog_controller import (
    get_maintenance_logs,
    get_maintenance_log,
    create_maintenance_log_route,
    update_maintenance_log_route,
    delete_maintenance_log_route
)

maintenance_log_ns = Namespace('maintenance_logs', description='Maintenance Log operations')

maintenance_log_model = maintenance_log_ns.model('MaintenanceLog', {
    'idMaintenanceLog': fields.Integer(readonly=True),
    'maintenance_date': fields.String,
    'comments': fields.String,
    'sensor_id': fields.Integer
})

maintenance_log_input_model = maintenance_log_ns.model('MaintenanceLogInput', {
    'maintenance_date': fields.String(required=True),
    'comments': fields.String(required=True),
    'sensor_id': fields.Integer(required=True)
})

@maintenance_log_ns.route('/')
class MaintenanceLogList(Resource):
    @maintenance_log_ns.doc('list_maintenance_logs')
    @maintenance_log_ns.marshal_list_with(maintenance_log_model)
    def get(self):
        """List all maintenance logs"""
        return get_maintenance_logs()

    @maintenance_log_ns.doc('create_maintenance_log')
    @maintenance_log_ns.expect(maintenance_log_input_model)
    def post(self):
        """Create a new maintenance log"""
        return create_maintenance_log_route()

@maintenance_log_ns.route('/<int:id>')
@maintenance_log_ns.param('id', 'The maintenance log identifier')
class MaintenanceLogResource(Resource):
    @maintenance_log_ns.doc('get_maintenance_log')
    def get(self, id):
        """Get maintenance log by ID"""
        return get_maintenance_log(id)

    @maintenance_log_ns.doc('update_maintenance_log')
    @maintenance_log_ns.expect(maintenance_log_input_model)
    def put(self, id):
        """Update maintenance log"""
        return update_maintenance_log_route(id)

    @maintenance_log_ns.doc('delete_maintenance_log')
    def delete(self, id):
        """Delete maintenance log"""
        return delete_maintenance_log_route(id)

def register_maintenance_log_namespace(api):
    api.add_namespace(maintenance_log_ns)
