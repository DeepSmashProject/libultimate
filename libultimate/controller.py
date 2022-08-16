import string
from .enums import Action
from .console import Console
from typing import NamedTuple
import uuid

class Command(NamedTuple):
    id: str
    player_id: int
    action: Action


class UltimateController:
    def __init__(self, console: Console):
        self.console = console

    def act(self, player_id: int, action: Action):
        command: Command = {
            "id": str(uuid.uuid4()),
            "player_id": player_id,
            "action": action
        }
        self.console.api.send_command(command)
