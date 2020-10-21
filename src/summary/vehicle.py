from src import log
from src.summary.base import BaseSummary


class VehicleSummary(BaseSummary):
    def __init__(self):
        self.reset()

    def reset(self):
        super().reset()
        self.is_first_vehicle = False
        return

    def _get_vehicle(self, dicts):
        res = {
            'status': False,
            'name': 'Unknown',
            'first': False,
            'values': []
        }

        if len(dicts) == 0:
            return res

        # status
        res['status'] = True
        # name
        res['name'] = dicts[0]['vehicle_name']
        # first
        if not self.is_first_vehicle:
            self.is_first_vehicle = True
            res['first'] = True
        # values
        res['values'] = dicts
        return res

    def get_vehicle(self):
        return self._get_vehicle(self._template_dicts)

    def get_all_vehicles(self):
        return self._get_vehicle(self.template_dicts)


if __name__ == "__main__":
    import json
    with open('json/C_TemplateMatchingSummary.json') as f:
        _dict = json.load(f)
    dicts = _dict['metadata'][0]['value']

    import time
    s = time.time()
    summary = VehicleSummary()
    summary.set(dicts)

    vehicle = summary.get_vehicle()
    log.print(vehicle)

    end = summary.get_end()
    log.print(end)

    metadata = summary.get_metadata()
    log.print(metadata)

    summary.stack()
    if end['status']:
        all_vehicles = summary.get_all_vehicles()
        log.print(all_vehicles)
    print(time.time() - s)
