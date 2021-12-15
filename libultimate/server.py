
import sys
import threading
from flask import Flask, Response,stream_with_context, request
from flask_cors import CORS
from .controller import UltimateController
import json
from yuzulib.server import Server, ControllerView, RunnerView, ScreenView as YuzuScreenView
from libultimate.enums import Action
from flask_classful import FlaskView, route
import copy
import torch
from .model import  NetV5
from collections import deque

class UltimateControllerView(FlaskView):
    controller = UltimateController()

    @route('/act',methods=["POST"])
    def act(self):
        # curl -X POST -d '{"action": "ACTION_JAB"}' 'localhost:6000/ultimate-controller/act'
        req_data = json.loads(request.get_data())
        if "action" not in req_data.keys():
            return Response("ERROR: {} argument is not exist".format("action")), 400
        action = copy.deepcopy(req_data["action"])
        action = getattr(Action, action)
        self.controller.act(action)
        return Response("OK"), 200

    @route('/move/home',methods=["POST"])
    def move_to_home(self):
        # curl -X POST 'localhost:6000/ultimate-controller/move/home'
        self.controller.move_to_home()
        return Response("OK"), 200

    @route('/move/training',methods=["POST"])
    def move_to_training(self):
        # curl -X POST -d '{"stage": ,}' 'localhost:6000/ultimate-controller/move/training'
        req_data = json.loads(request.get_data())
        for key in ["stage", "player", "cpu", "setting"]:
            if key not in req_data.keys():
                return Response("ERROR: {} argument is not exist".format(key)), 400
        config = req_data
        self.controller.move_to_training(config)
        return Response("OK"), 200

    @route('/reset/training',methods=["POST"])
    def reset_training(self):
        # curl -X POST 'localhost:6000/ultimate-controller/reset/training'
        self.controller.reset_training()
        return Response("OK"), 200

class ScreenView(YuzuScreenView):
    device = torch.device("cpu")
    model = NetV5().to(device)
    model.load()
    p1_d_buffer = deque([], 2)
    p2_d_buffer = deque([], 2)
    p1_damage = 0
    p2_damage = 0
    p1_damaged_or_killed_flag = False
    p2_damaged_or_killed_flag = False
    def _process(self, screen_data, req_data):
        # get damage
        damage, diff_damage, kill = self._get_damage(screen_data["frame"])
        screen_data["info"] = {"damage": damage, "diff_damage": diff_damage, "kill": kill}
        return screen_data

    def _get_damage(self, observation):
        # read damage from observation
        #p1_damage_obs = (observation[414:444, 127:151], observation[414:444, 149:173], observation[414:444, 171:195]) #[y,x]
        #p2_damage_obs = (observation[414:444, 309:333], observation[414:444, 331:355], observation[414:444, 353:377]) #[y,x] 
        p1_damage_obs = (observation[411:441, 124:148], observation[411:441, 146:170], observation[411:441, 168:192]) #[y,x]
        p2_damage_obs = (observation[411:441, 306:330], observation[411:441, 328:352], observation[411:441, 350:374]) #[y,x] 
        p1_damage = self.model.predict_damage(p1_damage_obs)
        p2_damage = self.model.predict_damage(p2_damage_obs)
        self.p1_d_buffer.append(p1_damage)
        self.p2_d_buffer.append(p2_damage)
        p1_diff_damage = 0
        p2_diff_damage = 0
        p1_killed = False
        p2_killed = False
        if self.p1_d_buffer.count(self.p1_damage) == 0 and self.p1_d_buffer.count(999) == 0 and p1_damage != self.p1_damage:
            p1_diff_damage = p1_damage - self.p1_damage
            if p1_diff_damage > 0:
                self.p1_damage = p1_damage
            else:
                p1_diff_damage = 0
            # kill or not
            if self.p1_damaged_or_killed_flag and p1_damage == 0:
                p1_killed = True
                self.p1_damage = 0
        if self.p2_d_buffer.count(self.p2_damage) == 0 and self.p2_d_buffer.count(999) == 0 and p2_damage != self.p2_damage:
            p2_diff_damage = p2_damage - self.p2_damage
            if p2_diff_damage > 0:
                self.p2_damage = p2_damage
            else:
                p2_diff_damage = 0
            # kill or not
            if self.p2_damaged_or_killed_flag and p2_damage == 0:
                p2_killed = True
                self.p2_damage = 0

        # killed flag
        if self.p1_d_buffer.count(999) >= len(self.p1_d_buffer):
            self.p1_damaged_or_killed_flag = True
        if self.p2_d_buffer.count(999) >= len(self.p2_d_buffer):
            self.p2_damaged_or_killed_flag = True
            
        return (self.p1_damage, self.p2_damage), (p1_diff_damage, p2_diff_damage), (p1_killed, p2_killed)


if __name__ == '__main__':
    server = Server(host='0.0.0.0', port=7000, views=[ControllerView, RunnerView, ScreenView, UltimateControllerView])
    server.run()