import string
from .enums import Action
from .console import Console
from typing import NamedTuple, Tuple
import uuid

class Command(NamedTuple):
    id: str
    player_id: int
    action: Action
    stick_x: float
    stick_y: float

class ControlState(NamedTuple):
    update_count: str
    buttons: int
    l_stick_x: Action
    l_stick_y: float
    r_stick_x: float
    r_stick_y: int
    flags: Action
    l_trigger: float
    r_trigger: float

class UltimateController:
    def __init__(self, console: Console):
        self.console = console

    def act(self, player_id: int, action: Action = Action.NONE, main_stick = (0, 0)):
        command: Command = {
            "id": str(uuid.uuid4()),
            "player_id": player_id,
            "action": action,
            "stick_x": main_stick[0],
            "stick_y": main_stick[1],
        }
        self.console.api.send_command(player_id, command)

    def act2(self, player_id: int, l_stick = (0, 0), r_stick = (0, 0), l_trigger = 0, r_trigger = 0, buttons = 0, flags = 0):
        control_state: ControlState = {
            "update_count": 0,
            "buttons": 0,
            "l_stick_x": l_stick[0],
            "l_stick_y": l_stick[1],
            "r_stick_x": r_stick[0],
            "r_stick_y": r_stick[1],
            "flags": flags,
            "l_trigger": l_trigger,
            "r_trigger": r_trigger,
        }
        self.console.api.send_control_state(player_id, control_state)
