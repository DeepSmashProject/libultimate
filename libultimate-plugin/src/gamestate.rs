use crate::charge::ChargeState;
use std::fs;
use std::io::{self, Read, Write, BufReader};
use serde::{Serialize};
use std::fs::{File, OpenOptions};
//use nix::unistd;
//use nix::sys::stat;
//use std::path::Path;
//use std::env;

#[derive(Serialize)]
pub struct GameState {
    pub players: Box<[PlayerState]>,
    pub projectiles: Box<[Projectile]>,
}
#[derive(Serialize)]
pub struct PlayerState{
    pub fighter_kind: i32,
    pub situation_kind: i32,
    pub lr: f32,
    pub percent: f32,
    pub position: Position,
    //pub charge: ChargeState,
}
#[derive(Serialize)]
pub struct Projectile{

}

#[derive(Serialize)]
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
        println!("save");
       // let gs_text = serde_json::to_string(&self.game_state).unwrap();
        let mut f = fs::File::open("sd:/libultimate/game_state.json").expect("file not found");
        //write!(&f, "{}", gs_text).expect("something went wrong reading the file");
    }

    fn update_player_state(&self) {
        println!("update_player_state");
        self.save();
    }
}

pub fn save_game_state(game_state: GameState) {
    println!("save");
    let gs_text = serde_json::to_string(&game_state).expect("game_state serialize error.");
    println!("gs_text: {:#?}", gs_text);
    let mut file = OpenOptions::new().read(true).write(true).open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
    println!("file: {:#?}", file);
    //let mut f = fs::File::open("sd:/libultimate/game_state.json").expect("game_state.json file not found");
    write!(&file, "{}", gs_text).expect("something went wrong reading the file");
}
