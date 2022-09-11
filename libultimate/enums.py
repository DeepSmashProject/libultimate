from enum import Enum

class Stage(Enum):
    STAGE_BATTLE_FIELD=1
    STAGE_FINAL_DESTINATION=4
    STAGE_POKEMON_STADIUM2=41
    STAGE_SMASH_VILLE=45
    STAGE_HANENBOW=55
    STAGE_TOWN_AND_CITY=86

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

class Direction(Enum):
    NONE = 0
    UP = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN = 5
    DOWN_LEFT = 6
    LEFT = 7
    UP_LEFT = 8

class Button(Enum):
    NONE = 0
    A = 1
    B = 2
    X = 4
    Y = 8
    MAIN_STICK_BUTTON = 16
    C_STICK_BUTTON = 32
    L = 64
    R = 128
    ZL = 256
    ZR = 512
    PLUS = 1024
    MINUS = 2048
    D_PAD_LEFT = 4096
    D_PAD_UP = 8192
    D_PAD_RIGHT = 16384
    D_PAD_DOWN = 32768
    MAIN_STICK_LEFT = 65536
    MAIN_STICK_UP = 131072
    MAIN_STICK_RIGHT = 262144
    MAIN_STICK_DOWN = 524288
    C_STICK_LEFT = 1048576
    C_STICK_UP = 2097152
    C_STICK_RIGHT = 4194304
    C_STICK_DOWN = 8388608

class Action(str, Enum):
    TILT_U = "TILT_U"
    TILT_D = "TILT_D"
    TILT_F = "TILT_F"
    SMASH_U = "SMASH_U"
    SMASH_D = "SMASH_D"
    SMASH_F = "SMASH_F"
    JAB = "JAB"
    GRAB = "GRAB"
    DASH = "DASH"
    AIR_DODGE = "AIR_DODGE"
    SPOT_DODGE = "SPOT_DODGE"
    ROLL_B = "ROLL_B"
    ROLL_F = "ROLL_F"
    JUMP = "JUMP"
    SPECIAL_U = "SPECIAL_U"
    SPECIAL_D = "SPECIAL_D"
    SPECIAL_N = "SPECIAL_N"
    SPECIAL_F = "SPECIAL_F"
    TURN = "TURN"
    TURN_DASH = "TURN_DASH"
    WALK = "WALK"
    GUARD = "GUARD"
    THROW_B = "THROW_B"
    THROW_F = "THROW_F"
    THROW_U = "THROW_U"
    THROW_D = "THROW_D"
    DASH_ATTACK = "DASH_ATTACK"
    NONE = "NONE"
