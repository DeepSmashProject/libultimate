import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import grpc
from proto.libultimate_pb2 import ControlProps, GameStateProps
from proto.libultimate_pb2_grpc import LibUltimateStub
from contextlib import contextmanager     

class Console():
    def __init__(self, address="0.0.0.0:10000"):
        self.address=address

    def run(self):
        pass

    @contextmanager
    def connect(self):
        self.channel = grpc.insecure_channel(self.address)
        self.stub = LibUltimateStub(self.channel)
        print("opened connection!: {}".format(self.address))
        try:
            yield
        finally:
            self.channel.close()
            print("closed connection!: {}".format(self.address))

    def stream(self, hz=60):
        for res in self.stub.GetGameState(GameStateProps(hz=hz)):
            yield res

    def operateController(self):
        res = self.stub.OperateController(ControlProps(message="test"))
        return res

class Controller():
    def __init__(self, console: Console, port: int=1):
        self.console = console
        self.port = port

    def press(self):
        res = self.console.operateController()
        return res

    def release(self):
        res = self.console.operateController()
        return res

    def release_all(self):
        res = self.console.operateController()
        return res

if __name__ == "__main__":
    console = Console(address="0.0.0.0:10000")
    controller = Controller(console=console, port=1)

    for gamestate in console.stream():
        print("gamestate: ", gamestate.message)
        result = controller.press()
        print("controled: ", result.message)
