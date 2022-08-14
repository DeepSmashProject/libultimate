from enum import Enum

class Stage(Enum):
    """A VS-mode stage """
    NO_STAGE = 0
    FINAL_DESTINATION = 1
    BATTLEFIELD = 2
    POKEMON_STADIUM = 3
    DREAMLAND = 4
    FOUNTAIN_OF_DREAMS = 5
    YOSHIS_STORY = 6
    RANDOM_STAGE = 7

class Fighter(Enum):
    FIGHTER_MARIO = 0
    FIGHTER_DONKEY = 1
    FIGHTER_LINK = 2
    FIGHTER_SAMUS = 3
    FIGHTER_YOSHI = 4
    FIGHTER_KIRBY = 5
    FIGHTER_FOX = 6
    FIGHTER_PIKACHU = 7
    FIGHTER_LUIGI = 8
    FIGHTER_NESS = 9
    FIGHTER_CAPTAIN = 10
    FIGHTER_PURIN = 11
    FIGHTER_PEACH = 12
    FIGHTER_KOOPA = 13
    FIGHTER_POPO = 14
    FIGHTER_NANA = 15
    FIGHTER_SHEIK = 16
    FIGHTER_ZELDA = 17
    FIGHTER_MARIOD = 18
    FIGHTER_PICHU = 19
    FIGHTER_FALCO = 20
    FIGHTER_MARTH = 21
    FIGHTER_YOUNGLINK = 22
    FIGHTER_GANON = 23
    FIGHTER_MEWTWO = 24
    FIGHTER_ROY = 25
    FIGHTER_GAMEWATCH = 26
    FIGHTER_METAKNIGHT = 27
    FIGHTER_PIT = 28
    FIGHTER_SZEROSUIT = 29
    FIGHTER_WARIO = 30
    FIGHTER_SNAKE = 31
    FIGHTER_IKE = 32
    FIGHTER_PZENIGAME = 33
    FIGHTER_PFUSHIGISOU = 34
    FIGHTER_PLIZARDON = 35
    FIGHTER_DIDDY = 36
    FIGHTER_LUCAS = 37
    FIGHTER_SONIC = 38
    FIGHTER_DEDEDE = 39
    FIGHTER_PIKMIN = 40
    FIGHTER_LUCARIO = 41
    FIGHTER_ROBOT = 42
    FIGHTER_TOONLINK = 43
    FIGHTER_WOLF = 44
    FIGHTER_MURABITO = 45
    FIGHTER_ROCKMAN = 46
    FIGHTER_WIIFIT = 47
    FIGHTER_ROSETTA = 48
    FIGHTER_LITTLEMAC = 49
    FIGHTER_GEKKOUGA = 50
    FIGHTER_PALUTENA = 51
    FIGHTER_PACMAN = 52
    FIGHTER_REFLET = 53
    FIGHTER_SHULK = 54
    FIGHTER_KOOPAJR = 55
    FIGHTER_DUCKHUNT = 56
    FIGHTER_RYU = 57
    FIGHTER_CLOUD = 58
    FIGHTER_KAMUI = 59
    FIGHTER_BAYONETTA = 60
    FIGHTER_INKLING = 61
    FIGHTER_RIDLEY = 62
    FIGHTER_SIMON = 63
    FIGHTER_KROOL = 64
    FIGHTER_SHIZUE = 65
    FIGHTER_GAOGAEN = 66
    FIGHTER_PACKUN = 67
    FIGHTER_JACK = 68
    FIGHTER_BRAVE = 69
    FIGHTER_BUDDY = 70
    FIGHTER_DOLLY = 71
    FIGHTER_MASTER = 72
    FIGHTER_TANTAN = 73
    FIGHTER_PICKEL = 74
    FIGHTER_EDGE = 75
    FIGHTER_MIIFIGHTER = 76
    FIGHTER_MIISWORDSMAN = 77
    FIGHTER_MIIGUNNER = 78
    FIGHTER_SAMUSD = 79
    FIGHTER_DAISY = 80
    FIGHTER_LUCINA = 81
    FIGHTER_CHROM = 82
    FIGHTER_PITB = 83
    FIGHTER_KEN = 84
    FIGHTER_RICHTER = 85
    FIGHTER_KOOPAG = 86
    FIGHTER_MIIENEMYF = 87
    FIGHTER_MIIENEMYS = 88
    FIGHTER_MIIENEMYG = 89

class Button(Enum):
    """A single button on a PRO controller"""
    BUTTON_A = "z"
    BUTTON_B = "x"
    BUTTON_X = "c"
    BUTTON_Y = "v"
    BUTTON_ZL = "q"
    BUTTON_ZR = "o"
    BUTTON_L = "e"
    BUTTON_R = "u"
    BUTTON_D_UP = "up"
    BUTTON_D_DOWN = "down"
    BUTTON_D_LEFT = "left"
    BUTTON_D_RIGHT = "right"
    BUTTON_C_UP = "i"
    BUTTON_C_DOWN = "k"
    BUTTON_C_LEFT = "j"
    BUTTON_C_RIGHT = "l"
    BUTTON_S_UP = "w"
    BUTTON_S_DOWN = "s"
    BUTTON_S_LEFT = "a"
    BUTTON_S_RIGHT = "d"
    BUTTON_MODIFIER = "shift"

class Action:
    """A single button on a PRO controller"""
    ACTION_JAB = {"name": "ACTION_JAB", "buttons": [Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_TILT = {"name": "ACTION_RIGHT_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_TILT = {"name": "ACTION_LEFT_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_TILT = {"name": "ACTION_UP_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_UP, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_TILT = {"name": "ACTION_DOWN_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_DOWN, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_SMASH = {"name": "ACTION_RIGHT_SMASH", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_SMASH = {"name": "ACTION_LEFT_SMASH", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_SMASH = {"name": "ACTION_UP_SMASH", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_SMASH = {"name": "ACTION_DOWN_SMASH", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_NEUTRAL_SPECIAL = {"name": "ACTION_NEUTRAL_SPECIAL", "buttons": [Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_SPECIAL = {"name": "ACTION_RIGHT_SPECIAL", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_SPECIAL = {"name": "ACTION_LEFT_SPECIAL", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_SPECIAL = {"name": "ACTION_UP_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_RIGHT_SPECIAL = {"name": "ACTION_UP_RIGHT_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_S_RIGHT, Button.BUTTON_B], "hold": False, "sec": 0.05, "wait": 0.05, "refresh": False}
    ACTION_UP_LEFT_SPECIAL = {"name": "ACTION_UP_LEFT_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_S_LEFT, Button.BUTTON_B], "hold": False, "sec": 0.05, "wait": 0.05, "refresh": False}
    ACTION_DOWN_SPECIAL = {"name": "ACTION_DOWN_SPECIAL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_GRAB = {"name": "ACTION_GRAB", "buttons": [Button.BUTTON_R], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_SHIELD = {"name": "ACTION_SHIELD", "buttons": [Button.BUTTON_ZR], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_JUMP = {"name": "ACTION_JUMP", "buttons": [Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_RIGHT_JUMP = {"name": "ACTION_RIGHT_JUMP", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_LEFT_JUMP = {"name": "ACTION_LEFT_JUMP", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_SHORT_HOP = {"name": "ACTION_SHORT_HOP", "buttons": [Button.BUTTON_Y, Button.BUTTON_X], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_RIGHT_SHORT_HOP = {"name": "ACTION_RIGHT_SHORT_HOP", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_Y, Button.BUTTON_X], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_LEFT_SHORT_HOP = {"name": "ACTION_LEFT_SHORT_HOP", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_Y, Button.BUTTON_X], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_UP_TAUNT = {"name": "ACTION_UP_TAUNT", "buttons": [Button.BUTTON_D_UP], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_TAUNT = {"name": "ACTION_DOWN_TAUNT", "buttons": [Button.BUTTON_D_DOWN], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_TAUNT = {"name": "ACTION_LEFT_TAUNT", "buttons": [Button.BUTTON_D_LEFT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_TAUNT = {"name": "ACTION_RIGHT_TAUNT", "buttons": [Button.BUTTON_D_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_SPOT_DODGE = {"name": "ACTION_SPOT_DODGE", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_DOWN], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_ROLL = {"name": "ACTION_RIGHT_ROLL", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_ROLL = {"name": "ACTION_LEFT_ROLL", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_LEFT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_DASH = {"name": "ACTION_RIGHT_DASH", "buttons": [Button.BUTTON_S_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_DASH = {"name": "ACTION_LEFT_DASH", "buttons": [Button.BUTTON_S_LEFT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_WALK = {"name": "ACTION_RIGHT_WALK", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_WALK = {"name": "ACTION_LEFT_WALK", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_CROUCH = {"name": "ACTION_CROUCH", "buttons": [Button.BUTTON_S_DOWN], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_CRAWL = {"name": "ACTION_RIGHT_CRAWL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_CRAWL = {"name": "ACTION_LEFT_CRAWL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_STICK = {"name": "ACTION_RIGHT_STICK", "buttons": [Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_STICK = {"name": "ACTION_LEFT_STICK", "buttons": [Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_STICK = {"name": "ACTION_UP_STICK", "buttons": [Button.BUTTON_S_UP], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_STICK = {"name": "ACTION_DOWN_STICK", "buttons": [Button.BUTTON_S_DOWN], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_NO_OPERATION = {"name": "ACTION_NO_OPERATION", "buttons": [], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    