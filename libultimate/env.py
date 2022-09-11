from libultimate import Controller, Console, Button, Direction
from enum import Enum
import gym
import time
import threading
from multiprocessing import Process, Pool

class EnvAction(Enum):
    NONE = {"name": "NONE", "func": lambda cont: {}}
    JAB = {"name": "JAB", "func": lambda cont: cont.jab()}
    TILT_U = {"name": "TILT_U", "func": lambda cont: cont.tilt(Direction.UP)}
    TILT_L = {"name": "TILT_L", "func": lambda cont: cont.tilt(Direction.LEFT)}
    TILT_D = {"name": "TILT_D", "func": lambda cont: cont.tilt(Direction.DOWN)}
    TILT_R = {"name": "TILT_R", "func": lambda cont: cont.tilt(Direction.RIGHT)}
    SMASH_U = {"name": "SMASH_U", "func": lambda cont: cont.smash(Direction.UP)}
    SMASH_L = {"name": "SMASH_L", "func": lambda cont: cont.smash(Direction.LEFT)}
    SMASH_D = {"name": "SMASH_D", "func": lambda cont: cont.smash(Direction.DOWN)}
    SMASH_R = {"name": "SMASH_R", "func": lambda cont: cont.smash(Direction.RIGHT)}
    SPECIAL_U = {"name": "SPECIAL_U", "func": lambda cont: cont.special(Direction.UP)}
    SPECIAL_L = {"name": "SPECIAL_L", "func": lambda cont: cont.special(Direction.LEFT)}
    SPECIAL_D = {"name": "SPECIAL_D", "func": lambda cont: cont.special(Direction.DOWN)}
    SPECIAL_R = {"name": "SPECIAL_R", "func": lambda cont: cont.special(Direction.RIGHT)}
    DASH_ATTACK_L = {"name": "DASH_ATTACK_L", "func": lambda cont: cont.dash_attack(lr=False)}
    DASH_ATTACK_R = {"name": "DASH_ATTACK_R", "func": lambda cont: cont.dash_attack(lr=True)}
    SPOT_DODGE = {"name": "SPOT_DODGE", "func": lambda cont: cont.spot_dodge()}
    ROLL_L = {"name": "ROLL_L", "func": lambda cont: cont.roll(lr=False)}
    ROLL_R = {"name": "ROLL_R", "func": lambda cont: cont.roll(lr=True)}
    JUMP = {"name": "JUMP", "func": lambda cont: cont.jump()}
    JUMP_L = {"name": "JUMP_L", "func": lambda cont: cont.jump(lr=False)}
    JUMP_R = {"name": "JUMP_R", "func": lambda cont: cont.jump(lr=True)}
    SHORT_HOP = {"name": "SHORT_HOP", "func": lambda cont: cont.short_hop()}
    SHORT_HOP_L = {"name": "SHORT_HOP_L", "func": lambda cont: cont.short_hop(lr=False)}
    SHORT_HOP_R = {"name": "SHORT_HOP_R", "func": lambda cont: cont.short_hop(lr=True)}
    WALK_L = {"name": "WALK_L", "func": lambda cont: cont.walk(lr=False)}
    WALK_R = {"name": "WALK_R", "func": lambda cont: cont.walk(lr=True)}
    DASH_L = {"name": "DASH_L", "func": lambda cont: cont.dash(lr=False)}
    DASH_R = {"name": "DASH_R", "func": lambda cont: cont.dash(lr=True)}
    GUARD = {"name": "GUARD", "func": lambda cont: cont.guard()}
    GRAB = {"name": "GRAB", "func": lambda cont: cont.grab()}

class UltimateEnv(gym.Env):
    def __init__(self, console: Console, controller: Controller, hz=60, action_space=int(len(EnvAction))):
        super().__init__()
        self.hz = hz
        self.action_space = gym.spaces.Discrete(action_space) 
        self.console = console
        self.controller = controller
        self.gamestate = None
        self.prev_gamestate = None

    def __enter__(self):
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._stream_gamestate)
        self.thread.start()
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("[libultimate] Stopping stream...")
        self.stop_event.set()
        time.sleep(1)

    def _stream_gamestate(self):
        for gamestate in self.console.stream(hz=self.hz):
            self.prev_gamestate = self.gamestate
            self.gamestate = gamestate
            if self.stop_event.is_set():
                break

    def _gamestate_to_observation(self, gamestate):
        return gamestate

    def reset(self, without_reset=False):
        if not without_reset:
            self.controller.input([Button.L, Button.R, Button.A])
        observation = self._gamestate_to_observation(self.gamestate)
        self.controller.release_all()
        time.sleep(1)
        return observation

    def step(self, action):
        action.value["func"](self.controller)
        #self.controller.act(action)
        interval = 60/self.hz * (1/60)
        time.sleep(interval)
        observation = self._gamestate_to_observation(self.gamestate)
        info = self.gamestate
        self.done = self._done(self.gamestate, self.prev_gamestate)
        reward = self._reward(self.done, self.gamestate, self.prev_gamestate)
        self.prev_gamestate = self.gamestate
        return observation, reward, self.done, info

    def render(self, mode='human', close=False):
            print("GameState: {}".format(self.gamestate))

    def _done(self, gamestate, prev_gamestate):
        return (prev_gamestate.players[0].fighter_status_kind != 470 and gamestate.players[0].fighter_status_kind == 470) or (prev_gamestate.players[1].fighter_status_kind != 470 and gamestate.players[1].fighter_status_kind == 470)

    def _reward(self, done, gamestate, prev_gamestate):
        p1_diff_damage = gamestate.players[0].percent - prev_gamestate.players[0].percent
        p2_diff_damage = gamestate.players[1].percent - prev_gamestate.players[1].percent
        reward = p2_diff_damage - p1_diff_damage
        if done:
            if gamestate.players[0].percent == 0:
                reward = -1
            if gamestate.players[1].percent == 0:
                reward = 1
        return reward
