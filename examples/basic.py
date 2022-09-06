import os
from libultimate import Console, UltimateController, Action

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    console = Console(ryujinx_path=RYUJINX_PATH)
    controller = UltimateController(console)

    for gamestate in console.stream(hz=5):
        print("gamestate: ", gamestate)
        controller.act(0, Action.JUMP, main_stick=(1, 0))
