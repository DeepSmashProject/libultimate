import time
from typing import List
import numpy as np
import requests
from yuzulib import Client
from .enums import Button
import matplotlib.pyplot as plt

class UltimateClient(Client):
    def __init__(self, address="http://localhost:6000", disable_warning=False) -> None:
        super(UltimateClient, self).__init__(address, disable_warning)

    def move_to_home(self):
        self.reset_game()
        url = '{}/ultimate-controller/move/home'.format(self.address)
        res = requests.post(url)
        pass

    def move_to_training(self, config):
        self.move_to_home()
        url = '{}/ultimate-controller/move/training'.format(self.address)
        payload = config
        res = requests.post(url, json=payload)
