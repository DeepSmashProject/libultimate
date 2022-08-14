import os
import sys
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from gamestate import GameState
from utils import create_namedtuple_from_dict

class API():
    def __init__(self, RYUJINX_DIR: str):
        self.game_state_path = os.path.join(RYUJINX_DIR, 'sdcard/game_state.json')

    def read_state(self, callback, hz=60):
        interval = hz * (1/60)
        while True:
            time.sleep(interval)
            try:
                with open(self.game_state_path, 'r') as f:
                    text = f.read()
                    gs_json = json.loads(text)
                    game_state: GameState = create_namedtuple_from_dict("GameState", gs_json)
                    callback(game_state)
            except Exception as err:
                print("Warning: couldn't read state: {}".format(err))

    def send_control(self):
        pass



if __name__ == "__main__":
    def callback(game_state):
        print(game_state)

    RYUJINX_DIR = os.path.join(os.path.dirname(__file__), "test")
    api = API(RYUJINX_DIR)
    api.read_state(callback, hz=5)
