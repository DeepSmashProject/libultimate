import os
from libultimate import Console, UltimateController, Action

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    console = Console(ryujinx_path=RYUJINX_PATH)
    controller_1p = UltimateController(console, player_id=1)

    for gamestate in console.stream(hz=5):
        print("gamestate: ", gamestate)
        controller_1p.act(Action.JUMP, main_stick=(1, 0))
