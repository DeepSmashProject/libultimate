from pydantic import BaseModel
from typing import List, Optional, Any
from .enums import Fighter

class ControlState(BaseModel):
    id: str
    player_id: int
    update_count: int
    buttons: int
    l_stick_x: int
    l_stick_y: int
    r_stick_x: int
    r_stick_y: int
    flags: int
    l_trigger: int
    r_trigger: int
    hold: bool


class Position(BaseModel):
    x: float
    y: float

class Speed(BaseModel):
    x: float
    y: float

class ControllerState(BaseModel):
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

class FighterInformation(BaseModel):
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

class PlayerState(BaseModel):
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

class Projectile(BaseModel):
    position: Position

class GameState(BaseModel):
    frame_count: int
    players: List[PlayerState]
    projectiles: List[Projectile]
    image: Optional[Any]
