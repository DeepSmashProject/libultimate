from libultimate import UltimateClient, Button

if __name__ == "__main__":
    client = UltimateClient("http://localhost:8008")
    client.add_controller(0)
    for gamestate in client.stream():
        print("gamestate: ", gamestate)
        client.input(0, [Button.A])
