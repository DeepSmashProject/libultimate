import os
from libultimate import Console, ActionController, Direction, Action
import time
if __name__ == "__main__":
    RYUJINX_PATH = "/path/to/Ryujinx" # ex: /home/username/.config/Ryujinx
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = ActionController(player_id=1)
        console.add_controller(controller_1p)
        for action in Action:
            print(action.name)
            controller_1p.act(action.value)
            time.sleep(2)
