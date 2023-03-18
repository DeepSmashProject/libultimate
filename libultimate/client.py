from typing import List
from .enums import Button
import requests

class UltimateClient:
    def __init__(self, server_address: str):
        self.server_address = server_address
        
    def _get(self, path: str):
        url = '{}{}'.format(self.server_address, path)
        response = requests.get(url)
        return response
    
    def _post(self, path: str, data: dict):
        url = '{}{}'.format(self.server_address, path)
        response = requests.post(url, data=data)
        return response

    def add_controller(self, player_id: int):
        self._post("/controller/add", {"player_id": player_id})

    def input(self, player_id: int, buttons: List[Button]=[], main_stick = (0, 0), c_stick = (0, 0), hold = False):
        buttons_total = int(sum([btn.value for btn in buttons]))
        self._post("/controller/input", {
            "player_id": player_id,
            "buttons: ": buttons_total,
            "main_stick": main_stick,
            "c_stick": c_stick,
            "hold": hold,
        })
        
    def stream(self):
        try:
            yield from self._get("/stream/game_state")
        except Exception as err:
            self.logger.warning("couldn't read state: {}".format(err))
