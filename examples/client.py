from libultimate import UltimateClient, Button
import json
if __name__ == "__main__":
    client = UltimateClient("http://localhost:8008")
    client.add_controller(0)
    for gamestate in client.stream(fps=5, include_image=True, image_size=(256, 256)):
        print("gamestate: ", gamestate.players[0].position, gamestate.image.shape)
        client.input(0, [Button.A])
