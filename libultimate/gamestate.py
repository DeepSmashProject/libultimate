from typing import NamedTuple, List
from .enums import Fighter

class Position(NamedTuple):
    x: float = 0
    y: float = 0

class Speed(NamedTuple):
    x: float = 0
    y: float = 0

class ControllerState(NamedTuple):
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

class FighterInformation(NamedTuple):
    hit_point: int
    fighter_color: int
    is_operation_cpu: bool
    dead_count: int
    stock_count: int
    suicide_count: int
    total_beat_count: int
    is_last_dead_suicide: bool
    is_on_rebirth: bool
    fighter_category: int
    gravity: int

class PlayerState(NamedTuple):
    id: int
    fighter_kind: Fighter
    fighter_status_kind: int
    situation_kind: int
    lr: float
    percent: float
    position: Position
    speed: Speed
    #charge: float
    controller_state: ControllerState
    frame: int
    end_frame: int
    is_cpu: bool
    is_dead: bool
    #is_actionable: bool
    #fighter_information: FighterInformation

class Projectile(NamedTuple):
    position: Position

class GameState(NamedTuple):
    frame_count: int
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
            speed=Speed(
                x=p["speed"]["x"],
                y=p["speed"]["y"],
            ),
            #charge=p["charge"],
            controller_state=ControllerState(
                stick_x=p["controller_state"]["stick_x"],
                stick_y=p["controller_state"]["stick_y"],
                button_attack=p["controller_state"]["button_attack"],
                button_special=p["controller_state"]["button_special"],
                button_smash=p["controller_state"]["button_smash"],
                button_guard=p["controller_state"]["button_guard"],
                button_guard_hold=p["controller_state"]["button_guard_hold"],
                button_catch=p["controller_state"]["button_catch"],
                button_jump=p["controller_state"]["button_jump"],
                button_jump_mini=p["controller_state"]["button_jump_mini"],
                button_invalid=p["controller_state"]["button_invalid"]
            ),
            frame=p["frame"],
            end_frame=p["end_frame"],
            is_cpu=p["is_cpu"],
            is_dead=p["is_dead"],
            #is_actionable=p["is_actionable"],
            #fighter_information=FighterInformation(
            #    hit_point=p["fighter_information"]["hit_point"],
            #    fighter_color=p["fighter_information"]["fighter_color"],
            #    is_operation_cpu=p["fighter_information"]["is_operation_cpu"],
            #    dead_count=p["fighter_information"]["dead_count"],
            #    stock_count=p["fighter_information"]["stock_count"],
            #    suicide_count=p["fighter_information"]["suicide_count"],
            #    total_beat_count=p["fighter_information"]["total_beat_count"],
            #    is_last_dead_suicide=p["fighter_information"]["is_last_dead_suicide"],
            #    is_on_rebirth=p["fighter_information"]["is_on_rebirth"],
            #    fighter_category=p["fighter_information"]["fighter_category"],
            #    gravity=p["fighter_information"]["gravity"],
            #)
        ))
    return GameState(
        frame_count=gs_json["frame_count"],
        players=players,
        projectiles=[]
    )
