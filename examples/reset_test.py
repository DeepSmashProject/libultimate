from yuzulib import Runner, Screen, Button
from libultimate import Controller, Action, TrainingMode, Stage, Fighter
import time
import random
runner = Runner("", "", "")
runner.run()

controller = Controller()
# Reset Position
print("reset")
controller.multi_press([Button.BUTTON_L, Button.BUTTON_R, Button.BUTTON_A], sec=0.02)
time.sleep(0.1)