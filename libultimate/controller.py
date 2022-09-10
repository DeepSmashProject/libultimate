import string
import time
from .enums import Button, Direction, Action
from .console import Console
from typing import NamedTuple, Tuple
import uuid

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

    def input(self, button: Button, main_stick = (0, 0), c_stick = (0, 0), l_trigger = 0, r_trigger = 0, flags = 0, hold = False):
        control_state: ControlState = {
            "id": str(uuid.uuid4()),
            "player_id": int(self.player_id),
            "update_count": int(0),
            "buttons": int(button.value),
            "l_stick_x": int(main_stick[0] * 32768), # Min: 0, Max: 0x7FFF
            "l_stick_y": int(main_stick[1] * 32768), # Min: 0, Max: -0x7FFF
            "r_stick_x": int(c_stick[0] * 32768), # Min: 0, Max: 0x7FFF
            "r_stick_y": int(c_stick[1] * 32768), # Min: 0, Max: 0x7FFF
            "flags": int(flags),
            "l_trigger": int(l_trigger),
            "r_trigger": int(r_trigger),
            "hold": hold,
        }
        self.console.api.send_control_state(self.player_id, control_state)

    def jab(self):
        self.input(Button.A)

    def tilt(self, direction: Direction):
        if direction== Direction.UP: self.input(Button.A, main_stick=(0, 0.5), hold=False)
        elif direction== Direction.UP_RIGHT: self.input(Button.A, main_stick=(0.5, 0.5), hold=False)
        elif direction== Direction.RIGHT: self.input(Button.A, main_stick=(0.5, 0), hold=False)
        elif direction== Direction.DOWN_RIGHT: self.input(Button.A, main_stick=(0.5, -0.5), hold=False)
        elif direction== Direction.DOWN: self.input(Button.A, main_stick=(0, -0.5), hold=False)
        elif direction== Direction.DOWN_LEFT: self.input(Button.A, main_stick=(-0.5, -0.5), hold=False)
        elif direction== Direction.LEFT: self.input(Button.A, main_stick=(-0.5, 0), hold=False)
        elif direction== Direction.UP_LEFT: self.input(Button.A, main_stick=(-0.5, 0.5), hold=False)

    def smash(self, direction: Direction):
        if direction== Direction.UP: self.input(Button.A, main_stick=(0, 1), hold=False)
        elif direction== Direction.UP_RIGHT: self.input(Button.A, main_stick=(1, 1), hold=False)
        elif direction== Direction.RIGHT: self.input(Button.A, main_stick=(1, 0), hold=False)
        elif direction== Direction.DOWN_RIGHT: self.input(Button.A, main_stick=(1, -1), hold=False)
        elif direction== Direction.DOWN: self.input(Button.A, main_stick=(0, -1), hold=False)
        elif direction== Direction.DOWN_LEFT: self.input(Button.A, main_stick=(-1, -1), hold=False)
        elif direction== Direction.LEFT: self.input(Button.A, main_stick=(-1, 0), hold=False)
        elif direction== Direction.UP_LEFT: self.input(Button.A, main_stick=(-1, 1), hold=False)

    def special(self, direction: Direction):
        if direction== Direction.NONE: self.input(Button.B, main_stick=(0, 0), hold=False)
        elif direction== Direction.UP: self.input(Button.B, main_stick=(0, 1), hold=False)
        elif direction== Direction.UP_RIGHT: self.input(Button.B, main_stick=(1, 1), hold=False)
        elif direction== Direction.RIGHT: self.input(Button.B, main_stick=(1, 0), hold=False)
        elif direction== Direction.DOWN_RIGHT: self.input(Button.B, main_stick=(1, -1), hold=False)
        elif direction== Direction.DOWN: self.input(Button.B, main_stick=(0, -1), hold=False)
        elif direction== Direction.DOWN_LEFT: self.input(Button.B, main_stick=(-1, -1), hold=False)
        elif direction== Direction.LEFT: self.input(Button.B, main_stick=(-1, 0), hold=False)
        elif direction== Direction.UP_LEFT: self.input(Button.B, main_stick=(-1, 1), hold=False)

    def dash_attack(self, lr: bool): # True = Right, False = Left
        if lr: 
            self.input(Button.NONE, main_stick=(1, 0), hold=True)
            time.sleep(0.2)
            self.input(Button.A, main_stick=(1, 0), hold=False)
        else:
            self.input(Button.NONE, main_stick=(-1, 0), hold=True)
            time.sleep(0.2)
            self.input(Button.A, main_stick=(-1, 0), hold=False)

    def guard(self):
        self.input(Button.ZL, hold=True)
    
    def grab(self):
        self.input(Button.L, hold=False)

    def spot_dodge(self):
        self.input(Button.ZL, main_stick=(0, -1), hold=False)

    def roll(self, lr: bool): # True = Right, False = Left
        if lr: self.input(Button.ZL, main_stick=(1, 0), hold=False)
        else: self.input(Button.ZL, main_stick=(-1, 0), hold=False)

    def jump(self, direction: Direction):
        if direction == Direction.NONE: self.input(Button.X, hold=True)
        elif direction == Direction.RIGHT: 
            self.input(Button.X, main_stick=(1, 0), hold=True)
            time.sleep(0.1)
            self.input(Button.NONE, main_stick=(1, 0), hold=True)
        elif direction == Direction.LEFT: 
            self.input(Button.X, main_stick=(-1, 0), hold=True)
            time.sleep(0.1)
            self.input(Button.NONE, main_stick=(-1, 0), hold=True)

    def short_hop(self, direction: Direction):
        if direction == Direction.NONE: self.input(Button.X, hold=False)
        elif direction == Direction.RIGHT: 
            self.input(Button.X, main_stick=(1, 0), hold=False)
            time.sleep(0.1)
            self.input(Button.NONE, main_stick=(1, 0), hold=True)
        elif direction == Direction.LEFT: 
            self.input(Button.X, main_stick=(-1, 0), hold=False)
            time.sleep(0.1)
            self.input(Button.NONE, main_stick=(-1, 0), hold=True)

    def walk(self, lr: bool): # True = Right, False = Left
        if lr: self.input(Button.NONE, main_stick=(0.5, 0), hold=True)
        else: self.input(Button.NONE, main_stick=(-0.5, 0), hold=True)

    def dash(self, lr: bool): # True = Right, False = Left
        if lr: self.input(Button.NONE, main_stick=(1, 0), hold=True)
        else: self.input(Button.NONE, main_stick=(-1, 0), hold=True)

    def taint(self, direction: Direction):
        if direction== Direction.UP: self.input(Button.D_PAD_UP, hold=True)
        elif direction== Direction.RIGHT: self.input(Button.D_PAD_RIGHT, hold=True)
        elif direction== Direction.DOWN: self.input(Button.D_PAD_DOWN, hold=True)
        elif direction== Direction.LEFT: self.input(Button.D_PAD_LEFT, hold=True)

    def release_all(self):
        self.input(Button.NONE)

class Command(NamedTuple):
    id: str
    player_id: int
    action: Action
    stick_x: float
    stick_y: float
    hold: bool

class ActionController:
    def __init__(self, player_id: int):
        self.player_id = player_id

    def set_console(self, console: Console):
        self.console = console

    def act(self, action: Action, main_stick = (0, 0), hold=False):
        command: Command = {
            "id": str(uuid.uuid4()),
            "player_id": self.player_id,
            "action": action,
            "stick_x": main_stick[0],
            "stick_y": main_stick[1],
            "hold": hold,
        }
        self.console.api.send_command(self.player_id, command)
