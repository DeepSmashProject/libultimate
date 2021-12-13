import argparse
from libultimate import UltimateServer

parser = argparse.ArgumentParser(description='')
parser.add_argument('--host')
parser.add_argument('--port')

args = parser.parse_args()
print("Running Server at {}:{}".format(args.host, args.port))
server = UltimateServer(host=str(args.host), port=int(args.port))
server.run()