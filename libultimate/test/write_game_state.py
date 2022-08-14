import os
import sys
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from gamestate import GameState
from enums import Fighter

def write_game_state(game_state):
    game_state_path = os.path.join(os.path.dirname(__file__), 'sdcard/libultimate/game_state.json')
    with open(game_state_path, 'w') as f:
        json.dump(game_state, f, indent=2, ensure_ascii=False)

def loop_write(hz=60):
    interval = hz * (1/60)
    percent = 0
    while True:
        time.sleep(interval)
        percent += 1
        game_state: GameState = {
            "players": [{
                "fighter": Fighter.FIGHTER_CAPTAIN.value,
                "direction": True,
                "percent": percent,
                "position": None,
                "charge": 0
            }],
            "projectiles": []
        }
        write_game_state(game_state)

if __name__ == "__main__":
    loop_write(15)
