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
