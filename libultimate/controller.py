from .console import Console
from typing import NamedTuple, Tuple

class ControllerState(NamedTuple):
    button_a: bool = False
    button_b: bool = False
    button_x: bool = False
    button_y: bool = False
    button_l: bool = False
    button_r: bool = False
    button_z: bool = False
    button_zl: bool = False
    button_zr: bool = False
    button_d_up: bool = False
    button_d_down: bool = False
    button_d_left: bool = False
    button_d_right: bool = False
    main_stick: Tuple(float, float) = (0.5, 0.5)
    c_stick: Tuple(float, float) = (0.5, 0.5)

class Controller():
    def __init__(self, console: Console, port: int=1):
        self.console = console
        self.port = port

    def press(self):
        res = self.console.operateController()
        return res

    def release(self):
        res = self.console.operateController()
        return res

    def release_all(self):
        res = self.console.operateController()
        return res
        