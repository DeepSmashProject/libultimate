//use crate::charge::ChargeState;
use std::io::{Write};
use serde::{Serialize, Deserialize};
use std::fs::{OpenOptions};
use std::fs;

#[derive(Serialize, Deserialize, Clone)]
pub enum Action {
    AIR_ESCAPE = 0,
    ATTACK_HI3 = 1,
    ATTACK_HI4 = 2,
    ATTACK_LW3 = 3,
    ATTACK_LW4 = 4,
    ATTACK_N = 5,
    ATTACK_S3 = 6,
    ATTACK_S4 = 7,
    CATCH = 8,
    DASH = 9,
    ESCAPE = 10,
    ESCAPE_B = 11,
    ESCAPE_F = 12,
    JUMP = 13,
    JUMP_BUTTON = 14,
    SPECIAL_ANY = 15,
    SPECIAL_HI = 16,
    SPECIAL_LW = 17,
    SPECIAL_N = 18,
    SPECIAL_S = 19,
    TURN = 20,
    TURN_DASH = 21,
    WALK = 22,
    WALL_JUMP_LEFT = 23,
    WALL_JUMP_RIGHT  = 24,
}

#[derive(Serialize, Deserialize, Clone)]
pub struct Command {
    pub id: i32,
    pub action: Action,
}

impl Default for Command {
    fn default() -> Self {
        Self {
            id: 0,
            action: Action::ATTACK_N,
        }
    }
}

impl Command {
    pub fn get() -> Command{
        //let gs_text = serde_json::to_string(&self).expect("game_state serialize error.");
        //let file = OpenOptions::new().write(true).truncate(true).open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
        //write!(&file, "{}", gs_text).expect("something went wrong reading the file");
        let content = fs::read_to_string("sd:/libultimate/game_state.json").expect("Failed to load JSON");
        let command: Command = serde_json::from_str(&content).unwrap();
        return command;
    }
}
