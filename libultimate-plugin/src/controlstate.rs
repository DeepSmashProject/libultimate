//use crate::charge::ChargeState;
use std::io::{Write, BufReader, Error};
use serde::{Serialize, Deserialize};
use std::fs::{OpenOptions, File};
use std::fs;
use std::path::Path;

#[derive(Serialize, Deserialize, Clone)]
pub struct ControlState {
    pub id: String,
    pub player_id: u32,
    pub update_count: i64,
    pub buttons: u64,
    pub l_stick_x: i32,
    pub l_stick_y: i32,
    pub r_stick_x: i32,
    pub r_stick_y: i32,
    pub flags: u32,
    pub l_trigger: u32,
    pub r_trigger: u32,
}

impl Default for ControlState {
    fn default() -> Self {
        Self {
            id: "".to_string(),
            player_id: 0,
            update_count: 0,
            buttons: 0,
            l_stick_x: 0,
            l_stick_y: 0,
            r_stick_x: 0,
            r_stick_y: 0,
            flags: 0,
            l_trigger: 0,
            r_trigger: 0,
        }
    }
}

impl ControlState {
    pub fn get(entry_id: i32) -> Result<ControlState, Error>{
        let mut control_state: ControlState = ControlState::default();
        let control_state_ok_path = format!("sd:/libultimate/control_state_{}.ok.json", entry_id);
        let control_state_path = format!("sd:/libultimate/control_state_{}.json", entry_id);
        if Path::new(&control_state_ok_path).exists() {
            let file = File::open(&control_state_path)?;
            let reader = BufReader::new(file);
            control_state = match serde_json::from_reader(reader){
                Ok(control_state) => control_state,
                Err(_) => ControlState::default(),
            };
            // remove ok.json
            fs::remove_file(&control_state_ok_path).unwrap();
        }
        return Ok(control_state);
    }

    /*pub fn update(mut self, command: Command){
        self.id = command.id;
        self.player_id = command.player_id;
        self.action = command.action;
        self.stick_x = command.stick_x;
        self.stick_y = command.stick_y;
    }*/
}
