import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .gamestate import GameState, toGameState
from .controller import Command

class API():
    def __init__(self, ryujinx_path: str):
        self.game_state_path = os.path.join(ryujinx_path, 'sdcard/libultimate/game_state.json')
        self.command_path = os.path.join(ryujinx_path, 'sdcard/libultimate/command.json')

    def read_state(self):
        with open(self.game_state_path, 'r') as f:
            text = f.read()
            gs_json = json.loads(text)
            game_state: GameState = toGameState(gs_json)
            return game_state

    def send_command(self, command: Command):
        with open(self.command_path, 'w') as f:
            json.dump(command, f)

