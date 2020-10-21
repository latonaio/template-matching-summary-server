from pathlib import Path

from src import log
from src.errors import TemplateMatchingSummaryServerError


@log.client.function_log
def run():
    device_name = Path(__file__).parent.parent.parent.parent.name

    server = None
    if device_name in ['tartarus', 'poseidon', 'lib']:
        from src.servers.vehicle import VehicleServer
        server = VehicleServer
    elif device_name in ['deneb', 'elpis', 'neo', 'moca']:
        from src.servers.trigger import TriggerServer
        server = TriggerServer
    else:
        msg = f'Device name ({device_name}) is wrong.'
        raise TemplateMatchingSummaryServerError(msg)

    server.register_namespace(
        "/template_matching_summary", port=3100)
    return
