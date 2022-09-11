import os
import sys
import time
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .api import API

class Console():
    def __init__(self, ryujinx_path, level=logging.WARNING):
        logging.basicConfig(format='%(asctime)s - [%(levelname)s] - %(message)s', level=level)
        self.logger = logging.getLogger(__name__)
        self.ryujinx_path = ryujinx_path
        self.api = API(ryujinx_path)
        self.controllers = []

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.logger.info('[libultimate] Cleaning up...')
        time.sleep(0.1)
        for controller in self.controllers:
            controller.release_all()
        self.logger.info('[libultimate] Done.')

    def add_controller(self, controller):
        controller.set_console(self)
        self.controllers.append(controller)

    def stream(self, hz=60):
        interval = 60/hz * (1/60)
        while True:
            try:
                time.sleep(interval)
                gamestate = self.api.read_state()
                yield gamestate
            except Exception as err:
                self.logger.warning("couldn't read state: {}".format(err))
