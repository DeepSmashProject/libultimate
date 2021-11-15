#from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
import time
import pyautogui
m = mouse.Controller()
k = keyboard.Controller()
import os
from pathlib import Path

data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()
path = str(data_path) + '/screenshot.png'

while True:
    time.sleep(1)
    res = pyautogui.locateOnScreen(path, confidence=.8)
    if res != None:
        print("Reached Home!")
        break
    else:
        k.press("v")
        time.sleep(0.1)
        k.release("v")
        k.press("x")
        time.sleep(0.1)
        k.release("x")
