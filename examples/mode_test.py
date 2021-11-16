from yuzulib import Runner, Screen
from libultimate import Controller, Action, TrainingMode, Stage, Fighter
import time
import random
#runner = Runner("", "")
#runner.run()

controller = Controller()
controller.move_to_home()

training_mode = TrainingMode(
    controller=controller,
    stage=Stage.STAGE_FINAL_DESTINATION, 
    player=Fighter.FIGHTER_MARIO,
    cpu=Fighter.FIGHTER_DONKEY_KONG,
    cpu_level=7,
)
print("Training Mode")
training_mode.start()
time.sleep(1)
