from enum import Enum
from yuzulib import Button
class Action:
    """A single button on a PRO controller"""
    ACTION_JAB = [Button.BUTTON_A]
    ACTION_RIGHT_TILT = [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT, Button.BUTTON_A]
    ACTION_LEFT_TILT = [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT, Button.BUTTON_A]
    ACTION_UP_TILT = [Button.BUTTON_MODIFIER, Button.BUTTON_S_UP, Button.BUTTON_A]
    ACTION_DOWN_TILT = [Button.BUTTON_MODIFIER, Button.BUTTON_S_DOWN, Button.BUTTON_A]
    ACTION_RIGHT_SMASH = [Button.BUTTON_S_RIGHT, Button.BUTTON_A]
    ACTION_LEFT_SMASH = [Button.BUTTON_S_LEFT, Button.BUTTON_A]
    ACTION_UP_SMASH = [Button.BUTTON_S_UP, Button.BUTTON_A]
    ACTION_DOWN_SMASH = [Button.BUTTON_S_DOWN, Button.BUTTON_A]
    ACTION_NEUTRAL_SPECIAL = [Button.BUTTON_B]
    ACTION_RIGHT_SPECIAL = [Button.BUTTON_S_RIGHT, Button.BUTTON_B]
    ACTION_LEFT_SPECIAL = [Button.BUTTON_S_LEFT, Button.BUTTON_B]
    ACTION_UP_SPECIAL = [Button.BUTTON_S_UP, Button.BUTTON_B]
    ACTION_DOWN_SPECIAL = [Button.BUTTON_S_DOWN, Button.BUTTON_B]
    ACTION_GRAB = [Button.BUTTON_ZR]
    ACTION_SHIELD = [Button.BUTTON_R]
    ACTION_JAMP = [Button.BUTTON_Y]
    ACTION_SHORT_HOP = [Button.BUTTON_Y, Button.BUTTON_X]
    ACTION_UP_TAUNT = [Button.BUTTON_D_UP]
    ACTION_DOWN_TAUNT = [Button.BUTTON_D_DOWN]
    ACTION_LEFT_TAUNT = [Button.BUTTON_D_LEFT]
    ACTION_RIGHT_TAUNT = [Button.BUTTON_D_RIGHT]
    ACTION_SPOT_DODGE = [Button.BUTTON_R, Button.BUTTON_S_DOWN]
    ACTION_RIGHT_ROLL = [Button.BUTTON_R, Button.BUTTON_S_RIGHT]
    ACTION_LEFT_ROLL = [Button.BUTTON_R, Button.BUTTON_S_LEFT]
    ACTION_RIGHT_DASH = [Button.BUTTON_A_RIGHT]
    ACTION_LEFT_DASH = [Button.BUTTON_A_LEFT]
    ACTION_RIGHT_WALK = [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT]
    ACTION_LEFT_WALK = [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT]
    ACTION_CROUCH = [Button.BUTTON_S_DOWN]
    ACTION_RIGHT_CRAWL = [Button.BUTTON_S_DOWN, Button.BUTTON_S_RIGHT]
    ACTION_LEFT_CRAWL = [Button.BUTTON_S_DOWN, Button.BUTTON_S_LEFT]
    ACTION_RIGHT_STICK = [Button.BUTTON_S_RIGHT]
    ACTION_LEFT_STICK = [Button.BUTTON_S_LEFT]
    ACTION_UP_STICK = [Button.BUTTON_S_UP]
    ACTION_DOWN_STICK = [Button.BUTTON_S_DOWN]
    ACTION_NO_OPERATION = []
    
class Stage(Enum):
    STAGE_BATTLE_FIELD="1"
    STAGE_FINAL_DESTINATION="3"
    STAGE_POKEMON_STADIUM2="40"
    STAGE_SMASH_VILLE="44"
    STAGE_TOWN_AND_CITY="85"

class Fighter(Enum):
    FIGHTER_MARIO="0"
    FIGHTER_DONKEY_KONG="1"
    FIGHTER_LINK="2"
    FIGHTER_SAMUS="3"
    FIGHTER_YOSHI="4"
    FIGHTER_KIRBY="5"
    FIGHTER_FOX="6"

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
        # To Training from Games & More
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
        controller.press(Button.BUTTON_PLUS)








