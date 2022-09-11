# libultimate

Open API written in Python 3 for making your own Smash Bros Ultimate AI that works with RyujinX

### Demo
https://user-images.githubusercontent.com/43264434/188854277-5facc0c9-8c50-412e-853a-112a45fef26f.mp4

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
   - Required other nros
     - libnro_hook.nro: https://github.com/ultimate-research/nro-hook-plugin/releases/download/v0.3.0/libnro_hook.nro
     - libparam_hook.nro: https://github.com/ultimate-research/params-hook-plugin/releases/download/v0.1.1/libparam_hook.nro
     - libnn_hid_hook.nro: https://github.com/jugeeya/nn-hid-hook/releases/download/beta/libnn_hid_hook.nro
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
        controller_1p = Controller(player_id=0) # player_id: 0 ~ 7
        console.add_controller(controller_1p)

        for gamestate in console.stream(hz=5):
            print("gamestate: ", gamestate)
            controller_1p.input(Button.A)

```

# Methods

## Console
### init

```
with Console(ryujinx_path="path/to/ryujinx", level=logging.ERROR) as console:
```

| Name         | Default         | Type          | Description                 |
| ------------ | --------------- | ------------- | --------------------------- |
| ryujinx_path | Required*       | String        | Path of your ryujinx folder |
| level        | logging.WARNING | logging.LEVEL | Log Level                   |

### stream
```
for gamestate in console.stream(hz=60):
    print(gamestate)
```

| Name      | Default  | Type       | Description      |
| --------- | -------- | ---------- | ---------------- |
| gamestate |          | *GameState | *GameState       |
| hz        | Optional | int        | frame per second |

### add_controller
```
console.add_controller(controller_1p)
```

| Name       | Default   | Type        | Description |
| ---------- | --------- | ----------- | ----------- |
| controller | Required* | *Controller | *Controller |

## Controller
### init

```
controller_1p = Controller(player_id=1)
```

| Name      | Default   | Type      | Description           |
| --------- | --------- | --------- | --------------------- |
| player_id | Required* | int (0~7) | Controller port (0~7) |

### input

```
controller_1p.input(button=Button.A, main_stick=(0, 1), c_stick=(0, 0), hold=False)
```

| Name       | Default   | Type           | Description                                                                  |
| ---------- | --------- | -------------- | ---------------------------------------------------------------------------- |
| button     | Required* | *Button        | *Button (1~8)                                                                |
| main_stick | Optional  | (float, float) | main stick tuple (x, y): -1(left) < x <1(right), -1(down) < y < 1(up) second |
| c_stick    | Optional  | (float, float) | c stick tuple (x, y): -1(left) < x <1(right), -1(down) < y < 1(up)           |
| hold       | Optional  | bool           | hold input until next input                                                  |

### release_all
```
controller_1p.release_all()
```

### controller actions

```
controller_1p.jab()
controller_1p.tilt(Direction.UP)
controller_1p.tilt(Direction.DOWN)
controller_1p.tilt(Direction.LEFT)
controller_1p.tilt(Direction.RIGHT)
controller_1p.special(Direction.UP)
controller_1p.special(Direction.DOWN)
controller_1p.special(Direction.LEFT)
controller_1p.special(Direction.RIGHT)
controller_1p.smash(Direction.UP)
controller_1p.smash(Direction.DOWN)
controller_1p.smash(Direction.LEFT)
controller_1p.smash(Direction.RIGHT)
controller_1p.dash_attack(lr=True)
controller_1p.dash_attack(lr=False)
controller_1p.guard()
controller_1p.grab()
controller_1p.spot_dodge()
controller_1p.roll(lr=True)
controller_1p.roll(lr=False)
controller_1p.walk(lr=True)
controller_1p.walk(lr=False)
controller_1p.dash(lr=True)
controller_1p.dash(lr=False)
controller_1p.jump(Direction.NONE)
controller_1p.jump(Direction.RIGHT)
controller_1p.jump(Direction.LEFT)
controller_1p.taint(Direction.UP)
controller_1p.taint(Direction.DOWN)
controller_1p.taint(Direction.LEFT)
controller_1p.taint(Direction.RIGHT)
```

# Structs

## GameState

| Name        | Type          | Description                           |
| ----------- | ------------- | ------------------------------------- |
| players     | PlayerState[] | player statuses                       |
| projectiles | Projectile[]  | projectile statuses (not implemented) |


## PlayerState

| Name                | Type     | Description                |
| ------------------- | -------- | -------------------------- |
| id                  | int      | player id                  |
| fighter_kind        | int      | fighter kind id            |
| fighter_status_kind | int      | fighter status kind        |
| situation_kind      | int      | situation kind             |
| lr                  | int      | left = False, right = True |
| percent             | float    | damage percent             |
| position            | Position | position                   |

## Position

| Name | Type  | Description |
| ---- | ----- | ----------- |
| x    | float | x position  |
| y    | float | y position  |

## Fighter Status
Reference: https://github.com/jugeeya/UltimateTrainingModpack/blob/master/src/training/mash.rs

| Status           | Num | Description         |
| ---------------- | --- | ------------------- |
| WAIT             | 0   | no action           |
| WALK             | 1   | walk                |
| RUN              | 4   | run                 |
| JUMP             | 11  | jump on ground      |
| JUMP_AERIAL      | 12  | jump on aerial      |
| CANNOT_ACTION    | 16  | cannot action       |
| GUARD            | 28  | guard               |
| ESCAPE_B         | 31  | spot dodge          |
| ESCAPE_F         | 33  | roll dodge          |
| ESCAPE_AIR       | 33  | air dodge           |
| ESCAPE_AIR_SLIDE | 34  | air slide dodge     |
| ATTACK           | 39  | neutral attack      |
| ATTACK_DASH      | 41  | dash attack         |
| ATTACK_AIR       | 54  | attack on air       |
| ATTACK_S3        | 42  | side attack         |
| ATTACK_HI3       | 43  | up attack           |
| ATTACK_LW3       | 44  | down attack         |
| ATTACK_S4        | 47  | side smash attack   |
| ATTACK_LW4       | 50  | down smash attack   |
| ATTACK_HI4       | 53  | up smash attack     |
| CATCH            | 55  | grab                |
| CATCH_ATTACK     | 61  | grab attack         |
| CATCH_WAIT       | 60  | grab wait           |
| CATCH_CUT        | 62  | grab cut            |
| CATCH_TURN       | 64  | throw from grab     |
| CLIFF_CATCH      | 119 | catch cliff         |
| CLIFF_ATTACK     | 120 | attack from cliff   |
| CLIFF_CLIMB      | 121 | climb from cliff    |
| CLIFF_ESCAPE     | 122 | escape from cliff   |
| CLIFF_JUMP1      | 124 | jump from cliff     |
| CLIFF_JUMP2      | x   | jump2 from cliff    |
| DEAD             | 470 | dead                |
| SPECIAL_N        | 476 | special attack      |
| SPECIAL_S        | 477 | side special attack |
| SPECIAL_HI       | 478 | up special attack   |
| SPECIAL_LW       | 481 | down special attack |

## Situation Status

| Status   | Num | Description |
| -------- | --- | ----------- |
| GROUND   | 0   | on ground   |
| CLIFF    | 1   | on cliff    |
| AIR      | 2   | on air      |
| OUTFIELD | 5   | on outfield |
