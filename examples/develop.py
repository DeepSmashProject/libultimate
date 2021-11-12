from yuzulib import Runner, Screen
from libultimate import Controller, Action
import time
runner = Runner("", "", "")
runner.run()

controller = Controller()
def callback(frame, fps):
    print("callback!", frame[0][0], fps)
    start = time.time()
    controller.press(Action.ACTION_JAB)
    elapsed_time = time.time() - start
    print(elapsed_time)
screen = Screen(callback, fps=60)
screen.capture()
