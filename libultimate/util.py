from pynput import mouse, keyboard
import time
m = mouse.Controller()
k = keyboard.Controller()

def click_mouse(delay: int = 0):
    m.press(mouse.Button.left)
    m.release(mouse.Button.left)
    time.sleep(delay)

def move_mouse(x: float, y: float):
    m.position = (x, y)

def press_key(key: str, delay: int = 0):
    k.press(key)
    k.release(key)
    time.sleep(delay)

