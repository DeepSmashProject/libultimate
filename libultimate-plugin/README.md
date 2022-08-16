
# Fighter Status
https://github.com/jugeeya/UltimateTrainingModpack/blob/master/src/training/mash.rs

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

# Situation Status

| Status   | Num | Description |
| -------- | --- | ----------- |
| GROUND   | 0   | on ground   |
| CLIFF    | 1   | on cliff    |
| AIR      | 2   | on air      |
| OUTFIELD | 5   | on outfield |
