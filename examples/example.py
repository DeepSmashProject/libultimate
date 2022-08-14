import os
import sys
from libultimate import Console, Controller

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    console = Console(ryujinx_path=RYUJINX_PATH)
    controller = Controller(console=console, port=1)

    for gamestate in console.stream(hz=5):
        print("gamestate: ", gamestate)
        #result = controller.press()
        #print("controled: ", result.message)
