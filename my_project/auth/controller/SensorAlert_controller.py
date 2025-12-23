from flask import request
from ..service.sensor_alert_service import SensorAlertService

sensor_alert_service = SensorAlertService()

def create_sensor_alert_route():
    data = request.get_json()
    sensor_name = data.get('sensor_name')
    alert_description = data.get('alert_description')

    if not sensor_name or not alert_description:
        return {'error': 'Both sensor_name and alert_description are required.'}, 400

    # Service.create expects dict, but here logic was specific args in DAO.
    # Service "create" implementation above accepted data dict and extracted args.
    result = sensor_alert_service.create(data)
    
    if "error" in result:
        return result, 400
    return result, 201
