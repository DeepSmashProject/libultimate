//use crate::charge::ChargeState;
use std::io::{Write, Error, ErrorKind};
use serde::{Serialize};
use std::fs::{OpenOptions};

pub trait GameStateTrait {
    fn new() -> GameState;
    fn get_player_state(&mut self, player_id: usize) -> Result<&PlayerState, Error>;
    fn set_player_state(&mut self, player_state: PlayerState) -> Result<usize, Error>;
    fn save(&mut self) -> Result<(), Error>;
}

#[derive(Serialize)]
pub struct GameState{
    pub players: Vec<PlayerState>,
    pub projectiles: Vec<Projectile>,
}

impl GameStateTrait for GameState {
    fn new() -> GameState {
        GameState {
            players: Vec::new(),
            projectiles: Vec::new()
        }
    }

    fn get_player_state(&mut self, player_id: usize) -> Result<&PlayerState, Error>{
        for (i, player) in self.players.iter().enumerate() {
            if player.id == player_id {
                return Ok(player);
            }
        }
        return Err(Error::new(ErrorKind::Other, "player state not found."));
    }

    fn set_player_state(&mut self, player_state: PlayerState) -> Result<usize, Error>{
        for (i, player) in self.players.iter().enumerate() {
            if player.id == player_state.id {
                self.players[i] = player_state;
                return Ok(i);
            }
        }
        self.players.push(player_state);
        return Ok(self.players.len() - 1);
    }

    fn save(&mut self) -> Result<(), Error>{
        let mut file = OpenOptions::new()
            .write(true)
            .create(true)
            .truncate(true)
            .open("sd:/libultimate/game_state.json")?;
        let json = serde_json::to_string(&self)?;
        file.write_all(json.as_bytes())?;
        Ok(())
    }

}

/*#[derive(Serialize, Clone)]
pub struct GameState {
    pub players: Vec<PlayerState>,
    pub projectiles: Vec<Projectile>,
}

impl Default for GameState {
    fn default() -> Self {
        Self {
            players: Vec::new(),
            projectiles: Vec::new(),
        }
    }
}

impl GameState {
    pub fn save(&self){
        let gs_text = serde_json::to_string(&self).expect("game_state serialize error.");
        let file = OpenOptions::new().write(true).truncate(true).open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
        write!(&file, "{}", gs_text).expect("something went wrong reading the file");
    }
}*/

#[derive(Serialize, Clone, Copy)]
pub struct PlayerState{
    pub id: usize,
    pub fighter_kind: i32,
    pub fighter_status_kind: i32,
    pub situation_kind: i32,
    pub lr: f32,
    pub percent: f32,
    //pub stock: i32,
    pub speed: Speed,
    pub position: Position,
    //pub control_state: ControlState,
    pub is_cpu: bool,
    pub is_dead: bool,
    pub frame: f32,
    pub end_frame: f32,
    pub is_actionable: bool,
    //pub fighter_information: FighterInformation,
    //pub charge: ChargeState,
}

#[derive(Serialize, Clone, Copy)]
pub struct FighterInformation{
    pub hit_point: u64,
    pub fighter_color: u64,
    pub is_operation_cpu: bool,
    pub dead_count: u64,
    pub stock_count: u64,
    pub suicide_count: u64,
    pub total_beat_count: u64,
    pub is_last_dead_suicide: bool,
    pub is_on_rebirth: bool,
    pub fighter_category: u64,
    pub gravity: u64
}

#[derive(Serialize, Debug, Clone, Copy)]
pub enum FighterId {
    Player = 0,
    CPU = 1,
}

#[derive(Serialize, Clone, Copy)]
pub struct ControlState{
    pub stick_x: f32,
    pub stick_y: f32,
    pub button_attack: bool,
    pub button_special: bool,
    pub button_smash: bool,
    pub button_guard: bool,
    pub button_guard_hold: bool,
    pub button_catch: bool,
    pub button_jump: bool,
    pub button_jump_mini: bool,
    pub button_invalid: bool,
}

#[derive(Serialize, Clone, Copy)]
pub struct Projectile{

}

#[derive(Serialize, Clone, Copy)]
pub struct Position{
    pub x: f32,
    pub y: f32,
}

#[derive(Serialize, Clone, Copy)]
pub struct Speed{
    pub x: f32,
    pub y: f32,
}
