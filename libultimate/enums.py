from enum import Enum
from yuzulib.enums import Button
class Action:
    """A single button on a PRO controller"""
    ACTION_JAB = {"name": "ACTION_JAB", "buttons": [Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_TILT = {"name": "ACTION_RIGHT_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_TILT = {"name": "ACTION_LEFT_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_UP_TILT = {"name": "ACTION_UP_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_UP, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_DOWN_TILT = {"name": "ACTION_DOWN_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_DOWN, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_SMASH = {"name": "ACTION_RIGHT_SMASH", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_SMASH = {"name": "ACTION_LEFT_SMASH", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_UP_SMASH = {"name": "ACTION_UP_SMASH", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_DOWN_SMASH = {"name": "ACTION_DOWN_SMASH", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_NEUTRAL_SPECIAL = {"name": "ACTION_NEUTRAL_SPECIAL", "buttons": [Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_SPECIAL = {"name": "ACTION_RIGHT_SPECIAL", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_SPECIAL = {"name": "ACTION_LEFT_SPECIAL", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_UP_SPECIAL = {"name": "ACTION_UP_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_DOWN_SPECIAL = {"name": "ACTION_DOWN_SPECIAL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_GRAB = {"name": "ACTION_GRAB", "buttons": [Button.BUTTON_R], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_SHIELD = {"name": "ACTION_SHIELD", "buttons": [Button.BUTTON_ZR], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_JUMP = {"name": "ACTION_JUMP", "buttons": [Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_JUMP = {"name": "ACTION_RIGHT_JUMP", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_JUMP = {"name": "ACTION_LEFT_JUMP", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_SHORT_HOP = {"name": "ACTION_SHORT_HOP", "buttons": [Button.BUTTON_Y, Button.BUTTON_X], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_SHORT_HOP = {"name": "ACTION_RIGHT_SHORT_HOP", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_Y, Button.BUTTON_X], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_SHORT_HOP = {"name": "ACTION_LEFT_SHORT_HOP", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_Y, Button.BUTTON_X], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_UP_TAUNT = {"name": "ACTION_UP_TAUNT", "buttons": [Button.BUTTON_D_UP], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_DOWN_TAUNT = {"name": "ACTION_DOWN_TAUNT", "buttons": [Button.BUTTON_D_DOWN], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_TAUNT = {"name": "ACTION_LEFT_TAUNT", "buttons": [Button.BUTTON_D_LEFT], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_TAUNT = {"name": "ACTION_RIGHT_TAUNT", "buttons": [Button.BUTTON_D_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_SPOT_DODGE = {"name": "ACTION_SPOT_DODGE", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_DOWN], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_ROLL = {"name": "ACTION_RIGHT_ROLL", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_ROLL = {"name": "ACTION_LEFT_ROLL", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_LEFT], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_DASH = {"name": "ACTION_RIGHT_DASH", "buttons": [Button.BUTTON_S_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_DASH = {"name": "ACTION_LEFT_DASH", "buttons": [Button.BUTTON_S_LEFT], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_WALK = {"name": "ACTION_RIGHT_WALK", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_WALK = {"name": "ACTION_LEFT_WALK", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_CROUCH = {"name": "ACTION_CROUCH", "buttons": [Button.BUTTON_S_DOWN], "hold": False, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_CRAWL = {"name": "ACTION_RIGHT_CRAWL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_CRAWL = {"name": "ACTION_LEFT_CRAWL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_RIGHT_STICK = {"name": "ACTION_RIGHT_STICK", "buttons": [Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_LEFT_STICK = {"name": "ACTION_LEFT_STICK", "buttons": [Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_UP_STICK = {"name": "ACTION_UP_STICK", "buttons": [Button.BUTTON_S_UP], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_DOWN_STICK = {"name": "ACTION_DOWN_STICK", "buttons": [Button.BUTTON_S_DOWN], "hold": True, "sec": 0.02, "wait": 0.05,}
    ACTION_NO_OPERATION = {"name": "ACTION_NO_OPERATION", "buttons": [], "hold": False, "sec": 0.02, "wait": 0.05,}
    
class Stage(Enum):
    STAGE_BATTLE_FIELD=1
    STAGE_FINAL_DESTINATION=4
    STAGE_POKEMON_STADIUM2=41
    STAGE_SMASH_VILLE=45
    STAGE_HANENBOW=55
    STAGE_TOWN_AND_CITY=86

class Fighter(Enum):
    FIGHTER_MARIO=0
    FIGHTER_DONKEY_KONG=1
    FIGHTER_LINK=2
    FIGHTER_SAMUS=3
    FIGHTER_YOSHI=4
    FIGHTER_KIRBY=5
    FIGHTER_FOX=6

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








