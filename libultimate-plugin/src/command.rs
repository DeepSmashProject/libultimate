//use crate::charge::ChargeState;
use std::io::{Write, BufReader, Error};
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
    pub stick_x: f32, // -1 ~ 1
    pub stick_y: f32, // -1 ~ 1
}

impl Default for Command {
    fn default() -> Self {
        Self {
            id: "".to_string(),
            player_id: 0,
            action: Action::NONE,
            stick_x: 0.0,
            stick_y: 0.0,
        }
    }
}

impl Command {
    pub fn get(entry_id: i32) -> Result<Command, Error>{
        let mut command: Command = Command::default();
        let command_ok_path = format!("sd:/libultimate/command_{}.ok.json", entry_id);
        let command_path = format!("sd:/libultimate/command_{}.json", entry_id);
        if Path::new(&command_ok_path).exists() {
            let file = File::open(&command_path)?;
            let reader = BufReader::new(file);
            command = match serde_json::from_reader(reader){
                Ok(command) => command,
                Err(e) => Command::default(),
            };
            // remove ok.json
            fs::remove_file(&command_ok_path).unwrap();
        }
        return Ok(command);
    }

    pub fn update(mut self, command: Command){
        self.id = command.id;
        self.player_id = command.player_id;
        self.action = command.action;
        self.stick_x = command.stick_x;
        self.stick_y = command.stick_y;
    }
}
