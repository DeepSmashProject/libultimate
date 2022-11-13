//use crate::charge::ChargeState;
use std::io::{Write, Error, ErrorKind};
use serde::{Serialize};
use std::fs::{OpenOptions};
use smash::app::{self, lua_bind::*, BattleObjectModuleAccessor};
use smash::lib::lua_const::*;
use once_cell::sync::{Lazy, OnceCell};
use std::sync::Mutex;
use crate::frame_counter::{FrameCounter, FrameCounterTrait};
static FRAME_COUNTER: Lazy<Mutex<FrameCounter>> = Lazy::new(|| Mutex::new(FrameCounter::new()));
static FRAME_COUNTER_ID: Lazy<Mutex<usize>> =  Lazy::new(|| Mutex::new(FRAME_COUNTER.lock().unwrap().register_counter()));

pub trait GameStateTrait {
    fn new() -> GameState;
    fn get_player_state(&mut self, player_id: usize) -> Result<&PlayerState, Error>;
    fn set_player_state(&mut self, player_state: PlayerState) -> Result<usize, Error>;
    fn save(&mut self, module_accessor: &mut app::BattleObjectModuleAccessor) -> Result<(), Error>;
}

#[derive(Serialize)]
pub struct GameState{
    pub frame_count: u32,  // frame count: 0~60 -> 0~60 -> 0~60 -> ...
    pub players: Vec<PlayerState>,
    pub projectiles: Vec<Projectile>,
}

impl GameStateTrait for GameState {
    fn new() -> GameState {
        FRAME_COUNTER.lock().unwrap().start_counting(*FRAME_COUNTER_ID.lock().unwrap());
        GameState {
            frame_count: 0,
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

    fn save(&mut self, module_accessor: &mut app::BattleObjectModuleAccessor) -> Result<(), Error>{
        unsafe {
            let entry_id_int = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) as i32;
            let entry_id = app::FighterEntryID(entry_id_int);
            let player_state = PlayerState {
                id: entry_id_int as usize,
                fighter_kind: app::utility::get_kind(module_accessor),
                fighter_status_kind: StatusModule::status_kind(module_accessor),
                situation_kind: StatusModule::situation_kind(module_accessor),
                lr: PostureModule::lr(module_accessor),
                percent: DamageModule::damage(module_accessor, 0),
                position: Position{
                    x: PostureModule::pos_x(module_accessor),
                    y: PostureModule::pos_y(module_accessor),
                },
                speed: Speed{
                    x: KineticModule::get_sum_speed_x(module_accessor, *KINETIC_ENERGY_RESERVE_ATTRIBUTE_MAIN),
                    y: KineticModule::get_sum_speed_y(module_accessor, *KINETIC_ENERGY_RESERVE_ATTRIBUTE_MAIN),
                },
                controller_state: ControllerState{
                    stick_x: ControlModule::get_stick_x(module_accessor),
                    stick_y: ControlModule::get_stick_y(module_accessor),
                    button_attack: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_ATTACK),
                    button_special: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_SPECIAL),
                    button_smash: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_SMASH),
                    button_guard: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_GUARD),
                    button_guard_hold: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_GUARD_HOLD),
                    button_catch: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_CATCH),
                    button_jump: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_JUMP),
                    button_jump_mini: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_JUMP_MINI),
                    button_invalid: ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_INVALID),
                },
                frame: MotionModule::frame(module_accessor),
                end_frame: MotionModule::end_frame(module_accessor),
                is_cpu:  WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) == FighterId::CPU as i32,
                is_dead: StatusModule::status_kind(module_accessor) == *FIGHTER_STATUS_KIND_DEAD,
                //is_actionable: is_actionable(module_accessor),
                /*fighter_information: gamestate::FighterInformation {
                    hit_point: FighterInformation::hit_point(fighter_info),
                    fighter_color: FighterInformation::fighter_color(fighter_info),
                    is_operation_cpu: FighterInformation::is_operation_cpu(fighter_info),
                    dead_count: FighterInformation::dead_count(fighter_info, entry_id_int),
                    stock_count: FighterInformation::stock_count(fighter_info),
                    suicide_count: FighterInformation::suicide_count(fighter_info, entry_id_int),
                    total_beat_count: FighterInformation::total_beat_count(fighter_info, entry_id_int),
                    is_last_dead_suicide: FighterInformation::is_last_dead_suicide(fighter_info),
                    is_on_rebirth: FighterInformation::is_on_rebirth(fighter_info),
                    fighter_category: FighterInformation::fighter_category(fighter_info),
                    gravity: FighterInformation::gravity(fighter_info),
                }*/
                //charge: _charge,
            };
            self.set_player_state(player_state).unwrap();

            FRAME_COUNTER.lock().unwrap().tick();
            self.frame_count = FRAME_COUNTER.lock().unwrap().get_frame_count(*FRAME_COUNTER_ID.lock().unwrap());
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
}

#[derive(Serialize)]
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
    pub controller_state: ControllerState,
    pub is_cpu: bool,
    pub is_dead: bool,
    pub frame: f32,
    pub end_frame: f32,
    //pub is_actionable: bool,
    //pub fighter_information: FighterInformation,
    //pub charge: ChargeState,
}

#[derive(Serialize)]
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

#[derive(Serialize, Debug)]
pub enum FighterId {
    Player = 0,
    CPU = 1,
}

#[derive(Serialize)]
pub struct ControllerState{
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

#[derive(Serialize)]
pub struct Projectile{

}

#[derive(Serialize)]
pub struct Position{
    pub x: f32,
    pub y: f32,
}

#[derive(Serialize)]
pub struct Speed{
    pub x: f32,
    pub y: f32,
}
