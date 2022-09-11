import os
from libultimate import Console, Controller, Direction
import time
if __name__ == "__main__":
    RYUJINX_PATH = "/path/to/Ryujinx" # ex: /home/username/.config/Ryujinx
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = Controller(player_id=1)
        console.add_controller(controller_1p)

        funcs = [
            {"name": "JAB", "func": lambda : controller_1p.jab()},
            {"name": "UP TILT", "func": lambda : controller_1p.tilt(Direction.UP)},
            {"name": "DOWN TILT", "func": lambda : controller_1p.tilt(Direction.DOWN)},
            {"name": "LEFT TILT", "func": lambda : controller_1p.tilt(Direction.LEFT)},
            {"name": "RIGHT TILT", "func": lambda : controller_1p.tilt(Direction.RIGHT)},
            {"name": "UP SPECIAL", "func": lambda : controller_1p.special(Direction.UP)},
            {"name": "DOWN SPECIAL", "func": lambda : controller_1p.special(Direction.DOWN)},
            {"name": "LEFT SPECIAL", "func": lambda : controller_1p.special(Direction.LEFT)},
            {"name": "RIGHT SPECIAL", "func": lambda : controller_1p.special(Direction.RIGHT)},
            {"name": "UP SMASH", "func": lambda : controller_1p.smash(Direction.UP)},
            {"name": "DOWN SMASH", "func": lambda : controller_1p.smash(Direction.DOWN)},
            {"name": "LEFT SMASH", "func": lambda : controller_1p.smash(Direction.LEFT)},
            {"name": "RIGHT SMASH", "func": lambda : controller_1p.smash(Direction.RIGHT)},
            {"name": "RIGHT DASH ATTACK", "func": lambda : controller_1p.dash_attack(lr=True)}, # Right
            {"name": "LEFT DASH ATTACK", "func": lambda : controller_1p.dash_attack(lr=False)}, # Left
            {"name": "GUARD", "func": lambda : controller_1p.guard()},
            {"name": "GRAB", "func": lambda : controller_1p.grab()},
            {"name": "SPOT DODGE", "func": lambda : controller_1p.spot_dodge()},
            {"name": "RIGHT ROLL", "func": lambda : controller_1p.roll(lr=True)}, # Right
            {"name": "LEFT ROLL", "func": lambda : controller_1p.roll(lr=False)}, # Left
            {"name": "RIGHT WALK", "func": lambda : controller_1p.walk(lr=True)}, # Right
            {"name": "LEFT WALK", "func": lambda : controller_1p.walk(lr=False)}, # Left
            {"name": "RIGHT DASH", "func": lambda : controller_1p.dash(lr=True)}, # Right
            {"name": "LEFT DASH", "func": lambda : controller_1p.dash(lr=False)}, # Left
            {"name": "JUMP", "func": lambda : controller_1p.jump()},
            {"name": "RIGHT JUMP", "func": lambda : controller_1p.jump(lr=True)}, # Right
            {"name": "LEFT JUMP", "func": lambda : controller_1p.jump(lr=False)}, # Left
            {"name": "RIGHT SHORT HOP", "func": lambda : controller_1p.short_hop()}, 
            {"name": "RIGHT SHORT HOP", "func": lambda : controller_1p.short_hop(lr=True)}, # Right
            {"name": "LEFT SHORT HOP", "func": lambda : controller_1p.short_hop(lr=False)}, # Left
            {"name": "UP TAINT", "func": lambda : controller_1p.taint(Direction.UP)},
            {"name": "DOWN TAINT", "func": lambda : controller_1p.taint(Direction.DOWN)},
            {"name": "LEFT TAINT", "func": lambda : controller_1p.taint(Direction.LEFT)},
            {"name": "RIGHT TAINT", "func": lambda : controller_1p.taint(Direction.RIGHT)},
        ]
        for data in funcs:
            print(data["name"])
            data["func"]()
            time.sleep(2)
