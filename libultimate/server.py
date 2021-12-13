
import sys
import threading
from flask import Flask, Response,stream_with_context, request
from flask_cors import CORS
from .controller import UltimateController
import json
from yuzulib import Server
from libultimate import Action
import time
import numpy as np
import requests
import cv2
from flask_classful import FlaskView, route


class UltimateControllerView(FlaskView):
    controller = UltimateController()
    controller.run()

    @route('/act',methods=["POST"])
    def act(self):
        # curl -X POST -d '{"action": ACTION_JAB}' 'localhost:6000/ultimatecontroller/act'
        req_data = json.loads(request.get_data())
        if "action" not in req_data.keys():
            return Response("ERROR: {} argument is not exist".format("action")), 400
        action = Action[req_data["action"]]
        self.controller.act(action)
        return Response("OK"), 200

    @route('/move/home',methods=["POST"])
    def move_to_home(self):
        # curl -X POST 'localhost:6000/ultimate-controller/move/home'
        self.controller.move_to_home()
        return Response("OK"), 200

    @route('/move/training',methods=["POST"])
    def move_to_training(self):
        # curl -X POST -d '{"buttons": ["BUTTON_A"]}' 'localhost:6000/ultimate-controller/press?hold=True&sec=0&wait=0'
        req_data = json.loads(request.get_data())
        for key in ["stage", "player", "cpu", "setting"]:
            if key not in req_data.keys():
                return Response("ERROR: {} argument is not exist".format(key)), 400
        config = req_data
        self.controller.move_to_training(config)
        return Response("OK"), 200

class UltimateServer(Server):
    def __init__(self, host, port) -> None:
        super(UltimateServer, self).__init__(host, port)
        UltimateControllerView.register(self.app)

    def run(self):
        self.app.debug = False
        self.app.run(host=self.host, port=self.port)

if __name__ == '__main__':
    server = UltimateServer(host='0.0.0.0', port=6000)
    server.run()