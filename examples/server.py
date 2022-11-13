from libultimate import UltimateServer, Console

if __name__ == "__main__":
    RYUJINX_PATH = "/path/to/Ryujinx" # ex: /home/username/.config/Ryujinx
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        server = UltimateServer(console)
        server.run(address="localhost", port=8000)
