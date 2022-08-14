from typing import NamedTuple, List
from .enums import Fighter

class Position(NamedTuple):
    x: float = 0
    y: float = 0

class PlayerState(NamedTuple):
    fighter: Fighter
    direction: bool
    percent: float
    position: Position
    charge: float

class Projectile(NamedTuple):
    position: Position

class GameState(NamedTuple):
    players: List[PlayerState]
    projectiles: List[Projectile]
