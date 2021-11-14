from enum import Enum
from yuzulib import Button
from .enums import Action, Stage, Fighter

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
        controller.press(Button.BUTTON_C_RIGHT)
        controller.press(Button.BUTTON_C_UP)
        controller.press(Button.BUTTON_A)
        '''# To Training from Games & More
        controller.press(Button.BUTTON_C_DOWN)
        controller.press(Button.BUTTON_C_LEFT)
        controller.press(Button.BUTTON_A)
        # Stage Select
        stage_num = self._stage.value
        stage_row = stage_num%11
        stage_line = int(stage_num/11)
        for i in range(stage_line):
            controller.press(Button.BUTTON_C_DOWN, sec=0.5)
        for k in range(stage_row):
            controller.press(Button.BUTTON_C_RIGHT, sec=0.5)
        controller.press(Button.BUTTON_A)
        # Fighter Select
        ## Player Select
        player_num = self._player.value
        player_row = player_num%7
        player_line = int(player_num/7)
        for i in range(player_line):
            controller.press(Button.BUTTON_C_DOWN, sec=1)
        for k in range(player_row):
            controller.press(Button.BUTTON_C_RIGHT, sec=1)
        controller.press(Button.BUTTON_A)
        ## CPU Select
        ### CPU Pick
        controller.press(Button.BUTTON_C_RIGHT, sec=1.5)
        controller.press(Button.BUTTON_C_DOWN, sec=1)
        controller.press(Button.BUTTON_B)
        ### Move
        cpu_num = self._cpu.value
        cpu_row = cpu_num%7
        cpu_line = int(cpu_num/7)
        for i in range(7-cpu_line):
            controller.press(Button.BUTTON_C_UP, sec=1)
        for k in range(7-cpu_row):
            controller.press(Button.BUTTON_C_LEFT, sec=1)
        controller.press(Button.BUTTON_A)
        ## CPU Level Select
        ### Top CPU Level
        controller.press(Button.BUTTON_C_RIGHT, sec=3)
        controller.press(Button.BUTTON_C_DOWN, sec=3)
        controller.press(Button.BUTTON_C_UP, sec=1)
        controller.press(Button.BUTTON_C_LEFT, sec=1)
        controller.press(Button.BUTTON_A)
        ### Change Level
        if self._cpu_level >= 3:
            for i in range(self._cpu_level - 3):
                controller.press(Button.BUTTON_C_UP)
        else:
            for i in range(3 - self._cpu_level):
                controller.press(Button.BUTTON_C_DOWN)
        controller.press(Button.BUTTON_A)
        # Start
        controller.press(Button.BUTTON_PLUS)'''








