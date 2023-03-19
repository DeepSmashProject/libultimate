from typing import List
from .enums import Button
from .schemas import GameState
import requests
import json

class UltimateClient:
    def __init__(self, server_address: str):
        self.server_address = server_address
        
    def _get(self, path: str, stream: bool = False):
        url = '{}{}'.format(self.server_address, path)
        response = requests.get(url, stream=stream)
        return response
    
    def _post(self, path: str, data: dict):
        url = '{}{}'.format(self.server_address, path)
        headers = {"content-type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response

    def add_controller(self, player_id: int):
        self._post("/controller/add", {"player_id": player_id})

    def input(self, player_id: int, buttons: List[Button]=[], main_stick = (0, 0), c_stick = (0, 0), hold = False):
        self._post("/controller/input", {
            "player_id": player_id,
            "buttons": [btn.value for btn in buttons],
            "main_stick": {"stick_x": main_stick[0], "stick_y": main_stick[1]},
            "c_stick": {"stick_x": c_stick[0], "stick_y": c_stick[1]},
            "hold": hold,
        })
        
    def stream(self, fps: int = 10, include_image: bool = False, image_size: tuple = None):
        def generate():
            try:
                endpoint = "/stream/game_state?fps={}&include_image={}".format(fps, include_image)
                if image_size:
                    endpoint += "&image_size={}".format(image_size)
                res = self._get(endpoint, stream=True)
                json_str = ""
                for chunk in res.iter_content(chunk_size=1024):
                    if chunk:
                        data = chunk.decode('utf-8')
                        for line in data.split('\n'):
                            if line:
                                json_str += line
                                try:
                                    result = json.loads(json_str)
                                    json_str = ""
                                    yield GameState.parse_obj(json.loads(result))
                                except Exception as err:
                                    pass
            except Exception as err:
                print(err)
        return generate()
