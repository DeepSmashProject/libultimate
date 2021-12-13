from libultimate import UltimateClient, Action

def show_screen():
    client = UltimateClient(address="http://localhost:6000", disable_warning=True)
    def callback(frame, fps):
        print("get", fps, frame.shape)
        client.act(Action.ACTION_JAB)
    client.run_screen(callback, fps=15, render=True, width=500, height=300)

def move_training_test():
    print("run game")
    client = UltimateClient(address="http://localhost:6000", disable_warning=True)
    client.move_to_home()
    #client.move_to_training()
    #client.reset_game()

def run_game_test():
    print("run game")
    game_path = "/workspace/games/SSBU/Super Smash Bros Ultimate [v0].nsp"
    dlc_dir = "/workspace/games/SSBU/DLC"
    client = UltimateClient(address="http://localhost:6000", disable_warning=True)
    client.run_game(game_path, dlc_dir)
    #client.move_to_training()
    #client.reset_game()

if __name__ == "__main__":
    #show_screen()
    move_training_test()
    #run_game_test()
    # TODO: async callback
    # TODO: RunnerView