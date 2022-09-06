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


class UltimateController:
    def __init__(self, console: Console):
        self.console = console

    def act(self, player_id: int, action: Action, main_stick = (0, 0)):
        command: Command = {
            "id": str(uuid.uuid4()),
            "player_id": player_id,
            "action": action,
            "stick_x": main_stick[0],
            "stick_y": main_stick[1],
        }
        self.console.api.send_command(player_id, command)
