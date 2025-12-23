from .general_service import GeneralService
from ..dao.EventLog_dao import get_all_event_logs, get_event_log_by_id, create_event_log, update_event_log, delete_event_log

class EventLogService(GeneralService):
    def get_all(self):
        return get_all_event_logs()

    def get_by_id(self, id):
        return get_event_log_by_id(id)

    def create(self, data):
        return create_event_log(data)

    def update(self, id, data):
        return update_event_log(id, data)

    def delete(self, id):
        return delete_event_log(id)
