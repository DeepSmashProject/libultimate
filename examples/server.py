from libultimate import UltimateServer, UltimateServerConfig, Console

if __name__ == "__main__":
    SDCARD_PATH = "~/YOUR_SDCARD_PATH" # ex: if Ryujinx: ~/.config/Ryujinx, if Yuzu: ~/.local/share/yuzu/sdmc
    with Console(sdcard_path=SDCARD_PATH) as console:
        config = UltimateServerConfig(fps=5)
        server = UltimateServer(console, config)
        server.run(address="localhost", port=8000)
