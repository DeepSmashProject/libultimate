from contextlib import ExitStack
from typing import List
import pyautogui
import time
import subprocess
import threading
import os
#from PyQt5.QtCore import QProcess
import os
from pathlib import Path
class Runner:
    def __init__(self, yuzu_path, game_dir, keys_dir):
        self.data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()
        self.yuzu_path = yuzu_path
        self.game_dir = game_dir
        self.keys_dir = keys_dir

    def setup(self):
        # copy prod.keys and title.keys
        pass

    def run(self):
        #p = QProcess()
        #p.start("/yuzu/build/bin/yuzu")
        #out = p.readAllStandardOutput()
        #print("test", out)
        #time.sleep(1000)
        #tt = threading.Thread( target = self._sub_thread )
        #tt.start()

        # take screen shot 
        #scrot /workspace/yuzulib/data/test.png -u
        self._take_screenshot()

    def _take_screenshot(self):
        filename = "{}/screenshot.png".format(str(self.data_path))
        # delete screenshot
        os.remove(filename)

        command = "scrot {} -u".format(filename)
        proc = subprocess.run(command, shell=True, executable='/bin/bash')
        if proc.returncode == 0:
            print("Take screenshot successfully")

    def _sub_thread(self):
        command = "/bin/bash -i -c '/yuzu/build/bin/yuzu'"
        subprocess.call(command, shell=True, executable='/bin/bash')


    
if __name__ == '__main__':
    runner = Runner("", "", "")
    runner.run()