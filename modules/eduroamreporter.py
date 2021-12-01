import os, shutil
from time import sleep
from . import var
import logging

log = logging.getLogger(__name__)


class EduroamReporter(object):
    def __init__(self):
        log.info("Reporter creating...")
        try:
            os.mkdir(var.TEMP_REPORTS_DIR)
        except FileExistsError:
            pass
        log.info("Reporter created")

    def _move_files(self):
        for temp_file in os.listdir(var.TEMP_REPORTS_DIR):
            if not temp_file.split('.') == var.TEMP_REPORTS_EXT:
                shutil.move(os.path.join(var.TEMP_REPORTS_DIR, temp_file), os.path.join(var.REPORTS_DIR, temp_file))

    def run(self):
        log.info("Reporter started")
        try:
            while True:
                sleep(var.UPDATE_SECONDS_INTERVAL)
                self._move_files()
        except KeyboardInterrupt:
            log.info("Reporter received exit signal")
        finally:
            self.exit()
        log.info("Reporter finished")

    def exit(self):
        log.info("Bot exiting...")
        pass
        log.info("Bot exited")
