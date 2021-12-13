from enum import Enum
from yuzulib import Button
from .enums import Action, Stage, Fighter
from .controller import Controller
import time
class Mode:
    def __init__(self):
        pass

class TrainingMode(Mode):
    def __init__(self, controller: Controller, stage: Stage, player: Fighter, cpu: Fighter, cpu_level=9):
        super(TrainingMode, self).__init__()
        self._player = player
        self._cpu = cpu
        self._cpu_level = cpu_level
        self._stage = stage
        self._controller = controller

    def start(self):
        print("Starting Training Mode")
        self._move_to_training_mode()
        self._select_stage()
        self._select_player()
        self._select_cpu()
        self._change_cpu_level()
        self._start_training()
        self._set_training_setting()
        self.reset()

    def _move_to_training_mode(self):
        print("Moving to training mode")
        # To Games & More from Home
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_UP], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)

        # To Training from Games & More
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(10) # Loading

    def _select_stage(self):
        print("Selecting Stage: {}".format(self._stage.name))
        # Stage Select
        stage_num = self._stage.value
        stage_row = stage_num%11
        stage_line = int(stage_num/11)
        for i in range(stage_line):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.20, wait=0.30)
            time.sleep(0.3)
        for k in range(stage_row):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.23, wait=0.30)
            time.sleep(0.3)
        # to Final Destination
        self._controller.press([Button.BUTTON_X], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_X], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(10) # Loading

    def _select_player(self):
        print("Selecting Player: {}".format(self._player.name))
        ## Player Select
        ### to left top corner
        self._controller.press([Button.BUTTON_S_UP], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=3, wait=3)
        time.sleep(0.1)
        ### to mario
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.25, wait=0.25)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
        time.sleep(0.1)
        ### to fighter
        player_num = self._player.value
        player_row = player_num%7
        player_line = int(player_num/7)
        for i in range(player_line):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
            time.sleep(0.1)
        for k in range(player_row):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.37, wait=1)
            time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)

    def _select_cpu(self):
        print("Selecting Cpu: {}".format(self._cpu.name))
        ## Move CPU
        ### to right top corner
        self._controller.press([Button.BUTTON_S_UP], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_RIGHT], sec=3, wait=3)
        time.sleep(0.1)
        ### to random
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.25, wait=0.25)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.60, wait=1)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        ## Select CPU
        ### to left top corner
        self._controller.press([Button.BUTTON_S_UP], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=3, wait=3)
        time.sleep(0.1)
        ### to mario
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.25, wait=0.25)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
        time.sleep(0.1)
        ### to fighter
        cpu_num = self._cpu.value
        cpu_row = cpu_num%7
        cpu_line = int(cpu_num/7)
        for i in range(cpu_line):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
            time.sleep(0.1)
        for k in range(cpu_row):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.37, wait=1)
            time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)

    def _change_cpu_level(self):
        print("Change Cpu Level: {}".format(self._cpu_level))
        # CPU LEVEL
        ### to right bottom corner
        self._controller.press([Button.BUTTON_S_DOWN], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_RIGHT], sec=3, wait=3)
        time.sleep(0.1)
        ### to level
        self._controller.press([Button.BUTTON_S_UP], sec=0.2, wait=0.2)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.5, wait=1)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02, wait=0.02)
        ### Change Level
        if self._cpu_level >= 3:
            for i in range(self._cpu_level - 3):
                self._controller.press([Button.BUTTON_S_UP], sec=0.2, wait=0.2)
                time.sleep(0.1)
        else:
            for i in range(3 - self._cpu_level):
                self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
                time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02, wait=0.02)
        time.sleep(1)

    def _start_training(self):
        ### Start Training Mode
        self._controller.press([Button.BUTTON_PLUS], sec=0.02, wait=0.02)
        time.sleep(15) # Loading
        print("Start Training")


    def _set_training_setting(self):
        print("Set Training Setting")
        # Change Settings
        self._controller.press([Button.BUTTON_PLUS], sec=0.02)
        time.sleep(0.5)
        ## Change CPU Behavior
        for i in range(4):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
            time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.2, wait=0.2)
        time.sleep(0.1)

        ## Other Settings
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(0.5)
        ## Speed Quick Mode
        for i in range(5):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.2, wait=0.2)
            time.sleep(0.1)
        ## Not Display Combo
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.2, wait=0.2)
        time.sleep(0.1)
        # Finish Settings
        self._controller.press([Button.BUTTON_PLUS], sec=0.02)
        time.sleep(1)

    def reset(self):
        #print("Reset Training")
        self._controller.press([Button.BUTTON_L, Button.BUTTON_R, Button.BUTTON_A], sec=0.02)
        time.sleep(0.1)


        










