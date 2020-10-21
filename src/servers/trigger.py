from aion.websocket_server import BaseServerClass

from src import log
from src.errors import TemplateMatchingSummaryServerError
from src.summary.trigger import TriggerSummary


class TriggerServer(BaseServerClass):
    summary = TriggerSummary()

    @log.client.function_log
    async def template_matching_by_opencv(self, sid, data):
        log.print(data, debug=True)
        dicts = data.get('templateMatchingByOpenCV')
        if not dicts:
            msg = 'Request body is not found.'
            raise TemplateMatchingSummaryServerError(msg)

        should_be_reset = self.summary.should_be_reset(dicts)
        if should_be_reset:
            self.summary.reset()

        self.summary.set(dicts)
        trigger_dict = self.summary.get_trigger()
        end_dict = self.summary.get_end()
        res = self.summary.get_metadata()
        res['trigger'] = trigger_dict
        res['end'] = end_dict

        if end_dict['status']:
            self.summary.reset()
        return res

    @log.client.function_log
    async def reset(self, sid, data):
        self.summary.reset()
        return
