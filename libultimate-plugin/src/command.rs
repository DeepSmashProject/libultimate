//use crate::charge::ChargeState;
use std::io::{Write, BufReader, Error, ErrorKind};
use serde::{Serialize, Deserialize};
use std::fs::{OpenOptions, File};
use std::fs;
use std::path::Path;

#[derive(Serialize, Deserialize, Clone)]
pub enum Action {
    AIR_DODGE,
    TILT_U,
    TILT_F,
    TILT_D,
    SMASH_U,
    SMASH_F,
    SMASH_D,
    JAB,
    GRAB,
    DASH,
    SPOT_DODGE,
    ROLL_B,
    ROLL_F,
    JUMP,
    SPECIAL_U,
    SPECIAL_D,
    SPECIAL_N,
    SPECIAL_F,
    TURN,
    TURN_DASH,
    WALK,
    GUARD,
    THROW_B,
    THROW_F,
    THROW_U,
    THROW_D,
    DASH_ATTACK,
    NONE,
}

#[derive(Serialize, Deserialize, Clone)]
pub struct Command {
    pub id: String,
    pub player_id: u32,
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
    pub fn get(entry_id: u32) -> Result<Command, Error>{
        let mut command: Command = Command::default();
        let command_ok_path = format!("sd:/libultimate/command_{}.ok.json", entry_id);
        let command_path = format!("sd:/libultimate/command_{}.json", entry_id);
        if Path::new(&command_ok_path).exists() {
            let file = File::open(&command_path)?;
            let reader = BufReader::new(file);
            command = serde_json::from_reader(reader)?;
            // remove ok.json
            fs::remove_file(&command_ok_path).unwrap();
        }else{
            return Err(Error::new(ErrorKind::Other, "command.json does not exist"));
        }
        return Ok(command);
    }
}
