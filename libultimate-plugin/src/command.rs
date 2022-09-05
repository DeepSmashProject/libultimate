//use crate::charge::ChargeState;
use std::io::{Write, BufReader};
use serde::{Serialize, Deserialize};
use std::fs::{OpenOptions, File};
use std::fs;
use std::path::Path;

#[derive(Serialize, Deserialize, Clone)]
pub enum Action {
    AIR_ESCAPE,
    ATTACK_HI3,
    ATTACK_HI4,
    ATTACK_LW3,
    ATTACK_LW4,
    ATTACK_N,
    ATTACK_S3,
    ATTACK_S4,
    CATCH,
    DASH,
    ESCAPE,
    ESCAPE_B,
    ESCAPE_F,
    JUMP,
    JUMP_BUTTON,
    SPECIAL_ANY,
    SPECIAL_HI,
    SPECIAL_LW,
    SPECIAL_N,
    SPECIAL_S,
    TURN,
    TURN_DASH,
    WALK,
    WALL_JUMP_LEFT,
    WALL_JUMP_RIGHT,
    NONE,
}

#[derive(Serialize, Deserialize, Clone)]
pub struct Command {
    pub id: String,
    pub player_id: i32,
    pub action: Action,
}

impl Default for Command {
    fn default() -> Self {
        Self {
            id: "".to_string(),
            player_id: 0,
            action: Action::NONE,
        }
    }
}

impl Command {
    pub fn get() -> Command{
        let mut command: Command = Command::default();
        if Path::new("sd:/libultimate/command.ok.json").exists() {
            let file = File::open("sd:/libultimate/command.json").expect("Failed to load JSON");
            let reader = BufReader::new(file);
            command = match serde_json::from_reader(reader){
                Ok(command) => command,
                Err(e) => Command::default(),
            };
            // remove ok.json
            fs::remove_file("sd:/libultimate/command.ok.json").unwrap();
        }
        return command;
    }
}
