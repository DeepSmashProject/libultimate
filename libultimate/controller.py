import string
from .enums import Action
from .console import Console
from typing import NamedTuple
import uuid

class Command(NamedTuple):
    id: string
    action: Action


class UltimateController:
    def __init__(self, console: Console):
        self.console = console

    def act(self, action: Action):
        command: Command = {
            id: uuid.uuid4(),
            action: action
        }
        self.console.api.send_command(command)
