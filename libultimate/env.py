from libultimate import Controller, Console, Button, Direction
from enum import Enum
import gym
import time
import threading

class EnvAction(Enum):
    NONE = 0
    JAB = lambda cont: cont.jab()
    TILT_U = lambda cont: cont.tilt(Direction.UP)
    TILT_L = lambda cont: cont.tilt(Direction.LEFT)
    TILT_D = lambda cont: cont.tilt(Direction.DOWN)
    TILT_R = lambda cont: cont.tilt(Direction.RIGHT)
    SMASH_U = lambda cont: cont.smash(Direction.UP)
    SMASH_L = lambda cont: cont.smash(Direction.LEFT)
    SMASH_D = lambda cont: cont.smash(Direction.DOWN)
    SMASH_R = lambda cont: cont.smash(Direction.RIGHT)
    SPECIAL_U = lambda cont: cont.special(Direction.UP)
    SPECIAL_L = lambda cont: cont.special(Direction.LEFT)
    SPECIAL_D = lambda cont: cont.special(Direction.DOWN)
    SPECIAL_R = lambda cont: cont.special(Direction.RIGHT)
    DASH_ATTACK_L = lambda cont: cont.dash_attack(lr=False)
    DASH_ATTACK_R = lambda cont: cont.dash_attack(lr=True)
    SPOT_DODGE = lambda cont: cont.spot_dodge()
    ROLL_L = lambda cont: cont.roll(lr=False)
    ROLL_R = lambda cont: cont.roll(lr=True)
    JUMP = lambda cont: cont.jump()
    JUMP_L = lambda cont: cont.jump(lr=False)
    JUMP_R = lambda cont: cont.jump(lr=True)
    SHORT_HOP = lambda cont: cont.short_hop()
    SHORT_HOP_L = lambda cont: cont.short_hop(lr=False)
    SHORT_HOP_R = lambda cont: cont.short_hop(lr=True)
    WALK_L = lambda cont: cont.walk(lr=False)
    WALK_R = lambda cont: cont.walk(lr=True)
    DASH_L = lambda cont: cont.dash(lr=False)
    DASH_R = lambda cont: cont.dash(lr=True)
    GUARD = lambda cont: cont.guard()
    GRAB = lambda cont: cont.grab()

class UltimateEnv(gym.Env):
    def __init__(self, console: Console, controller: Controller, hz=60, action_space=int(len(Action))):
        super().__init__()
        self.hz = hz
        self.action_space = gym.spaces.Discrete(action_space) 
        self.console = console
        self.controller = controller
        self.gamestate = None
        self.prev_gamestate = None
        self.run()

    def run(self):
        thread = threading.Thread(target=self._stream_gamestate)
        thread.start()
        time.sleep(1)

    def _stream_gamestate(self):
        for gamestate in self.console.stream(hz=self.hz):
            self.prev_gamestate = self.gamestate
            self.gamestate = gamestate

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
        action.value(self.controller)
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
        return prev_gamestate.players[0].is_dead or prev_gamestate.players[1].is_dead

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
