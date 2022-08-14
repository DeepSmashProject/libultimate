use smash::lib::L2CValue;
use smash::lua2cpp::L2CFighterBase;
use smash::app::sv_system;
use smash::app::{self, lua_bind::*};
use smash::lib::lua_const::*;
use skyline::nro::{self, NroInfo};
mod charge;
use std::fs;
use std::io::Write;
//use nix::unistd;
//use nix::sys::stat;
//use std::path::Path;
//use std::env;

struct SavedState {
    x: f32,
    y: f32,
    percent: f32,
    lr: f32,
    situation_kind: i32,
    fighter_kind: i32,
    charge: charge::ChargeState,
}

struct GameState {
    players: Box<[PlayerState]>,
    projectiles: Box<[Projectile]>,
    stage: i32,
}

struct PlayerState{
    fighter_kind: i32,
    situation_kind: i32,
    lr: i32,
    percent: f32,
    position: Position,
    charge: charge::ChargeState,
}

struct Projectile{

}

struct Position{
    x: f32,
    y: f32,
}

trait GameStateModule {
    fn open(&self) -> u64;
    fn close(&self) -> u64;
    fn save(&self) -> u64;
}

struct GameStateModuleStruct {
    game_state: GameState
}

impl GameStateModule for GameStateModuleStruct {
    fn open(&self) -> u64 {
        println!("open");
    }

    fn save(&self) -> u64 {
        println!("save");
    }

    fn close(&self) -> u64 {
        println!("close");
    }
}

trait ControllerModule {
    fn open(&self) -> u64;
    fn close(&self) -> u64;
    fn on_push_control(&self) -> u64;
}

struct ControllerModuleStruct {
    game_state: Controller
}

impl ControllerModule for ControllerModuleStruct {
    fn open(&self) -> u64 {
        println!("open");
    }

    fn on_push_control(&self) -> u64 {
        println!("on_push_control");
    }

    fn close(&self) -> u64 {
        println!("close");
    }
}
