from aion.websocket_server import BaseServerClass

from src import log
from src.errors import TemplateMatchingSummaryServerError
from src.summary.vehicle import VehicleSummary


class VehicleServer(BaseServerClass):
    summary = VehicleSummary()

    @log.client.function_log
    async def template_matching_by_opencv(self, sid, data):
        log.print(data, debug=True)
        dicts = data.get('templateMatchingByOpenCV')
        if not dicts:
            msg = 'Request body is not found.'
            raise TemplateMatchingSummaryServerError(msg)

        self.summary.set(dicts)
        vehicle_dict = self.summary.get_vehicle()
        end_dict = self.summary.get_end()
        res = self.summary.get_metadata()
        self.summary.stack()
        summary_dict = self.summary.get_all_vehicles()
        res['vehicle'] = vehicle_dict
        res['end'] = end_dict
        res['summary'] = summary_dict

        if end_dict['status']:
            self.summary.reset()
        return res

    @log.client.function_log
    async def reset(self, sid, data):
        self.summary.reset()
        return
