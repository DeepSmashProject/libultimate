import os
import sys
import time
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .api import API

class Console():
    def __init__(self, sdcard_path, level=logging.ERROR, include_image=False, image_size=None):
        logging.basicConfig(format='%(asctime)s - [%(levelname)s] - %(message)s', level=level)
        self.logger = logging.getLogger(__name__)
        self.api = API(sdcard_path, include_image, image_size)
        self.controllers = []

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.logger.info('[libultimate] Cleaning up...')
        time.sleep(0.1)
        for controller in self.controllers:
            controller.release_all()
        self.logger.info('[libultimate] Done.')

    def add_controller(self, controller):
        controller.set_console(self)
        self.controllers.append(controller)

    def get_controller(self, player_id):
        for controller in self.controllers:
            if controller.player_id == player_id:
                return controller
        return None

    def stream(self, fps=1):
        hz = 60/fps
        current_frame_hz_num = 0
        while True:
            try:
                time.sleep(0.01)
                gamestate = self.api.read_state()
                frame_hz_num = gamestate.frame_count // hz
                if current_frame_hz_num != frame_hz_num:
                    current_frame_hz_num = frame_hz_num
                    yield gamestate
            except Exception as err:
                self.logger.warning("couldn't read state: {}".format(err))
