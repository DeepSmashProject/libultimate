from contextlib import ExitStack
from typing import List
import pyautogui
from .enums import Action
from .mode import Mode
import time
import yuzulib as yuzu

class Controller(yuzu.Controller):
    def __init__(self):
        super(Controller, self).__init__()
        self._hold_buttons = []

    def act(self, action: Action, hold=True, sec=None):
        button_list = action
        self.multi_press(button_list, sec=0.02)

    def mode(self, mode: Mode):
        # mode: "training" only
        mode.setup(self)

if __name__ == '__main__':
    controller = Controller()
    controller.act(Action.ACTION_JAB)