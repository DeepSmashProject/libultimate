import os
import sys
import json
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .schemas import ControlState, GameState

class API():
    def __init__(self, ryujinx_path: str):
        self.ryujinx_path = ryujinx_path
        self.game_state_path = os.path.join(ryujinx_path, 'sdcard/libultimate/game_state.json')
        self.logger = logging.getLogger(__name__)

    def read_state(self):
        with open(self.game_state_path, 'r') as f:
            text = f.read()
            gs_json = json.loads(text)
            game_state: GameState = GameState.parse_obj(gs_json)
            return game_state

    def send_command(self, player_id: int, command):
        command_path = os.path.join(self.ryujinx_path, 'sdcard/libultimate/command_{}.json'.format(player_id))
        command_ok_path = os.path.join(self.ryujinx_path, 'sdcard/libultimate/command_{}.ok.json'.format(player_id))
        if not os.path.isfile(command_ok_path):
            with open(command_path, 'w') as f:
                json.dump(command, f)
            # create ok file
            with open(command_ok_path, 'w') as f:
                pass
        else:
            self.logger.warning("command cannot sent.")

    def send_control_state(self, player_id: int, control_state: ControlState):
        control_state_path = os.path.join(self.ryujinx_path, 'sdcard/libultimate/control_state_{}.json'.format(player_id))
        control_state_ok_path = os.path.join(self.ryujinx_path, 'sdcard/libultimate/control_state_{}.ok.json'.format(player_id))
        if not os.path.isfile(control_state_ok_path):
            with open(control_state_path, 'w') as f:
                json.dump(control_state.json(), f)
            # create ok file
            with open(control_state_ok_path, 'w') as f:
                pass
        else:
            self.logger.warning("control_state cannot sent.")

