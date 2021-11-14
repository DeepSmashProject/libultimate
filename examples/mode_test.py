from yuzulib import Runner, Screen
from libultimate import Controller, Action, TrainingMode, Stage, Fighter
import time
import random
runner = Runner("", "", "")
runner.run()

controller = Controller()

training_mode = TrainingMode(
    stage=Stage.STAGE_FINAL_DESTINATION, 
    player=Fighter.FIGHTER_MARIO,
    cpu=Fighter.FIGHTER_DONKEY_KONG,
    cpu_level=7,
)
print("Training Mode")
controller.mode(training_mode)
time.sleep(1)
