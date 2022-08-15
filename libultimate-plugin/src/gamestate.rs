//use crate::charge::ChargeState;
use std::io::{Write};
use serde::{Serialize};
use std::fs::{OpenOptions};

#[derive(Serialize, Clone)]
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
    pub fn update_player_state(&self, player_state: PlayerState) -> GameState {
        let mut index: i32 = -1;
        let mut players = self.players.clone();
        for (i, ps) in self.players.iter().enumerate(){
            if ps.id == player_state.id{
                index = i as i32;
            }
        }
        if index < 0 {
            // not exist
            players.push(player_state);
        }else{
            // exist
            players[index as usize] = player_state;
        }
        GameState {
            players: players,
            projectiles: Vec::new(),
        }
    }

    pub fn save(&self){
        let gs_text = serde_json::to_string(&self).expect("game_state serialize error.");
        let file = OpenOptions::new().write(true).truncate(true).open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
        write!(&file, "{}", gs_text).expect("something went wrong reading the file");
    }
}

#[derive(Serialize, Clone, Copy)]
pub struct PlayerState{
    pub id: i32,
    pub fighter_kind: i32,
    pub fighter_status_kind: i32,
    pub situation_kind: i32,
    pub lr: f32,
    pub percent: f32,
    //pub stock: i32,
    pub position: Position,
    pub control_state: ControlState,
    pub is_cpu: bool,
    pub is_dead: bool,
    //pub charge: ChargeState,
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
