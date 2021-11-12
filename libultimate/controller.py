from contextlib import ExitStack
from typing import List
import pyautogui
from .enums import Action
import time
import yuzulib as yuzu

class Controller(yuzu.Controller):
    def __init__(self):
        super(Controller, self).__init__()
        self._hold_buttons = []

    def act(self, action: Action, sec=None):
        button_list = action.value
        self.multi_press(button_list)

    def to_mode(self, mode):
        mode.setup(self)

if __name__ == '__main__':
    controller = Controller()
    controller.act(Action.ACTION_JAB)