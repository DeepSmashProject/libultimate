# libultimate

Open API written in Python 3 for making your own Smash Bros Ultimate AI that works with RyujinX

### Demo

## Required
- Ryujinx (latest)
- Python3, Pip3
- Cargo

## Install

```
git clone https://github.com/DeepSmashProject/libultimate.git
```

### Python Library
```
cd libultimate/libultimate
pip3 install -e .
```

### Skyline Library
```
cd libultimate/libultimate-plugin
cargo install cargo-skyline
cargo skyline build
```
liblibultimate_plugin.nro will be created in  './target/aargh64-skyline-switch/debug'

### Ryujinx
Download Ryujinx from https://ryujinx.org/

### SSBU Roms
SSBU Roms and prod.keys is need.
Please extract rom file by yourself

## Setup Instructions
Linux/OSX/Windows
1. Add prod.keys and SSBU Roms in Ryujinx
   - Reference: https://www.youtube.com/watch?v=CPKpgUDexzg&ab_channel=ShandellExplains
   - Please check to be able to run emulator and play ssbu.
2. Add libultimate plugin
   - Click "File" -> "Open Ryujinx Folder" on emulator.
   - Move plugin folder to "/mods/"
3. Run Emulator
   - Move to training mode.
   - If you want to check the plugin runnning status, you can see plugin logs by "cargo skyline listen" 
4. Run Example
   - Run "python3 examples/basic.py"

## Example

```
import os
from libultimate import Console, Controller, Button

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join("path/to/Ryujinx") # ex. "/home/user/.config/Ryujinx"
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = Controller(player_id=1)
        console.add_controller(controller_1p)

        for gamestate in console.stream(hz=5):
            print("gamestate: ", gamestate)
            controller_1p.input(Button.A)

```


