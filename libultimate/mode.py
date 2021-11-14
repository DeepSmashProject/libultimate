from enum import Enum
from yuzulib import Button
from .enums import Action, Stage, Fighter
import time
class Mode:
    def __init__(self):
        pass

class TrainingMode(Mode):
    def __init__(self, stage: Stage, player: Fighter, cpu: Fighter, cpu_level=9):
        super(TrainingMode, self).__init__()
        self._player = player
        self._cpu = cpu
        self._cpu_level = cpu_level
        self._stage = stage

    def setup(self, controller):
        # To Games & More from Home
        controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.02)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_UP], sec=0.02)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)

        # To Training from Games & More
        controller.multi_press([Button.BUTTON_S_DOWN], sec=0.02)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_LEFT], sec=0.02)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)
        
        # Stage Select
        print("STAGE: {}".format(self._stage.name))
        stage_num = self._stage.value
        stage_row = stage_num%11
        stage_line = int(stage_num/11)
        print(stage_line, stage_row)
        for i in range(stage_line):
            controller.multi_press([Button.BUTTON_S_DOWN], sec=0.21)
            time.sleep(0.1)
        for k in range(stage_row):
            controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.23)
            time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        time.sleep(1.5)
        # Fighter Select
        ## Player Select
        ### to left top corner
        controller.multi_press([Button.BUTTON_S_UP], sec=2)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_LEFT], sec=1)
        time.sleep(0.1)
        ### to mario
        controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.25)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_DOWN], sec=0.30)
        time.sleep(0.1)
        ### to fighter
        player_num = self._player.value
        player_row = player_num%7
        player_line = int(player_num/7)
        for i in range(player_line):
            controller.multi_press([Button.BUTTON_S_DOWN], sec=0.30)
            time.sleep(0.1)
        for k in range(player_row):
            controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.37)
            time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)

        ## CPU Select
        ## Move CPU
        ### to right top corner
        controller.multi_press([Button.BUTTON_S_UP], sec=2)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_RIGHT], sec=3)
        time.sleep(0.1)
        ### to random
        controller.multi_press([Button.BUTTON_S_LEFT], sec=0.25)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_DOWN], sec=0.60)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        ## Select CPU
        ### to left top corner
        controller.multi_press([Button.BUTTON_S_UP], sec=3)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_LEFT], sec=3)
        time.sleep(0.1)
        ### to mario
        controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.25)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_DOWN], sec=0.30)
        time.sleep(0.1)
        ### to fighter
        cpu_num = self._cpu.value
        cpu_row = cpu_num%7
        cpu_line = int(cpu_num/7)
        for i in range(cpu_line):
            controller.multi_press([Button.BUTTON_S_DOWN], sec=0.30)
            time.sleep(0.1)
        for k in range(cpu_row):
            controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.37)
            time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)

        # CPU LEVEL
        ### to right bottom corner
        controller.multi_press([Button.BUTTON_S_DOWN], sec=3)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_RIGHT], sec=3)
        time.sleep(0.1)
        ### to level
        controller.multi_press([Button.BUTTON_S_UP], sec=0.2)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_LEFT], sec=0.5)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        ### Change Level
        if self._cpu_level >= 3:
            for i in range(self._cpu_level - 3):
                controller.multi_press([Button.BUTTON_S_UP], sec=0.2)
                time.sleep(0.1)
        else:
            for i in range(3 - self._cpu_level):
                controller.multi_press([Button.BUTTON_S_DOWN], sec=0.2)
                time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        time.sleep(0.1)

        ### Start Training Mode
        controller.multi_press([Button.BUTTON_PLUS], sec=0.02)
        
        time.sleep(5)
        # Change Settings
        controller.multi_press([Button.BUTTON_PLUS], sec=0.02)
        time.sleep(0.5)
        ## Change CPU Behavior
        for i in range(4):
            controller.multi_press([Button.BUTTON_S_DOWN], sec=0.2)
            time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.2)
        time.sleep(0.1)

        ## Other Settings
        controller.multi_press([Button.BUTTON_S_DOWN], sec=0.2)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_A], sec=0.02)
        time.sleep(0.5)
        ## Speed Quick Mode
        for i in range(5):
            controller.multi_press([Button.BUTTON_S_RIGHT], sec=0.2)
            time.sleep(0.1)
        ## Not Display Combo
        controller.multi_press([Button.BUTTON_S_DOWN], sec=0.2)
        time.sleep(0.1)
        controller.multi_press([Button.BUTTON_S_LEFT], sec=0.2)
        time.sleep(0.1)
        # Finish Settings
        controller.multi_press([Button.BUTTON_PLUS], sec=0.02)
        time.sleep(0.1)

        # Reset Position
        controller.multi_press([Button.BUTTON_L, Button.BUTTON_R, Button.BUTTON_A], sec=0.02)
        time.sleep(0.1)


        










