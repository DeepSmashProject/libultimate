from yuzulib import Controller, Runner, Button, Screen
import time
runner = Runner("", "", "")
runner.run()

controller = Controller()
def callback(frame, fps):
    print("callback!", frame[0][0], fps)
    start = time.time()
    controller.press(Button.BUTTON_A)
    elapsed_time = time.time() - start
    print(elapsed_time)
screen = Screen(callback, fps=60)
screen.capture()
