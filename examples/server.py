from libultimate import UltimateServer, Console

if __name__ == "__main__":
    SDCARD_PATH = "~/YOUR_SDCARD_PATH" # ex: if Ryujinx: ~/.config/Ryujinx, if Yuzu: ~/.local/share/yuzu/sdmc
    with Console(sdcard_path=SDCARD_PATH) as console:
        server = UltimateServer(console)
        server.run(address="0.0.0.0", port=8008)
