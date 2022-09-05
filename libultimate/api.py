import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .gamestate import GameState, toGameState

class API():
    def __init__(self, ryujinx_path: str):
        self.game_state_path = os.path.join(ryujinx_path, 'sdcard/libultimate/game_state.json')
        self.command_path = os.path.join(ryujinx_path, 'sdcard/libultimate/command.json')
        self.command_ok_path = os.path.join(ryujinx_path, 'sdcard/libultimate/command.ok.json')

    def read_state(self):
        with open(self.game_state_path, 'r') as f:
            text = f.read()
            gs_json = json.loads(text)
            game_state: GameState = toGameState(gs_json)
            return game_state

    def send_command(self, command):
        if not os.path.isfile(self.command_ok_path):
            with open(self.command_path, 'w') as f:
                json.dump(command, f)
            # create ok file
            with open(self.command_ok_path, 'w') as f:
                pass
        else:
            print("Warning: command not sent, previous command not acknowledged")

