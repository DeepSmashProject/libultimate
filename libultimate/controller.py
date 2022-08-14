from .console import Console
from typing import NamedTuple, Tuple
from contextlib import ExitStack
from typing import List
from .enums import Button
import threading
import time
from pynput.keyboard import Controller as Con, Key
from .enums import Action

class ControllerState(NamedTuple):
    button_a: bool = False
    button_b: bool = False
    button_x: bool = False
    button_y: bool = False
    button_l: bool = False
    button_r: bool = False
    button_z: bool = False
    button_zl: bool = False
    button_zr: bool = False
    button_d_up: bool = False
    button_d_down: bool = False
    button_d_left: bool = False
    button_d_right: bool = False
    main_stick: Tuple[float, float] = (0, 0) # -1 -> +1
    c_stick: Tuple[float, float] = (0, 0) # -1 -> +1

class ControllerOld():
    def __init__(self, console: Console, port: int=1):
        self.console = console
        self.port = port

    def press(self):
        res = self.console.api.send_command()
        return res

    def release(self):
        res = self.console.api.send_command()
        return res

    def release_all(self):
        res = self.console.api.send_command()
        return res
        
class Controller:
    def __init__(self):
        self.control_event = threading.Event()
        self.kill_event = threading.Event()
        self.unhold_event = threading.Event()
        self.data = {"buttons": [], "hold": False, "sec": 0}
        # blank push for focus keyboard
        self.keyboard = Con()
        self.run()
        self.press([Button.BUTTON_MODIFIER])

    def run(self):
        thread = threading.Thread(target=self._control)
        thread.start()
        time.sleep(1)

    def press(self, buttons: List[Button], hold=False, sec=0, wait=0, refresh=False):
        if self.data["hold"]:
            if buttons == self.data["buttons"] and hold and not refresh:
                return
            else:
                self.unhold_event.set()
                time.sleep(0.02)
                
        self.data = {"buttons": buttons, "hold": hold, "sec": sec}
        self.control_event.set()
        time.sleep(wait)
    
    def _convert_pynput_buttons(self, buttons: List[Button]):
        pynput_buttons = []
        for bt in buttons:
            if bt.value in Key.__members__:
                pynput_buttons.append(Key[bt.value])
            else:
                pynput_buttons.append(bt.value)
        return pynput_buttons


    def _control(self):
        while True:
            self.control_event.wait()
            self.control_event.clear()
            if self.kill_event.is_set():
                break
            self._press()

    def _press(self):
        #print(self.data)
        #buttons = self.data["buttons"]
        buttons = self._convert_pynput_buttons(self.data["buttons"])
        if len(buttons) == 0:
            return
        with ExitStack() as stack:
            for i, button in enumerate(buttons):
                if i == len(buttons)-1:
                    break
                stack.enter_context(self.keyboard.pressed(button))
            last_button = buttons[len(buttons)-1]
            self.keyboard.press(last_button)
            if self.data["hold"]:
                self.unhold_event.wait()
                self.unhold_event.clear()
                self.keyboard.release(last_button)
            else:
                if self.data["sec"] != None:
                    time.sleep(self.data["sec"])
                self.keyboard.release(last_button)

    def close(self):
        time.sleep(1)
        self.unhold_event.set()
        self.kill_event.set()
        self.control_event.set()

class UltimateController(Controller):
    def __init__(self):
        super(UltimateController, self).__init__()
        #self.mode = Mode(self)

    def act(self, action: Action):
        buttons = action["buttons"]
        hold = action["hold"]
        sec = action["sec"]
        wait = action["wait"]
        refresh = action["refresh"]
        self.press(buttons, hold=hold, sec=sec, wait=wait, refresh=refresh)


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.press([Button.BUTTON_A, Button.BUTTON_C_DOWN])
    controller.close()
