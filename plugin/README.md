
# Install cargo-skyline

https://github.com/jam1garner/cargo-skyline
https://github.com/ultimate-research/skyline-smash
https://github.com/ultimate-research/skyline-rs-template


```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Permissionエラーが出る場合
cp /tmp/tmp.xxxx/rustup-init /home/default
cd /home/default
./rustup-init
```

```
cargo install cargo-skyline
```

```
cargo skyline listen
```

# Fighter Status
https://github.com/jugeeya/UltimateTrainingModpack/blob/master/src/training/mash.rs

| Status           | Num | Description         |
| ---------------- | --- | ------------------- |
| WAIT             | 0   | no action           |
| WALK             | 1   | walk                |
| DASH             | 4   | dash                |
| RUN_BRAKE?       | 5   | finish run          |
| TURN             | 7   | turn                |
| TURN_DASH        | 8   | turn dash           |
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
| STANDBY          | 182 | on board after dead |
| DEAD             | 470 | dead                |
| SPECIAL_N        | 476 | special attack      |
| SPECIAL_S        | 477 | side special attack |
| SPECIAL_HI       | 478 | up special attack   |
| SPECIAL_LW       | 481 | down special attack |

# Situation Status

| Status   | Num | Description |
| -------- | --- | ----------- |
| GROUND   | 0   | on ground   |
| CLIFF    | 1   | on cliff    |
| AIR      | 2   | on air      |
| OUTFIELD | 5   | on outfield |

# Action

| Status          | Description        |
| --------------- | ------------------ |
| AIR_ESCAPE      | air escape         |
| ATTACK_HI3      | up tilt            |
| ATTACK_HI4      | up smash           |
| ATTACK_LW3      | down tilt          |
| ATTACK_LW4      | down smash         |
| ATTACK_N        | Jab                |
| ATTACK_S3       | side tilt          |
| ATTACK_S4       | side smash         |
| CATCH           | grab               |
| DASH            | dash               |
| ESCAPE          | spot dogde         |
| ESCAPE_B        | back roll dodge    |
| ESCAPE_F        | forward roll dodge |
| JUMP            | jump               |
| JUMP_BUTTON     | jump               |
| SPECIAL_ANY     | up special ?       |
| SPECIAL_HI      | up special         |
| SPECIAL_LW      | down special       |
| SPECIAL_N       | neutral special    |
| SPECIAL_S       | side special       |
| TURN            | turn               |
| TURN_DASH       | turn dash          |
| WALK            | walk               |
| WALL_JUMP_LEFT  | wall jump left     |
| WALL_JUMP_RIGHT | wall jump right    |

# Button

| Status        | Num     | Description    |
| ------------- | ------- | -------------- |
| NONE          | 0       | none           |
| A             | 1       | a              |
| B             | 2       | b              |
| X             | 4       | x              |
| Y             | 8       | y              |
| LStick Button | 16      | l stick button |
| RStick Button | 32      | r stick button |
| L             | 64      | l              |
| R             | 128     | r              |
| ZL            | 256     | zl             |
| ZR            | 512     | zr             |
| Plus          | 1024    | +              |
| Minus         | 2048    | -              |
| DPad Left     | 4096    | d pad left     |
| DPad Up       | 8192    | d pad up       |
| DPad Right    | 16384   | d pad right    |
| DPad Down     | 32768   | d pad down     |
| LStick Left   | 65536   | l stick left   |
| LStick Up     | 131072  | l stick up     |
| LStick Right  | 262144  | l stick right  |
| LStick Down   | 524288  | l stick down   |
| RStick Left   | 1048576 | r stick left   |
| RStick Up     | 2097152 | r stick up     |
| RStick Right  | 4194304 | r stick right  |
| RStick Down   | 8388608 | r stick down   |

# test
NONE
DASH, WALK, JUMP, SHORT_HOP
GUARD, SPOT_DODGE, F_ROL, B_ROLL
CATCH, THROW_F, THROW_B, THROW_U, THROW_D
TILT_FBUD
SMASH_FBUD
ATTACK_FBUD, JAB
DASH_ATTAK
NAIR, BAIR, FAIR, UAIR, DAIR
TURN, TURN_DASH
