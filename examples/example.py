import os
import sys
from libultimate import Console, Controller, UltimateController, Action

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    console = Console(ryujinx_path=RYUJINX_PATH)
    controller = UltimateController()

    for gamestate in console.stream(hz=5):
        print("gamestate: ", gamestate)
        controller.act(Action.ACTION_JAB)
        #result = controller.press()
        #print("controled: ", result.message)
