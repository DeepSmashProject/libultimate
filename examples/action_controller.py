import os
from libultimate import Console, ActionController, Direction, Action
import time
if __name__ == "__main__":
    SDCARD_PATH = "~/YOUR_SDCARD_PATH" # ex: if Ryujinx: ~/.config/Ryujinx, if Yuzu: ~/.local/share/yuzu/sdmc
    with Console(sdcard_path=SDCARD_PATH) as console:
        controller_1p = ActionController(player_id=0)
        console.add_controller(controller_1p)
        for action in Action:
            print(action.name)
            controller_1p.act(action.value)
            time.sleep(2)
