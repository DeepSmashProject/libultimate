from typing import NamedTuple, List
from .enums import Fighter

class Position(NamedTuple):
    x: float = 0
    y: float = 0

class ControlState(NamedTuple):
    stick_x: float
    stick_y: float
    button_attack: bool
    button_special: bool
    button_smash: bool
    button_guard: bool
    button_guard_hold: bool
    button_catch: bool
    button_jump: bool
    button_jump_mini: bool
    button_invalid: bool

class PlayerState(NamedTuple):
    id: int
    fighter_kind: Fighter
    fighter_status_kind: int
    situation_kind: int
    lr: float
    percent: float
    position: Position
    #charge: float
    control_state: ControlState
    is_cpu: bool
    is_dead: bool

class Projectile(NamedTuple):
    position: Position

class GameState(NamedTuple):
    players: List[PlayerState]
    projectiles: List[Projectile]

def toGameState(gs_json):
    players = []
    for p in gs_json["players"]:
        players.append(PlayerState(
            id=p["id"],
            fighter_kind=p["fighter_kind"],
            fighter_status_kind=p["fighter_status_kind"],
            situation_kind=p["situation_kind"],
            lr=p["lr"],
            percent=p["percent"],
            position=Position(
                x=p["position"]["x"],
                y=p["position"]["y"],
            ),
            control_state=ControlState(
                stick_x=p["control_state"]["stick_x"],
                stick_y=p["control_state"]["stick_y"],
                button_attack=p["control_state"]["button_attack"],
                button_special=p["control_state"]["button_special"],
                button_smash=p["control_state"]["button_smash"],
                button_guard=p["control_state"]["button_guard"],
                button_guard_hold=p["control_state"]["button_guard_hold"],
                button_catch=p["control_state"]["button_catch"],
                button_jump=p["control_state"]["button_jump"],
                button_jump_mini=p["control_state"]["button_jump_mini"],
                button_invalid=p["control_state"]["button_invalid"]
            ),
            is_cpu=p["is_cpu"]
        ))
    return GameState(
        players=players,
        projectiles=[]
    )
