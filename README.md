# libultimate

Open API written in Python 3 for making your own Smash Bros Ultimate AI that works with Ryujinx or Yuzu

### Demo
https://user-images.githubusercontent.com/43264434/188854277-5facc0c9-8c50-412e-853a-112a45fef26f.mp4

## Required
- Ryujinx (latest)
- Python3, Pip3
- Cargo

## Install

```
# main
pip install git+https://github.com/DeepSmashProject/libultimate.git

# version 1.2.1
pip install git+https://github.com/DeepSmashProject/libultimate.git@1.2.1
```

or

```
git clone https://github.com/DeepSmashProject/libultimate.git
cd libultimate
pip3 install -e .
```

# Get Started
## 1. make sure the game is ready to run
1. install prod.keys
   - For Yuzu: From File -> Open yuzu folder
Copy prod.keys from $HOME/.local/share/yuzu/keys
   - For Ryujinx: Copy prod.keys to $HOME/.config/Ryujinx/system/prod.keys

2. install firmware
   - For Yuzu: Copy the files extracted from firmware.zip to $HOME/.local/share/yuzu/nand/system/Contents/registered
   - For Ryujinx: Tools->InstallFirmware->Install from Zip and select firmware-xxx.zip

3. set up your game
   - For Yuzu: Go to Add New Game Directory and select your game directory.
   - For Ryujinx: Go to Options->Settings->General->Add and select the SSBU folder (the folder with nsp)

## 2. install Skyline Plugin
1. install DLC
libparam-hook.nro is compatible with 13.0.1, so you need to update it to 13.0.1.
Right click on the Ryujinx game title and select Manage Title Update->nsp for v13.0.1.

2. install the plugin

Download the plugin
````
curl -L https://github.com/DeepSmashProject/libultimate/releases/download/${LIB_ULTIMATE_VERSION}/release.zip
```

- For Yuzu: Extract the above release.zip and put release/contents/01006A800016E000 into $HOME/.local/share/yuzu/sdmc/atmosphere/contents
- For Ryujinx: put release/contents/01006A800016E000 into $HOME/.config/Ryujinx/mods/contents

Restart the game and if it works correctly, you are good to go.
After entering the competitive mode, look at sdcard/libultimate/game_state.json and if the data is in there, it is working.

## 3. install libultimate and run examples
1. install libultimate

````
git clone https://github.com/DeepSmashProject/libultimate.git -b {LIB_ULTIMATE_VERSION}
cd libultimate
pip3 install -e .
```
LIB_ULTIMATE_VERSION must match the version of the plugin at the time of download. 2.

2. run examples

````
cd examples
````

Change SDCARD_PATH in basic.py.
- In case of Yuzu: ~/.local/share/yuzu/sdmc
- For Ryujinx: path like ~/.config/Ryujinx/sdcard.
```` import os
import os
from libultimate import Console, Controller, Button

if __name__ == "__main__":
    SDCARD_PATH = "~/YOUR_SDCARD_PATH" # ex: if Ryujinx: ~/.config/Ryujinx, if Yuzu: ~/.local/share/yuzu/sdmc
    with Console(sdcard_path=SDCARD_PATH) as console:
        controller_1p = Controller(player_id=0)
        console.add_controller(controller_1p)

        for gamestate in console.stream(fps=5):
            print("gamestate: ", gamestate)
            controller_1p.input([Button.A])

````

Run basic.py.
```
python3 basic.py
```

Translated with www.DeepL.com/Translator (free version)

## Example

```
import os
from libultimate import Console, Controller, Button

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join("path/to/Ryujinx") # ex. "/home/user/.config/Ryujinx"
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        controller_1p = Controller(player_id=0) # player_id: 0 ~ 7
        console.add_controller(controller_1p)

        for gamestate in console.stream(fps=5):
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

| Name        | Type          | Description                                                               |
| ----------- | ------------- | ------------------------------------------------------------------------- |
| frame_count | int           | current frame (loop 0 to 60)                                              |
| image       | 3d array[int] | RGB array. if include_image=True, you can get the desktop image per frame |
| players     | PlayerState[] | player statuses                                                           |
| projectiles | Projectile[]  | projectile statuses (not implemented)                                     |


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
| speed               | Speed    | speed                      |
| is_dead             | bool     | dead flag                  |
| is_cpu              | bool     | cpu: True, player: False   |

## Position

| Name | Type  | Description |
| ---- | ----- | ----------- |
| x    | float | x position  |
| y    | float | y position  |

## Speed

| Name | Type  | Description |
| ---- | ----- | ----------- |
| x    | float | x speed     |
| y    | float | y speed     |

## Fighter Status
Reference: https://github.com/jugeeya/UltimateTrainingModpack/blob/master/src/training/mash.rs

| Status                       | Num | Description                  |
| ---------------------------- | --- | ---------------------------- |
| WAIT                         | 0   | no action                    |
| WALK                         | 1   | walk                         |
| DASH_START                   | 3   | dash start                   |
| DASH                         | 4   | dash                         |
| DASH_END                     | 5   | dash end                     |
| TURN                         | 7   | turn                         |
| TURN_DASH                    | 8   | turn dash                    |
| JUMP                         | 11  | jump on ground               |
| JUMP_AERIAL                  | 12  | jump on aerial               |
| CANNOT_ACTION                | 16  | cannot action                |
| CROUCH                       | 18  | crouch                       |
| LANDING                      | 22  | landign from jump            |
| LANDING_SHORT                | 23  | landign from short jump      |
| GUARD_START                  | 27  | guard start                  |
| GUARD                        | 28  | guard                        |
| GUARD_END                    | 29  | guard end                    |
| ESCAPE_N                     | 31  | spot dodge                   |
| ESCAPE_F                     | 32  | roll dodge to forward        |
| ESCAPE_B                     | 33  | roll dodge to back           |
| ESCAPE_AIR                   | 34  | air dodge                    |
| ATTACK                       | 39  | neutral attack               |
| ATTACK_DASH                  | 41  | dash attack                  |
| ATTACK_S3                    | 42  | side attack                  |
| ATTACK_HI3                   | 43  | up attack                    |
| ATTACK_LW3                   | 44  | down attack                  |
| ATTACK_SIDE_SMASH_KEEP_START | 45  | side smash keep first        |
| ATTACK_SIDE_SMASH_KEEP       | 46  | side smash keep during       |
| ATTACK_S4                    | 47  | side smash attack            |
| ATTACK_DOWN_SMASH_KEEP_START | 48  | down smash keep first        |
| ATTACK_DOWN_SMASH_KEEP       | 49  | down smash keep during       |
| ATTACK_LW4                   | 50  | down smash attack            |
| ATTACK_UP_SMASH_KEEP_START   | 51  | up smash keep first          |
| ATTACK_UP_SMASH_KEEP         | 52  | up smash keep during         |
| ATTACK_HI4                   | 53  | up smash attack              |
| ATTACK_AIR                   | 54  | attack on air                |
| GRAB                         | 55  | grab                         |
| GRAB_WAIT                    | 60  | grab wait                    |
| GRAB_ATTACK                  | 61  | grab attack                  |
| GRAB_CUT                     | 62  | grab cut                     |
| GRAB_TURN                    | 64  | throw from grab              |
| GRABBED                      | 66  | grabbed                      |
| GRABBED_ATTACKED             | 67  | damaged attack from grabbed  |
| GRABBED_CUT                  | 68  | escaped from grabbed         |
| GRABBED_THROWED              | 70  | throwed from grabbed         |
| DAMAGED_NOT_FLY              | 71  | recieved weak damage         |
| DAMAGED_STANDING_FLY         | 72  | recieved standing fly damage |
| DAMAGED_FALL_FLY             | 73  | recieved fall fly damage     |
| DOWN_START                   | 80  | down start                   |
| DOWN                         | 83  | down                         |
| DOWN_GETUP                   | 87  | getup from down              |
| CLIFF_CATCH                  | 119 | catch cliff                  |
| CLIFF_ATTACK                 | 120 | attack from cliff            |
| CLIFF_CLIMB                  | 121 | climb from cliff             |
| CLIFF_ESCAPE                 | 122 | escape from cliff            |
| CLIFF_JUMP1                  | 124 | jump from cliff              |
| CLIFF_JUMP2                  | x   | jump2 from cliff             |
| CLIFF_STEGGER                | 127 | stegger on edge of cliff     |
| DEAD                         | 470 | dead                         |
| SPECIAL_N                    | 476 | special attack               |
| SPECIAL_S                    | 477 | side special attack          |
| SPECIAL_HI                   | 478 | up special attack            |
| SPECIAL_LW                   | 481 | down special attack          |

## Situation Status

| Status   | Num | Description |
| -------- | --- | ----------- |
| GROUND   | 0   | on ground   |
| CLIFF    | 1   | on cliff    |
| AIR      | 2   | on air      |
| OUTFIELD | 5   | on outfield |

# Use Docker

Edit docker/.env
```
make build
make run 
make exec
make remove
```