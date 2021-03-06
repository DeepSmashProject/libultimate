import pyautogui
from .enums import Action
import time
from yuzulib.controller import Controller
from yuzulib.enums import Button
import os
from pathlib import Path
from .mode import Action, TrainingMode, Stage, Fighter

class UltimateController(Controller):
    def __init__(self):
        super(UltimateController, self).__init__()
        self.training_mode = None

    def act(self, action: Action):
        buttons = action["buttons"]
        hold = action["hold"]
        sec = action["sec"]
        wait = action["wait"]
        refresh = action["refresh"]
        self.press(buttons, hold=hold, sec=sec, wait=wait, refresh=refresh)

    def move_to_home(self):
        data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()
        path = str(data_path) + '/home.png'
        print(path)

        while True:
            time.sleep(1)
            res = pyautogui.locateOnScreen(path, confidence=.8)
            if res != None:
                print("Reached Home!")
                break
            else:
                self.press([Button.BUTTON_X], sec=0.02)
                time.sleep(0.1)
                self.press([Button.BUTTON_B], sec=0.02)
                time.sleep(0.1)

    def move_to_training(self, config):
        self.training_mode = TrainingMode(
            controller=self,
            stage=Stage[config["stage"]], 
            player=Fighter[config["player"]["fighter"]],
            cpu=Fighter[config["cpu"]["fighter"]],
            cpu_level=config["cpu"]["level"],
        )
        self.training_mode.start()

    def reset_training(self):
        self.press([Button.BUTTON_L, Button.BUTTON_R, Button.BUTTON_A], sec=0.02)
        time.sleep(0.1)


if __name__ == '__main__':
    controller = UltimateController()
    controller.act(Action.ACTION_JAB)