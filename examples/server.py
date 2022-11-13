from libultimate import UltimateServer, UltimateServerConfig, Console

if __name__ == "__main__":
    RYUJINX_PATH = "/path/to/Ryujinx" # ex: /home/username/.config/Ryujinx
    with Console(ryujinx_path=RYUJINX_PATH) as console:
        config = UltimateServerConfig(fps=5)
        server = UltimateServer(console, config)
        server.run(address="localhost", port=8000)
