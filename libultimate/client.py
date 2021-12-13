from matplotlib.pyplot import pause
import requests
from yuzulib import Client
from .enums import Action

class UltimateClient(Client):
    def __init__(self, address="http://localhost:6000", disable_warning=False) -> None:
        super(UltimateClient, self).__init__(address, disable_warning)

    def act(self, action: Action):
        url = '{}/ultimate-controller/act'.format(self.address)
        print("action: ", action)
        action["buttons"] = [bt.name for bt in action["buttons"]]
        payload = {"action": action}
        res = requests.post(url, json=payload)

    def move_to_home(self):
        self.reset_game()
        url = '{}/ultimate-controller/move/home'.format(self.address)
        res = requests.post(url)

    def move_to_training(self, config):
        self.move_to_home()
        url = '{}/ultimate-controller/move/training'.format(self.address)
        payload = config
        res = requests.post(url, json=payload)

    def reset_training(self):
        url = '{}/ultimate-controller/reset/training'.format(self.address)
        res = requests.post(url)
