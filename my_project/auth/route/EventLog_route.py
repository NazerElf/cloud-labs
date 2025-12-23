from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.EventLog_controller import (
    get_event_logs,
    get_event_log,
    create_event_log_route,
    update_event_log_route,
    delete_event_log_route
)

event_log_ns = Namespace('event_logs', description='Event Log operations')

event_log_model = event_log_ns.model('EventLog', {
    'idEvent_Log': fields.Integer(readonly=True),
    'event_time': fields.String,
    'event_type': fields.String,
    'description': fields.String,
    'Users_idUser': fields.Integer,
    'Sensors_idSensor': fields.Integer
})

event_log_input_model = event_log_ns.model('EventLogInput', {
    'event_time': fields.String,
    'event_type': fields.String,
    'description': fields.String,
    'Users_idUser': fields.Integer(required=True),
    'Sensors_idSensor': fields.Integer(required=True)
})

@event_log_ns.route('/')
class EventLogList(Resource):
    @event_log_ns.doc('list_event_logs')
    @event_log_ns.marshal_list_with(event_log_model)
    def get(self):
        """List all event logs"""
        return get_event_logs()

    @event_log_ns.doc('create_event_log')
    @event_log_ns.expect(event_log_input_model)
    def post(self):
        """Create a new event log"""
        return create_event_log_route()

@event_log_ns.route('/<int:id>')
@event_log_ns.param('id', 'The event log identifier')
class EventLogResource(Resource):
    @event_log_ns.doc('get_event_log')
    def get(self, id):
        """Get event log by ID"""
        return get_event_log(id)

    @event_log_ns.doc('update_event_log')
    @event_log_ns.expect(event_log_input_model)
    def put(self, id):
        """Update event log"""
        return update_event_log_route(id)

    @event_log_ns.doc('delete_event_log')
    def delete(self, id):
        """Delete event log"""
        return delete_event_log_route(id)

def register_event_log_namespace(api):
    api.add_namespace(event_log_ns)
