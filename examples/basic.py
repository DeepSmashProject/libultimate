import os
from libultimate import Console, Controller, Button

if __name__ == "__main__":
    SDCARD_PATH = "~/YOUR_SDCARD_PATH" # ex: if Ryujinx: ~/.config/Ryujinx, if Yuzu: ~/.local/share/yuzu/sdmc
    with Console(sdcard_path=SDCARD_PATH) as console:
        controller_1p = Controller(player_id=0)
        console.add_controller(controller_1p)

        for gamestate in console.stream(fps=5, include_image=True, image_size=(256, 256)):
            print("gamestate: ", gamestate)
            controller_1p.input([Button.A])
