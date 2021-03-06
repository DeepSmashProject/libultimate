from libultimate.client import UltimateClient
from libultimate.enums import Action, Stage, Fighter
def show_screen():
    client = UltimateClient(address="http://localhost:6000", disable_warning=True)
    def callback(frame, fps, info):
        print("get", fps, frame.shape, info)
        client.act(Action.ACTION_JAB)
    client.run_screen(callback, fps=15, render=False, width=500, height=300, grayscale=False)

def move_training_test():
    print("move training")
    client = UltimateClient(address="http://localhost:6000", disable_warning=True)
    #client.move_to_home()
    config = {
            "stage": Stage.STAGE_HANENBOW.name, 
            "player": {"fighter": Fighter.FIGHTER_MARIO.name, "color": 0}, 
            "cpu": {"fighter": Fighter.FIGHTER_DONKEY_KONG.name, "color": 0, "level": 9},
            "setting": {"quick_mode": True, "cpu_behavior": "cpu", "diable_combo_display": True}
        }
    client.move_to_training(config)
    #client.reset_game()

def move_home_test():
    print("move home")
    client = UltimateClient(address="http://localhost:6000", disable_warning=True)
    client.move_to_home()

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
    run_game_test()
    move_training_test()
    #move_home_test()
    # TODO: async callback
    # TODO: RunnerView