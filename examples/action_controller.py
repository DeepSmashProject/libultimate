import os
from libultimate import Console, ActionController, Direction, Action
import time
if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = ActionController(player_id=1)
        console.add_controller(controller_1p)
        for action in Action.values():
            print(action)
            controller_1p.act(action)
            time.sleep(2)
