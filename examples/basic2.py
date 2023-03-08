import os
from libultimate import Console, Controller, Direction

if __name__ == "__main__":
    RYUJINX_PATH = "~/.config/Ryujinx" # ex: /home/username/.config/Ryujinx
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = Controller(player_id=0)
        console.add_controller(controller_1p)

        for gamestate in console.stream(fps=5):
            print("gamestate: ", gamestate)
            p1_x = gamestate.players[0].position.x
            p1_y = gamestate.players[0].position.y
            p2_x = gamestate.players[1].position.x
            p2_y = gamestate.players[1].position.y
            if p1_x < p2_x-10:
                controller_1p.dash(True)
            elif p1_x > p2_x+10:
                controller_1p.dash(False)
            else:
                controller_1p.smash(Direction.UP)
