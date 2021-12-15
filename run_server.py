import argparse
from libultimate.server import ScreenView, UltimateControllerView
from yuzulib.server import Server, ControllerView, RunnerView
parser = argparse.ArgumentParser(description='')
parser.add_argument('--host')
parser.add_argument('--port')

args = parser.parse_args()
print("Running Ultimate Server at {}:{}".format(args.host, args.port))
server = Server(host=str(args.host), port=int(args.port), views=[ControllerView, RunnerView, ScreenView, UltimateControllerView])
server.run()