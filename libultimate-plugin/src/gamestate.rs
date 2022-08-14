use crate::charge::ChargeState;
use std::fs;
use std::io::{self, Read, Write, BufReader};
use serde::{Serialize};
use std::fs::{File, OpenOptions};
use std::cell::Cell;

#[derive(Serialize, Clone)]
pub struct GameState {
    pub players: Box<[PlayerState]>,
    pub projectiles: Box<[Projectile]>,
}

impl Default for GameState {
    fn default() -> Self {
        Self {
            players: Box::new([]),
            projectiles: Box::new([]),
        }
    }
}

#[derive(Serialize, Clone, Copy)]
pub struct PlayerState{
    pub fighter_kind: i32,
    pub situation_kind: i32,
    pub lr: f32,
    pub percent: f32,
    pub position: Position,
    //pub charge: ChargeState,
}

#[derive(Serialize, Clone, Copy)]
pub struct Projectile{

}

#[derive(Serialize, Clone, Copy)]
pub struct Position{
    pub x: f32,
    pub y: f32,
}

pub struct GameStateModule {
    game_state: GameState,
}


impl Default for GameStateModule {
    fn default() -> Self {
        Self {
            game_state: GameState {
                players: Box::new([]),
                projectiles: Box::new([]),
            },
        }
    }
}

impl GameStateModule {
    fn save(&self) {
        let gs_text = serde_json::to_string(&self.game_state).expect("game_state serialize error.");
        let mut file = OpenOptions::new().write(true).truncate(true).open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
        write!(&file, "{}", gs_text).expect("something went wrong reading the file");
    }

    fn update_player_state(&mut self, player_state: PlayerState) {
        println!("update_player_state");
        /*for (i, ps) in self.game_state.players.iter().enumerate(){
            if ps.fighter_kind == player_state.fighter_kind{
                &self.game_state.set(GameState {
                    players: Box::new([]),
                    projectiles: Box::new([]),
                });
            }
        }
        self.save();*/
    }
}

pub fn save_game_state(game_state: GameState) {
    let gs_text = serde_json::to_string(&game_state).expect("game_state serialize error.");
    let mut file = OpenOptions::new().write(true).truncate(true).open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
    write!(&file, "{}", gs_text).expect("something went wrong reading the file");
}
