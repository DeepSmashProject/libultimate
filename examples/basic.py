import os
from libultimate import Console, Controller, Button

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = Controller(player_id=1)
        console.add_controller(controller_1p)

        for gamestate in console.stream(hz=5):
            print("gamestate: ", gamestate)
            controller_1p.input([Button.A])
