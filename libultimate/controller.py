from contextlib import ExitStack
from typing import List
import pyautogui
from .enums import Action
from .mode import Mode
import time
import yuzulib as yuzu
import os
from pathlib import Path
from .util import click_mouse, press_key, move_mouse

class Controller(yuzu.Controller):
    def __init__(self):
        super(Controller, self).__init__()
        self._hold_buttons = []

    def act(self, action: Action, hold=True, sec=None):
        button_list = action
        self.multi_press(button_list, sec=0.02)

    def move_to_home(self):
        data_path = Path(os.path.dirname(__file__)).joinpath('/data/').resolve()
        path = str(data_path) + '/home.png'
        print(path)

        while True:
            time.sleep(1)
            res = pyautogui.locateOnScreen(path, confidence=.8)
            if res != None:
                print("Reached Home!")
                break
            else:
                self.multi_press([yuzu.Button.BUTTON_B], sec=0.02)
                time.sleep(0.1)
                self.multi_press([yuzu.Button.BUTTON_X], sec=0.02)

if __name__ == '__main__':
    controller = Controller()
    controller.act(Action.ACTION_JAB)