import os
import random
from libultimate import Console, UltimateController, Action, UltimateEnv

action_list = [
    Action.AIR_ESCAPE,
    Action.ATTACK_HI3,
    Action.ATTACK_HI4,
    Action.ATTACK_LW3,
    Action.ATTACK_LW4,
    Action.ATTACK_N,
    Action.ATTACK_S3,
    Action.ATTACK_S4,
    Action.CATCH,
    Action.DASH,
    Action.ESCAPE,
    Action.ESCAPE_B,
    Action.ESCAPE_F,
    Action.JUMP,
    Action.JUMP_BUTTON,
    Action.SPECIAL_ANY,
    Action.SPECIAL_HI,
    Action.SPECIAL_LW,
    Action.SPECIAL_N,
    Action.SPECIAL_S,
    Action.TURN,
    Action.TURN_DASH,
    Action.WALK,
    Action.WALL_JUMP_LEFT,
    Action.WALL_JUMP_RIGHT,
    Action.NONE,
]

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    console = Console(ryujinx_path=RYUJINX_PATH)
    controller = UltimateController(console)
    env = UltimateEnv(console, controller, hz=6, action_list=action_list)

    for k in range(10):
        done = False
        obs = env.reset()
        step = 0
        while not done:
            action = random.choice(action_list)
            next_obs, reward, done, info = env.step(action)
            print("episode: {}, step: {}, done: {}, reward: {}, action: {}".format(k, step, done, reward, action["name"]))
            step += 1
    print("finished!")
