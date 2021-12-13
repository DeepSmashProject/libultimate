import time
from typing import List
import numpy as np
import requests
from yuzulib import Client
from .enums import Button
import matplotlib.pyplot as plt

class UltimateClient(Client):
    def __init__(self, address="http://localhost:6000", disable_warning=False) -> None:
        super.__init__(self, address, disable_warning)

    def move_to_home(self):
        self.reset_game()
        url = '{}/controller/move/home'.format(self.address)
        res = requests.post(url)
        pass

    def move_to_training(self, stage, player_fighter, player_color, cpu_fighter, cpu_color, cpu_level, quick_mode: bool):
        self.move_to_home()
        url = '{}/controller/move/training'.format(self.address)
        payload = {
            "stage": stage, 
            "player": {"fighter": player_fighter, "color": player_color}, 
            "cpu": {"fighter": cpu_fighter, "color": cpu_color, "level": cpu_level},
            "setting": {"quick_mode": quick_mode, "cpu_behavior": "cpu", "diable_combo_display": True}
        }
        res = requests.post(url, json=payload)
