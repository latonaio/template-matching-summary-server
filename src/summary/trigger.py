from src import log
from src.summary.base import BaseSummary


class TriggerSummary(BaseSummary):
    def __init__(self):
        self.vehicle_name = None
        self.reset()

    def reset(self):
        super().reset()
        return

    def should_be_reset(self, dicts):
        new_vehicle_name = None
        if dicts[0]['templates']:
            new_vehicle_name = dicts[0]['templates'][0]['vehicle_name']

        if (self.vehicle_name or new_vehicle_name) and self.vehicle_name != new_vehicle_name:
            self.vehicle_name = new_vehicle_name
            return True
        return False

    def get_trigger(self):
        res = {
            'status': False,
            'values': []
        }

        if len(self._template_dicts) == 0:
            return res

        # status
        res['status'] = True
        # values
        res['values'] = self._template_dicts
        return res


if __name__ == "__main__":
    import json
    with open('json/C_TemplateMatchingSummary.json') as f:
        _dict = json.load(f)
    dicts = _dict['metadata'][0]['value']

    summary = TriggerSummary()
    should_be_reset = summary.should_be_reset(dicts)
    log.print(should_be_reset)
    if should_be_reset:
        summary.reset()

    summary.set(dicts)

    trigger = summary.get_trigger()
    log.print(trigger)

    end = summary.get_end()
    log.print(end)

    metadata = summary.get_metadata()
    log.print(metadata)

    summary.stack()
