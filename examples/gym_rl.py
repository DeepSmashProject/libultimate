import os
import random
from libultimate import Console, UltimateController, Action, UltimateEnv

action_list = [
    Action.ACTION_JAB,
    Action.ACTION_RIGHT_TILT,
    Action.ACTION_LEFT_TILT,
    Action.ACTION_UP_TILT,
    Action.ACTION_DOWN_TILT,
    Action.ACTION_RIGHT_SMASH,
    Action.ACTION_LEFT_SMASH,
    Action.ACTION_UP_SMASH,
    Action.ACTION_DOWN_SMASH,
    Action.ACTION_NEUTRAL_SPECIAL,
    Action.ACTION_RIGHT_SPECIAL,
    Action.ACTION_LEFT_SPECIAL,
    Action.ACTION_UP_SPECIAL,
    Action.ACTION_DOWN_SPECIAL,
    Action.ACTION_GRAB,
    Action.ACTION_SHIELD,
    Action.ACTION_JUMP,
    Action.ACTION_RIGHT_JUMP,
    Action.ACTION_LEFT_JUMP,
    Action.ACTION_SHORT_HOP,
    Action.ACTION_RIGHT_SHORT_HOP,
    Action.ACTION_LEFT_SHORT_HOP,
    #Action.ACTION_UP_TAUNT,
    #Action.ACTION_DOWN_TAUNT,
    #Action.ACTION_LEFT_TAUNT,
    #Action.ACTION_RIGHT_TAUNT,
    Action.ACTION_SPOT_DODGE,
    Action.ACTION_RIGHT_ROLL,
    Action.ACTION_LEFT_ROLL,
    #Action.ACTION_RIGHT_DASH,
    #Action.ACTION_LEFT_DASH,
    #Action.ACTION_RIGHT_WALK,
    #Action.ACTION_LEFT_WALK,
    #Action.ACTION_CROUCH,
    #Action.ACTION_RIGHT_CRAWL,
    #Action.ACTION_LEFT_CRAWL,
    Action.ACTION_RIGHT_STICK,
    Action.ACTION_LEFT_STICK,
    Action.ACTION_UP_STICK,
    Action.ACTION_DOWN_STICK,
    #Action.ACTION_NO_OPERATION
]

if __name__ == "__main__":
    RYUJINX_PATH = os.path.join(os.path.dirname(__file__), "../libultimate/test")
    console = Console(ryujinx_path=RYUJINX_PATH)
    controller = UltimateController()
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
