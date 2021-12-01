from time import sleep
from . import var
import logging

log = logging.getLogger(__name__)


class EduroamReporter(object):
    def __init__(self):
        log.info("Reporter creating...")
        log.info("Reporter created")

    def run(self):
        log.info("Reporter started")
        try:
            while True:
                sleep(var.UPDATE_SECONDS_INTERVAL)
        except KeyboardInterrupt:
            log.info("Reporter received exit signal")
        finally:
            self.exit()
        log.info("Reporter finished")

    def exit(self):
        log.info("Bot exiting...")
        pass
        log.info("Bot exited")
