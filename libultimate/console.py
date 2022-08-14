import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .api import API

class Console():
    def __init__(self, ryujinx_path):
        self.ryujinx_path = ryujinx_path
        self.api = API(ryujinx_path)

    def run(self):
        pass

    def stream(self, hz=60):
        interval = hz * (1/60)
        while True:
            try:
                time.sleep(interval)
                yield self.api.read_state()
            except Exception as err:
                print("Warning: couldn't read state: {}".format(err))


if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "test")
    console = Console(RYUJINX_PATH)
    for game_state in console.stream(hz=5):
        print(game_state)
