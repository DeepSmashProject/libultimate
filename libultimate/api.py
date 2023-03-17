import os
import sys
import json
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .schemas import ControlState, GameState
from pathlib import Path
from .util import capture

class API():
    def __init__(self, sdcard_path: str, include_image=False):
        self.libultimate_path = Path(sdcard_path).joinpath('libultimate').expanduser()
        self.logger = logging.getLogger(__name__)
        self.include_image = include_image
        # create libultimate folder
        self.create_root_dir()

    def create_root_dir(self):
        if not self.libultimate_path.exists():
            os.mkdir(self.libultimate_path)

    def read_state(self):
        game_state_path = Path(self.libultimate_path).joinpath('game_state.json').expanduser()
        with open(game_state_path, 'r') as f:
            text = f.read()
            gs_json = json.loads(text)
            game_state: GameState = GameState.parse_obj(gs_json)
            if self.include_image:
                game_state.image = capture()
            return game_state

    def send_command(self, player_id: int, command):
        command_path = Path(self.libultimate_path).joinpath('command_{}.json'.format(player_id)).expanduser()
        command_ok_path = Path(self.libultimate_path).joinpath('command_{}.ok.json'.format(player_id)).expanduser()
        if not os.path.isfile(command_ok_path):
            with open(command_path, 'w') as f:
                json.dump(command, f)
            # create ok file
            with open(command_ok_path, 'w') as f:
                pass
        else:
            self.logger.warning("command cannot sent.")

    def send_control_state(self, player_id: int, control_state: ControlState):
        control_state_path = Path(self.libultimate_path).joinpath('control_state_{}.json'.format(player_id)).expanduser()
        control_state_ok_path = Path(self.libultimate_path).joinpath('control_state_{}.ok.json'.format(player_id)).expanduser()
        if not os.path.isfile(control_state_ok_path):
            with open(control_state_path, 'w') as f:
                json.dump(control_state.dict(), f)
            # create ok file
            with open(control_state_ok_path, 'w') as f:
                pass
        else:
            self.logger.warning("control_state cannot sent.")

