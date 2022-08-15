from .enums import Stage, Button
import time

class Mode:
    def __init__(self, controller):
        self.training = TrainingMode(controller)

class TrainingMode:
    def __init__(self, controller):
        self._controller = controller

    def start(self, config):
        #config = {
        #    "stage": Stage.STAGE_HANENBOW, 
        #    "player": {"fighter": Fighter.FIGHTER_MARIO.name, "color": 0}, 
        #    "cpu": {"fighter": Fighter.FIGHTER_DONKEY_KONG.name, "color": 0, "level": 9},
        #    "setting": {"quick_mode": True, "cpu_behavior": "cpu", "diable_combo_display": True}
        #}
        print("Starting Training Mode")
        self._move_to_training_mode()
        self._select_stage(config["stage"])
        self._select_player(config["player"])
        self._select_cpu(config["cpu"])
        self._start_training()
        self._set_training_setting(config["setting"])
        self.reset()

    def _move_to_training_mode(self):
        print("Moving to training mode")
        # To Games & More from Home
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_UP], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)

        # To Training from Games & More
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(10) # Loading

    def _select_stage(self, stage: Stage):
        print("Selecting Stage: {}".format(stage.name))
        # Stage Select
        stage_num = stage.value
        stage_row = stage_num%11
        stage_line = int(stage_num/11)
        for i in range(stage_line):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.20, wait=0.30)
            time.sleep(0.3)
        for k in range(stage_row):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.23, wait=0.30)
            time.sleep(0.3)
        # to Final Destination
        self._controller.press([Button.BUTTON_X], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_X], sec=0.02)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(10) # Loading

    def _select_player(self, player_config):
        print("Selecting Player: {}".format(player_config["fighter"].name))
        ## Player Select
        ### to left top corner
        self._controller.press([Button.BUTTON_S_UP], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=3, wait=3)
        time.sleep(0.1)
        ### to mario
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.25, wait=0.25)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
        time.sleep(0.1)
        ### to fighter
        player_num = player_config["fighter"].value
        player_row = player_num%7
        player_line = int(player_num/7)
        for i in range(player_line):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
            time.sleep(0.1)
        for k in range(player_row):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.37, wait=1)
            time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)

    def _select_cpu(self, cpu_config):
        print("Selecting Cpu: {}".format(cpu_config["fighter"].name))
        ## Move CPU
        ### to right top corner
        self._controller.press([Button.BUTTON_S_UP], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_RIGHT], sec=3, wait=3)
        time.sleep(0.1)
        ### to random
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.25, wait=0.25)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.60, wait=1)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02) # TODO
        time.sleep(0.1)
        ## Select CPU
        ### to left top corner
        self._controller.press([Button.BUTTON_S_UP], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=3, wait=3)
        time.sleep(0.1)
        ### to mario
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.25, wait=0.25)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
        time.sleep(0.1)
        ### to fighter
        cpu_num = cpu_config["fighter"].value
        cpu_row = cpu_num%7
        cpu_line = int(cpu_num/7)
        for i in range(cpu_line):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.30, wait=0.30)
            time.sleep(0.1)
        for k in range(cpu_row):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.37, wait=1)
            time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(1)
        self._change_cpu_level(cpu_config["level"])

    def _change_cpu_level(self, cpu_level):
        print("Change Cpu Level: {}".format(cpu_level))
        # CPU LEVEL
        ### to right bottom corner
        self._controller.press([Button.BUTTON_S_DOWN], sec=3, wait=3)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_RIGHT], sec=3, wait=3)
        time.sleep(0.1)
        ### to level
        self._controller.press([Button.BUTTON_S_UP], sec=0.2, wait=0.2)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.5, wait=1)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02, wait=0.02) #TODO
        time.sleep(0.1)
        ### Change Level
        if cpu_level >= 3:
            for i in range(cpu_level - 3):
                self._controller.press([Button.BUTTON_S_UP], sec=0.2, wait=0.2)
                time.sleep(0.1)
        else:
            for i in range(3 - cpu_level):
                self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
                time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02, wait=0.02)
        time.sleep(1)

    def _start_training(self):
        ### Start Training Mode
        self._controller.press([Button.BUTTON_PLUS], sec=0.02, wait=0.02)
        time.sleep(15) # Loading
        print("Start Training")


    def _set_training_setting(self, setting_config):
        print("Set Training Setting")
        # Change Settings
        self._controller.press([Button.BUTTON_PLUS], sec=0.02)
        time.sleep(0.5)
        ## Change CPU Behavior
        for i in range(4):
            self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
            time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_RIGHT], sec=0.2, wait=0.2)
        time.sleep(0.1)

        ## Other Settings
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_A], sec=0.02)
        time.sleep(0.5)
        ## Speed Quick Mode
        for i in range(5):
            self._controller.press([Button.BUTTON_S_RIGHT], sec=0.2, wait=0.2)
            time.sleep(0.1)
        ## Not Display Combo
        self._controller.press([Button.BUTTON_S_DOWN], sec=0.2, wait=0.2)
        time.sleep(0.1)
        self._controller.press([Button.BUTTON_S_LEFT], sec=0.2, wait=0.2)
        time.sleep(0.1)
        # Finish Settings
        self._controller.press([Button.BUTTON_PLUS], sec=0.02)
        time.sleep(1)

    def reset(self):
        #print("Reset Training")
        self._controller.press([Button.BUTTON_L, Button.BUTTON_R, Button.BUTTON_A], sec=0.02, wait=0.2)
        time.sleep(0.1)


        










