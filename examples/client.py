from libultimate import UltimateClient, Button
import json
if __name__ == "__main__":
    client = UltimateClient("http://localhost:8008")
    #client.add_controller(0)
    #client.input(0, [Button.A])
    for gamestate in client.stream(fps=5):
        print("gamestate: ", gamestate.players[0].position)
    #    client.input(0, [Button.A])
