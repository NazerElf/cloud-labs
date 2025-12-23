from flask_restx import Namespace, Resource, fields
from my_project.auth.controller.AllTable_controller import (
    calculate_stat_controller,
    split_table_controller
)

all_table_ns = Namespace('all_table', description='General Table operations')

calculate_input_model = all_table_ns.model('CalculateInput', {
    'col_name': fields.String(required=True),
    'table_name': fields.String(required=True),
    'operation': fields.String(required=True, enum=['AVG', 'SUM', 'COUNT'])
})

@all_table_ns.route('/calculate')
class CalculateResource(Resource):
    @all_table_ns.doc('calculate_stats')
    @all_table_ns.expect(calculate_input_model)
    def post(self):
        """Calculate statistics"""
        return calculate_stat_controller()

@all_table_ns.route('/split')
class SplitResource(Resource):
    @all_table_ns.doc('split_tables')
    def post(self):
        """Split tables"""
        return split_table_controller()

def register_all_table_namespace(api):
    api.add_namespace(all_table_ns)