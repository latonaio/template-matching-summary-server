import sys
import pprint

from aion.logger_library.LoggerClient import LoggerClient

client = LoggerClient('TemplateMatchingSummaryServer')


def print(message, debug=False):
    message = pprint.pformat(message, indent=4)

    if not debug or (debug and sys.flags.debug):
        client.print(message)
    return
