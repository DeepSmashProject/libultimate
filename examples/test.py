from pydantic import BaseModel
from typing import List, NamedTuple
import json

class Projectile(NamedTuple):
    position: int

class GameState(NamedTuple):
    frame_count: int
    projectiles: List[Projectile]


class Projectile2(BaseModel):
    position: int

class GameState2(BaseModel):
    frame_count: int
    projectiles: List[Projectile2]

gamestate = GameState2(frame_count=1, projectiles=[Projectile2(position=1), Projectile2(position=2)])
print(json.dumps(gamestate.json()))

gamestate = GameState(frame_count=1, projectiles=[Projectile(position=1), Projectile2(position=2)])
print(json.dumps(gamestate._asdict()))
