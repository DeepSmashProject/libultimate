import threading
import time
class Controller:
    def __init__(self):
        self.control_event = threading.Event()
        self.kill_event = threading.Event()
        self.unhold_event = threading.Event()
        self.data = {"buttons": [], "hold": False, "sec": 0}

    def run(self):
        thread = threading.Thread(target=self._control)
        thread.start()
        time.sleep(1)

    def press(self, buttons, hold=False, sec=0, wait=0):
        if self.data["hold"]:
            if buttons == self.data["buttons"]:
                if not hold:
                    self.unhold_event.set()
                else:
                    print("{} continue hold.".format(self.data))
                    return
            else:
                self.unhold_event.set()
        self.data = {"buttons": buttons, "hold": hold, "sec": sec}
        self.control_event.set()
        time.sleep(wait)

    def _control(self):
        while True:
            self.control_event.wait()
            self.control_event.clear()
            if self.kill_event.is_set():
                break
            self._press()

    def _press(self):
        print(self.data)
        if self.data["hold"]:
            print("hold")
            self.unhold_event.wait()
            self.unhold_event.clear()

    def close(self):
        print("close")
        time.sleep(1)
        self.unhold_event.set()
        self.kill_event.set()
        self.control_event.set()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.press(["1"])
    time.sleep(1)
    controller.press(["2"], hold=True)
    time.sleep(1)
    controller.press(["2"], hold=True)
    time.sleep(1)
    controller.close()