import string
import time
from .enums import Button, Direction, Action
from .console import Console
from .schemas import ControlState
from typing import List, NamedTuple, Tuple
import uuid

class Controller:
    def __init__(self, player_id: int):
        self.player_id = player_id

    def set_console(self, console: Console):
        self.console = console

    def input(self, buttons: List[Button], main_stick = (0, 0), c_stick = (0, 0), hold = False):
        buttons_total = int(sum([btn.value for btn in buttons]))
        control_state = ControlState(
            id=str(uuid.uuid4()),
            player_id=int(self.player_id),
            update_count=int(0),
            buttons=buttons_total,
            l_stick_x=int(main_stick[0] * 32768), # Min: 0, Max: 0x7FFF
            l_stick_y=int(main_stick[1] * 32768), # Min: 0, Max: -0x7FFF
            r_stick_x=int(c_stick[0] * 32768), # Min: 0, Max: 0x7FFF
            r_stick_y=int(c_stick[1] * 32768), # Min: 0, Max: 0x7FFF
            flags=int(0),
            l_trigger=int(0),
            r_trigger=int(0),
            hold=hold,
        )
        self.console.api.send_control_state(self.player_id, control_state)

    def jab(self):
        self.input([Button.A])

    def tilt(self, direction: Direction):
        if direction== Direction.UP: self.input([Button.A], main_stick=(0, 0.5), hold=False)
        elif direction== Direction.UP_RIGHT: self.input([Button.A], main_stick=(0.5, 0.5), hold=False)
        elif direction== Direction.RIGHT: self.input([Button.A], main_stick=(0.5, 0), hold=False)
        elif direction== Direction.DOWN_RIGHT: self.input([Button.A], main_stick=(0.5, -0.5), hold=False)
        elif direction== Direction.DOWN: self.input([Button.A], main_stick=(0, -0.5), hold=False)
        elif direction== Direction.DOWN_LEFT: self.input([Button.A], main_stick=(-0.5, -0.5), hold=False)
        elif direction== Direction.LEFT: self.input([Button.A], main_stick=(-0.5, 0), hold=False)
        elif direction== Direction.UP_LEFT: self.input([Button.A], main_stick=(-0.5, 0.5), hold=False)

    def smash(self, direction: Direction):
        if direction== Direction.UP: self.input([Button.A], main_stick=(0, 1), hold=False)
        elif direction== Direction.UP_RIGHT: self.input([Button.A], main_stick=(1, 1), hold=False)
        elif direction== Direction.RIGHT: self.input([Button.A], main_stick=(1, 0), hold=False)
        elif direction== Direction.DOWN_RIGHT: self.input([Button.A], main_stick=(1, -1), hold=False)
        elif direction== Direction.DOWN: self.input([Button.A], main_stick=(0, -1), hold=False)
        elif direction== Direction.DOWN_LEFT: self.input([Button.A], main_stick=(-1, -1), hold=False)
        elif direction== Direction.LEFT: self.input([Button.A], main_stick=(-1, 0), hold=False)
        elif direction== Direction.UP_LEFT: self.input([Button.A], main_stick=(-1, 1), hold=False)

    def special(self, direction: Direction):
        if direction== Direction.NONE: self.input([Button.B], main_stick=(0, 0), hold=False)
        elif direction== Direction.UP: self.input([Button.B], main_stick=(0, 1), hold=False)
        elif direction== Direction.UP_RIGHT: self.input([Button.B], main_stick=(1, 1), hold=False)
        elif direction== Direction.RIGHT: self.input([Button.B], main_stick=(1, 0), hold=False)
        elif direction== Direction.DOWN_RIGHT: self.input([Button.B], main_stick=(1, -1), hold=False)
        elif direction== Direction.DOWN: self.input([Button.B], main_stick=(0, -1), hold=False)
        elif direction== Direction.DOWN_LEFT: self.input([Button.B], main_stick=(-1, -1), hold=False)
        elif direction== Direction.LEFT: self.input([Button.B], main_stick=(-1, 0), hold=False)
        elif direction== Direction.UP_LEFT: self.input([Button.B], main_stick=(-1, 1), hold=False)

    def dash_attack(self, lr: bool): # True = Right, False = Left
        if lr: 
            self.input([Button.NONE], main_stick=(1, 0), hold=True)
            time.sleep(0.2)
            self.input([Button.A], main_stick=(1, 0), hold=False)
        else:
            self.input([Button.NONE], main_stick=(-1, 0), hold=True)
            time.sleep(0.2)
            self.input([Button.A], main_stick=(-1, 0), hold=False)

    def guard(self):
        self.input([Button.ZL], hold=True)
    
    def grab(self):
        self.input([Button.L], hold=False)

    def spot_dodge(self):
        self.input([Button.ZL], main_stick=(0, -1), hold=False)

    def roll(self, lr: bool): # True = Right, False = Left
        if lr: self.input([Button.ZL], main_stick=(1, 0), hold=False)
        else: self.input([Button.ZL], main_stick=(-1, 0), hold=False)

    def jump(self, lr=None): # True = Right, False = Left
        if lr == None: 
            self.input([Button.NONE], main_stick=(0, 0), hold=True)
            time.sleep(0.05)
            self.input([Button.X], hold=True)
        elif lr: 
            self.input([Button.NONE], main_stick=(0, 0), hold=True)
            time.sleep(0.05)
            self.input([Button.X], main_stick=(1, 0), hold=True)
        elif not lr: 
            self.input([Button.NONE], main_stick=(0, 0), hold=True)
            time.sleep(0.05)
            self.input([Button.X], main_stick=(-1, 0), hold=True)

    def short_hop(self, lr=None):
        if lr == None: 
            self.input([Button.NONE], main_stick=(0, 0), hold=True)
            time.sleep(0.05)
            self.input([Button.X, Button.Y], hold=True)
        elif lr: 
            self.input([Button.NONE], main_stick=(0, 0), hold=True)
            time.sleep(0.05)
            self.input([Button.X, Button.Y], main_stick=(1, 0), hold=True)
        elif not lr: 
            self.input([Button.NONE], main_stick=(0, 0), hold=True)
            time.sleep(0.05)
            self.input([Button.X, Button.Y], main_stick=(-1, 0), hold=True)

    def walk(self, lr: bool): # True = Right, False = Left
        if lr: self.input([Button.NONE], main_stick=(0.5, 0), hold=True)
        else: self.input([Button.NONE], main_stick=(-0.5, 0), hold=True)

    def dash(self, lr: bool): # True = Right, False = Left
        if lr: self.input([Button.NONE], main_stick=(1, 0), hold=True)
        else: self.input([Button.NONE], main_stick=(-1, 0), hold=True)

    def taint(self, direction: Direction):
        if direction== Direction.UP: self.input([Button.D_PAD_UP], hold=True)
        elif direction== Direction.RIGHT: self.input([Button.D_PAD_RIGHT], hold=True)
        elif direction== Direction.DOWN: self.input([Button.D_PAD_DOWN], hold=True)
        elif direction== Direction.LEFT: self.input([Button.D_PAD_LEFT], hold=True)

    def release_all(self):
        self.input([Button.NONE])

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

    def release_all(self):
        pass
