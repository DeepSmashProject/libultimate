import os
import random
from libultimate import Console, Controller, EnvAction, UltimateEnv

action_list = [
    EnvAction.NONE,
    EnvAction.JAB,
    EnvAction.TILT_U,
    EnvAction.TILT_L,
    EnvAction.TILT_D,
    EnvAction.TILT_R,
    EnvAction.SMASH_U,
    EnvAction.SMASH_L,
    EnvAction.SMASH_D,
    EnvAction.SMASH_R,
    EnvAction.SPECIAL_U,
    EnvAction.SPECIAL_L,
    EnvAction.SPECIAL_D,
    EnvAction.SPECIAL_R,
    EnvAction.DASH_ATTACK_L,
    EnvAction.DASH_ATTACK_R,
    EnvAction.SPOT_DODGE,
    EnvAction.ROLL_L,
    EnvAction.ROLL_R,
    EnvAction.JUMP,
    EnvAction.JUMP_L,
    EnvAction.JUMP_R,
    EnvAction.SHORT_HOP,
    EnvAction.SHORT_HOP_L,
    EnvAction.SHORT_HOP_R,
    EnvAction.WALK_L,
    EnvAction.WALK_R,
    EnvAction.DASH_L,
    EnvAction.DASH_R,
    EnvAction.GUARD,
    EnvAction.GRAB,
]

if __name__ == "__main__":
    SDCARD_PATH = "~/YOUR_SDCARD_PATH" # ex: if Ryujinx: ~/.config/Ryujinx, if Yuzu: ~/.local/share/yuzu/sdmc
    with Console(sdcard_path=SDCARD_PATH) as console:
        controller_1p = Controller(player_id=0)
        console.add_controller(controller_1p)
        with UltimateEnv(console, controller_1p, hz=6, action_space=len(action_list)) as env:
            for k in range(10):
                done = False
                obs = env.reset()
                step = 0
                while not done:
                    action = random.choice(action_list)
                    next_obs, reward, done, info = env.step(action)
                    print("episode: {}, step: {}, done: {}, reward: {}, action: {}".format(k, step, done, reward, action.name))
                    step += 1
            print("finished!")
