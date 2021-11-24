from yuzulib import Runner, Screen, Controller, Button
from libultimate import Action
import time

controller = Controller()

for i in range(100):
    #print("Action JAB")
    controller.act(Button.BUTTON_ZL)
    time.sleep(1)
