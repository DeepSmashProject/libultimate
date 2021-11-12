from yuzulib import Runner, Screen
from libultimate import Controller, Action
import time
import random
runner = Runner("", "", "")
runner.run()

controller = Controller()
def callback(frame, fps):
    print("callback!", frame[0][0], fps)
    start = time.time()
    list = [Action.ACTION_JAB,
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
            Action.ACTION_JAMP,
            Action.ACTION_SHORT_HOP,
            Action.ACTION_UP_TAUNT,
            Action.ACTION_DOWN_TAUNT,
            Action.ACTION_LEFT_TAUNT,
            Action.ACTION_RIGHT_TAUNT,
            Action.ACTION_SPOT_DODGE,
            Action.ACTION_RIGHT_ROLL,
            Action.ACTION_LEFT_ROLL,
            Action.ACTION_RIGHT_DASH,
            Action.ACTION_LEFT_DASH,
            Action.ACTION_RIGHT_WALK,
            Action.ACTION_LEFT_WALK,
            Action.ACTION_CROUCH,
            Action.ACTION_RIGHT_CRAWL,
            Action.ACTION_LEFT_CRAWL,
            Action.ACTION_RIGHT_STICK,
            Action.ACTION_LEFT_STICK,
            Action.ACTION_UP_STICK,
            Action.ACTION_DOWN_STICK,
            Action.ACTION_NO_OPERATION]
    controller.act(random.choice(list))
    elapsed_time = time.time() - start
    print(elapsed_time)
screen = Screen(callback, fps=60)
screen.capture()
