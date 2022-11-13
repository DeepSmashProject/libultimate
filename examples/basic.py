import os
from libultimate import Console, Controller, Button

if __name__ == "__main__":
    RYUJINX_PATH = "/path/to/Ryujinx" # ex: /home/username/.config/Ryujinx
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = Controller(player_id=0)
        console.add_controller(controller_1p)

        for gamestate in console.stream(fps=5):
            print("gamestate: ", gamestate)
            controller_1p.input([Button.A])
