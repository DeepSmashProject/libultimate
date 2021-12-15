
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
    def _process(self, screen_data):
        return screen_data

if __name__ == '__main__':
    server = Server(host='0.0.0.0', port=7000, views=[ControllerView, RunnerView, ScreenView, UltimateControllerView])
    server.run()