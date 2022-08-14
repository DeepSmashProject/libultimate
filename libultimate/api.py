import os
import sys
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .gamestate import GameState
from .utils import create_namedtuple_from_dict

class API():
    def __init__(self, ryujinx_path: str):
        self.game_state_path = os.path.join(ryujinx_path, 'sdcard/game_state.json')

    def read_state(self):
        with open(self.game_state_path, 'r') as f:
            text = f.read()
            gs_json = json.loads(text)
            game_state: GameState = create_namedtuple_from_dict("GameState", gs_json)
            return game_state

    def send_command(self, command):
        pass



if __name__ == "__main__":
    RYUJINX_DIR = os.path.join(os.path.dirname(__file__), "test")
    api = API(RYUJINX_DIR)
    api.read_state()
