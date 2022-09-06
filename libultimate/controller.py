import string
from .enums import Action
from .console import Console
from typing import NamedTuple
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

    def act(self, player_id: int, action: Action, stick_x: float=0, stick_y: float=0):
        command: Command = {
            "id": str(uuid.uuid4()),
            "player_id": player_id,
            "action": action,
            "stick_x": stick_x,
            "stick_y": stick_y,
        }
        self.console.api.send_command(player_id, command)
