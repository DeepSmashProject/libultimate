import string
import time
from .enums import Action, Button, Direction
from .console import Console
from typing import NamedTuple, Tuple
import uuid

class Command(NamedTuple):
    id: str
    player_id: int
    action: Action
    stick_x: float
    stick_y: float

class UltimateController_Old:
    def __init__(self, console: Console, player_id: int):
        self.console = console
        self.player_id = player_id

    def act(self, action: Action = Action.NONE, main_stick = (0, 0)):
        command: Command = {
            "id": str(uuid.uuid4()),
            "player_id": self.player_id,
            "action": action,
            "stick_x": main_stick[0],
            "stick_y": main_stick[1],
        }
        self.console.api.send_command(self.player_id, command)

class ControlState(NamedTuple):
    id: str
    player_id: int
    update_count: str
    buttons: int
    l_stick_x: int
    l_stick_y: int
    r_stick_x: int
    r_stick_y: int
    flags: int
    l_trigger: int
    r_trigger: int
    hold: bool

class Controller:
    def __init__(self, player_id: int):
        self.player_id = player_id

    def set_console(self, console: Console):
        self.console = console

    def act(self, button: Button, main_stick = (0, 0), c_stick = (0, 0), l_trigger = 0, r_trigger = 0, flags = 0, hold = False):
        control_state: ControlState = {
            "id": str(uuid.uuid4()),
            "player_id": self.player_id,
            "update_count": 0,
            "buttons": button.value,
            "l_stick_x": main_stick[0] * 32768, # Min: 0, Max: 0x7FFF
            "l_stick_y": main_stick[1] * 32768, # Min: 0, Max: -0x7FFF
            "r_stick_x": c_stick[0] * 32768, # Min: 0, Max: 0x7FFF
            "r_stick_y": c_stick[1] * 32768, # Min: 0, Max: 0x7FFF
            "flags": flags,
            "l_trigger": l_trigger,
            "r_trigger": r_trigger,
            "hold": hold,
        }
        self.console.api.send_control_state(self.player_id, control_state)

    def jab(self):
        self.act(Button.A)

    def tilt(self, direction: Direction):
        if direction== Direction.UP: self.act(Button.A, main_stick=(0, 0.5), hold=True)
        elif direction== Direction.UP_RIGHT: self.act(Button.A, main_stick=(0.5, 0.5), hold=True)
        elif direction== Direction.RIGHT: self.act(Button.A, main_stick=(0.5, 0), hold=True)
        elif direction== Direction.DOWN_RIGHT: self.act(Button.A, main_stick=(0.5, -0.5), hold=True)
        elif direction== Direction.DOWN: self.act(Button.A, main_stick=(0, -0.5), hold=True)
        elif direction== Direction.DOWN_LEFT: self.act(Button.A, main_stick=(-0.5, -0.5), hold=True)
        elif direction== Direction.LEFT: self.act(Button.A, main_stick=(-0.5, 0), hold=True)
        elif direction== Direction.UP_LEFT: self.act(Button.A, main_stick=(-0.5, 0.5), hold=True)

    def smash(self, direction: Direction):
        if direction== Direction.UP: self.act(Button.A, main_stick=(0, 1), hold=True)
        elif direction== Direction.UP_RIGHT: self.act(Button.A, main_stick=(1, 1), hold=True)
        elif direction== Direction.RIGHT: self.act(Button.A, main_stick=(1, 0), hold=True)
        elif direction== Direction.DOWN_RIGHT: self.act(Button.A, main_stick=(1, -1), hold=True)
        elif direction== Direction.DOWN: self.act(Button.A, main_stick=(0, -1), hold=True)
        elif direction== Direction.DOWN_LEFT: self.act(Button.A, main_stick=(-1, -1), hold=True)
        elif direction== Direction.LEFT: self.act(Button.A, main_stick=(-1, 0), hold=True)
        elif direction== Direction.UP_LEFT: self.act(Button.A, main_stick=(-1, 1), hold=True)

    def special(self, direction: Direction):
        if direction== Direction.NONE: self.act(Button.B, main_stick=(0, 0), hold=True)
        elif direction== Direction.UP: self.act(Button.B, main_stick=(0, 1), hold=True)
        elif direction== Direction.UP_RIGHT: self.act(Button.B, main_stick=(1, 1), hold=True)
        elif direction== Direction.RIGHT: self.act(Button.B, main_stick=(1, 0), hold=True)
        elif direction== Direction.DOWN_RIGHT: self.act(Button.B, main_stick=(1, -1), hold=True)
        elif direction== Direction.DOWN: self.act(Button.B, main_stick=(0, -1), hold=True)
        elif direction== Direction.DOWN_LEFT: self.act(Button.B, main_stick=(-1, -1), hold=True)
        elif direction== Direction.LEFT: self.act(Button.B, main_stick=(-1, 0), hold=True)
        elif direction== Direction.UP_LEFT: self.act(Button.B, main_stick=(-1, 1), hold=True)

    def dash_attack(self, lr: bool): # True = Right, False = Left
        if lr: 
            self.act(Button.NONE, main_stick=(1, 0), hold=True)
            time.sleep(0.2)
            self.act(Button.A, main_stick=(1, 0), hold=True)
        else:
            self.act(Button.NONE, main_stick=(-1, 0), hold=True)
            time.sleep(0.2)
            self.act(Button.A, main_stick=(-1, 0), hold=True)

    def guard(self):
        self.act(Button.ZL, hold=True)
    
    def grab(self):
        self.act(Button.L, hold=True)

    def spot_dodge(self):
        self.act(Button.ZL, main_stick=(0, -1), hold=True)

    def roll(self, lr: bool): # True = Right, False = Left
        if lr: self.act(Button.ZL, main_stick=(1, 0), hold=True)
        else: self.act(Button.ZL, main_stick=(-1, 0), hold=True)

    def jump(self, direction: Direction):
        if direction == Direction.NONE: self.act(Button.X, hold=True)
        elif direction == Direction.RIGHT: self.act(Button.X, main_stick=(1, 0), hold=True)
        elif direction == Direction.LEFT: self.act(Button.X, main_stick=(-1, 0), hold=True)

    def walk(self, lr: bool): # True = Right, False = Left
        if lr: self.act(Button.NONE, main_stick=(0.5, 0), hold=True)
        else: self.act(Button.NONE, main_stick=(-0.5, 0), hold=True)

    def dash(self, lr: bool): # True = Right, False = Left
        if lr: self.act(Button.NONE, main_stick=(1, 0), hold=True)
        else: self.act(Button.NONE, main_stick=(-1, 0), hold=True)

    def taint(self, direction: Direction):
        if direction== Direction.UP: self.act(Button.D_PAD_UP, hold=True)
        elif direction== Direction.RIGHT: self.act(Button.D_PAD_RIGHT, hold=True)
        elif direction== Direction.DOWN: self.act(Button.D_PAD_DOWN, hold=True)
        elif direction== Direction.LEFT: self.act(Button.D_PAD_LEFT, hold=True)

    def release_all(self):
        self.act(Button.NONE)
