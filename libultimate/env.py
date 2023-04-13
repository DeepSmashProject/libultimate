from .enums import Button
from .client import UltimateClient
from enum import Enum
import gym
import time
import threading
import cv2
import random
import numpy as np

class EnvAction(Enum):
    NONE = {"name": "NONE", "input": {"buttons": [], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    JAB = {"name": "JAB", "input": {"buttons": [Button.A], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    TILT_U = {"name": "TILT_U", "input": {"buttons": [Button.A], "main_stick": (0, 0.5), "c_stick": (0, 0), "hold": False}}
    TILT_L = {"name": "TILT_L", "input": {"buttons": [Button.A], "main_stick": (-0.5, 0), "c_stick": (0, 0), "hold": False}}
    TILT_D = {"name": "TILT_D", "input": {"buttons": [Button.A], "main_stick": (0, -0.5), "c_stick": (0, 0), "hold": False}}
    TILT_R = {"name": "TILT_R", "input": {"buttons": [Button.A], "main_stick": (0.5, 0), "c_stick": (0, 0), "hold": False}}
    SMASH_U = {"name": "SMASH_U", "input": {"buttons": [Button.A], "main_stick": (0, 1), "c_stick": (0, 0), "hold": False}}
    SMASH_L = {"name": "SMASH_L", "input": {"buttons": [Button.A], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": False}}
    SMASH_D = {"name": "SMASH_D", "input": {"buttons": [Button.A], "main_stick": (0, -1), "c_stick": (0, 0), "hold": False}}
    SMASH_R = {"name": "SMASH_R", "input": {"buttons": [Button.A], "main_stick": (1, 0), "c_stick": (0, 0), "hold": False}}
    SPECIAL_N = {"name": "SPECIAL_N", "input": {"buttons": [Button.B], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    SPECIAL_UL = {"name": "SPECIAL_UL", "input": {"buttons": [Button.B], "main_stick": (-1, 1), "c_stick": (0, 0), "hold": True}}
    SPECIAL_UR = {"name": "SPECIAL_UR", "input": {"buttons": [Button.B], "main_stick": (1, 1), "c_stick": (0, 0), "hold": True}}
    SPECIAL_L = {"name": "SPECIAL_L", "input": {"buttons": [Button.B], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": False}}
    SPECIAL_D = {"name": "SPECIAL_D", "input": {"buttons": [Button.B], "main_stick": (0, -1), "c_stick": (0, 0), "hold": False}}
    SPECIAL_R = {"name": "SPECIAL_R", "input": {"buttons": [Button.B], "main_stick": (1, 0), "c_stick": (0, 0), "hold": False}}
    SPOT_DODGE = {"name": "SPOT_DODGE", "input": {"buttons": [Button.ZR], "main_stick": (0, -1), "c_stick": (0, 0), "hold": False}}
    ROLL_L = {"name": "ROLL_L", "input": {"buttons": [Button.ZR], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": False}}
    ROLL_R = {"name": "ROLL_R", "input": {"buttons": [Button.ZR], "main_stick": (1, 0), "c_stick": (0, 0), "hold": False}}
    JUMP = {"name": "JUMP", "input": {"buttons": [Button.X], "main_stick": (0, 0), "c_stick": (0, 0), "hold": True}}
    JUMP_L = {"name": "JUMP_L", "input": {"buttons": [Button.X], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": True}}
    JUMP_R = {"name": "JUMP_R", "input": {"buttons": [Button.X], "main_stick": (1, 0), "c_stick": (0, 0), "hold": True}}
    SHORT_HOP = {"name": "SHORT_HOP", "input": {"buttons": [Button.X, Button.Y], "main_stick": (0, 0), "c_stick": (0, 0), "hold": True}}
    SHORT_HOP_L = {"name": "SHORT_HOP_L", "input": {"buttons": [Button.X, Button.Y], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": True}}
    SHORT_HOP_R = {"name": "SHORT_HOP_R", "input": {"buttons": [Button.X, Button.Y], "main_stick": (1, 0), "c_stick": (0, 0), "hold": True}}
    WALK_L = {"name": "WALK_L", "input": {"buttons": [], "main_stick": (-0.5, 0), "c_stick": (0, 0), "hold": True}}
    WALK_R = {"name": "WALK_R", "input": {"buttons": [], "main_stick": (0.5, 0), "c_stick": (0, 0), "hold": True}}
    DASH_L = {"name": "DASH_L", "input": {"buttons": [], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": True}}
    DASH_R = {"name": "DASH_R", "input": {"buttons": [], "main_stick": (1, 0), "c_stick": (0, 0), "hold": True}}
    GUARD = {"name": "GUARD", "input": {"buttons": [Button.ZR], "main_stick": (0, 0), "c_stick": (0, 0), "hold": True}}
    GRAB = {"name": "GRAB", "input": {"buttons": [Button.L], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    
    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

class UltimateEnv(gym.Env):
    def __init__(self, server_url="http://localhost:8008", fps=10, image_size=(256, 256), disable_percent_reset=False, obs_key='image'):
        super().__init__()
        self.action_space = gym.spaces.Discrete(len(EnvAction))
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(image_size[1], image_size[0], 3), dtype=np.uint8)
        self.fps = fps
        self.image_size = image_size
        self.disable_percent_reset = disable_percent_reset
        self.client = UltimateClient(server_url)
        self.client.add_controller(0)
        self.obs_key = obs_key # 'image' or 'vector'
        self.gamestate = None
        self.prev_gamestate = None
        self.dead = {0: False, 1: False}
        self.reward = 0
        self.done = False

    def __enter__(self):
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._stream_gamestate)
        self.thread.start()
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("[libultimate] Stopping stream...")
        self.stop_event.set()
        cv2.destroyAllWindows()
        self.client.input(0)
        time.sleep(1)

    def _stream_gamestate(self):
        for gamestate in self.client.stream(fps=self.fps*2, include_image=self.obs_key=='image', image_size=self.image_size):
            self.prev_gamestate = self.gamestate
            self.gamestate = gamestate
            if self.gamestate.players[0].fighter_status_kind != 470 and self.prev_gamestate and self.prev_gamestate.players[0].fighter_status_kind == 470:
                self.dead[0] = True
            if self.gamestate.players[1].fighter_status_kind != 470 and self.prev_gamestate and self.prev_gamestate.players[1].fighter_status_kind == 470:
                self.dead[1] = True
            self.done = self._done()
            self.reward = self._reward(self.reward, self.done, self.gamestate, self.prev_gamestate)
            if self.stop_event.is_set():
                break

    def _gamestate_to_observation(self, gamestate):
        return gamestate.image

    def reset(self):
        if not self.disable_percent_reset:
            self.client.input(0, [Button.L, Button.R, Button.A])
        observation = self._gamestate_to_observation(self.gamestate)
        self.client.input(0)
        time.sleep(1)
        self.dead = {0: False, 1: False}
        self.reward = 0
        self.done = False
        return observation

    def step(self, action_num: int):
        input = EnvAction[EnvAction.get_names()[action_num]].value["input"]
        self.client.input(0, input["buttons"], input["main_stick"], input["c_stick"], input["hold"])
        interval = 1/self.fps
        time.sleep(interval)
        observation = self._gamestate_to_observation(self.gamestate)
        info = {"state": self.gamestate}
        self.prev_gamestate = self.gamestate
        reward = self.reward
        self.reward = 0
        return observation, reward, self.done, info

    def render(self, mode='human', close=False):
        cv2.imshow('camera' , self.gamestate.image)
        key =cv2.waitKey(10)
        if key == 27:
            raise KeyboardInterrupt

    def _done(self):
        return self.dead[0] or self.dead[1]

    def _reward(self, prev_reward, done, gamestate, prev_gamestate):
        if self.gamestate is None or self.prev_gamestate is None:
            return 0
        p1_diff_damage = gamestate.players[0].percent - prev_gamestate.players[0].percent
        p2_diff_damage = gamestate.players[1].percent - prev_gamestate.players[1].percent
        reward = prev_reward + (p2_diff_damage - p1_diff_damage)
        if done:
            if self.dead[0]:
                reward = -100
            if self.dead[1]:
                reward = 100
        return reward

if __name__ == "__main__":
    with UltimateEnv(server_url="http://localhost:8008", fps=10, image_size=(84, 84), disable_percent_reset=False) as env:
        episode = 1000
        for i in range(episode):
            print("episode: ", i)
            env.reset()
            done = False
            while not done:
                env.render()
                random_action_num = np.random.randint(0, len(EnvAction))
                observation, reward, done, info = env.step(random_action_num)
                print(done, reward)