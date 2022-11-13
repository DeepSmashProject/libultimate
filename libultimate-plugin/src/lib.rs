use smash::app::{self, lua_bind::*};
use smash::lib::lua_const::*;
use skyline::nro::{self, NroInfo};
use skyline::nn::hid::{NpadGcState, GetNpadStyleSet};
mod charge;
use std::fs;
use std::fs::{OpenOptions};
use std::io::{Error, ErrorKind};
use std::path::Path;
use std::sync::Mutex;
mod game_state;
mod controller;
mod command;
mod counter;
use crate::counter::{Counter, CounterTrait};
use crate::game_state::{GameState, GameStateTrait, PlayerState, Speed, Position, FighterId};
use crate::controller::{ControllerManager, ControllerManagerTrait};
use once_cell::sync::Lazy;
use once_cell::sync::OnceCell;

static GAME_STATE: Lazy<Mutex<GameState>> = Lazy::new(|| Mutex::new(GameState::new()));
static CONTROLLER_MANAGER: Lazy<Mutex<ControllerManager>> = Lazy::new(|| Mutex::new(ControllerManager::new()));
static COMMAND: Lazy<Mutex<command::Command>> = Lazy::new(|| Mutex::new(command::Command::default()));
//static mut FIGHTER_MANAGER_ADDR: usize = 0;

pub fn handle_get_npad_state(state: *mut NpadGcState, _controller_id: *const u32){
    unsafe {
        match CONTROLLER_MANAGER.lock().unwrap().operate(*_controller_id as usize, state) {
            Ok(_) => {},
            Err(_) => {},
        };
    }
}

#[skyline::hook(replace = ControlModule::get_command_flag_cat)]
pub unsafe fn handle_get_command_flag_cat(
    module_accessor: &mut app::BattleObjectModuleAccessor,
    category: i32,
) -> i32 {
    // once per frame
    let mut flag = original!()(module_accessor, category);
    if category == FIGHTER_PAD_COMMAND_CATEGORY1 {
        GAME_STATE.lock().unwrap().save(module_accessor);
    }
    flag = match get_command_flag(category, module_accessor){
        Ok(flag) => flag,
        Err(_) => original!()(module_accessor, category),
    };
    return flag;
}

unsafe fn get_command_flag(category: i32, module_accessor: &mut app::BattleObjectModuleAccessor) -> Result<i32, Error>{
    let entry_id_int = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) as u32;
    let _command = command::Command::get(entry_id_int)?;

    let mut prev_command = COMMAND.lock().unwrap();

    if entry_id_int == _command.player_id {
        // execute stick until recieve next command
        //ControlModule::set_main_stick_x(module_accessor, _command.stick_x);
        //ControlModule::set_main_stick_y(module_accessor, _command.stick_y);

        // execute command once per recieve command
        if _command.id != prev_command.id || _command.hold {
            if category == FIGHTER_PAD_COMMAND_CATEGORY1 {
                let flag: i32;
                match _command.action {
                    command::Action::AIR_DODGE => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_AIR_ESCAPE;
                    }
                    command::Action::TILT_U => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_HI3;
                    }
                    command::Action::SMASH_U => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_HI4;
                    }
                    command::Action::TILT_D => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_LW3;
                    }
                    command::Action::SMASH_D => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_LW4;
                    }
                    command::Action::JAB => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_N;
                    }
                    command::Action::TILT_F => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_S3;
                    }
                    command::Action::SMASH_F => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_S4;
                    }
                    command::Action::GRAB => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_CATCH;
                    }
                    command::Action::DASH => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_DASH;
                    }
                    command::Action::SPOT_DODGE => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ESCAPE;
                    }
                    command::Action::ROLL_B => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ESCAPE_B;
                    }
                    command::Action::ROLL_F => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_ESCAPE_F;
                    }
                    command::Action::JUMP => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_JUMP;
                    }
                    command::Action::SPECIAL_U => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_HI;
                    }
                    command::Action::SPECIAL_D => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_LW;
                    }
                    command::Action::SPECIAL_N => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_N;
                    }
                    command::Action::SPECIAL_F => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_S;
                    }
                    command::Action::TURN => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_TURN;
                    }
                    command::Action::TURN_DASH => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_TURN_DASH;
                    }
                    command::Action::WALK => {
                        flag = *FIGHTER_PAD_CMD_CAT1_FLAG_WALK;
                    }
                    _ => return Err(Error::new(ErrorKind::Other, "NO CMD")),
                }
                // update prev_command
                prev_command.id = _command.clone().id;
                prev_command.player_id = _command.clone().player_id;
                prev_command.action = _command.clone().action;
                prev_command.stick_x = _command.clone().stick_x;
                prev_command.stick_y = _command.clone().stick_y;
                return Ok(flag);
            }
            if category == 1 {
                let flag: i32;
                match _command.action {
                    command::Action::GUARD => {
                        flag = *FIGHTER_PAD_CMD_CAT2_FLAG_COMMON_GUARD;
                    }
                    command::Action::THROW_B => {
                        flag = *FIGHTER_PAD_CMD_CAT2_FLAG_THROW_B;
                    }
                    command::Action::THROW_F => {
                        flag = *FIGHTER_PAD_CMD_CAT2_FLAG_THROW_F;
                    }
                    command::Action::THROW_U => {
                        flag = *FIGHTER_PAD_CMD_CAT2_FLAG_THROW_HI;
                    }
                    command::Action::THROW_D => {
                        flag = *FIGHTER_PAD_CMD_CAT2_FLAG_THROW_LW;
                    }
                    command::Action::DASH_ATTACK => {
                        flag = *FIGHTER_PAD_CMD_CAT2_FLAG_DASH_ATTACK_S4;
                    }
                    _ => return Err(Error::new(ErrorKind::Other, "NO CMD")),
                }
                // update prev_command
                prev_command.id = _command.clone().id;
                prev_command.player_id = _command.clone().player_id;
                prev_command.action = _command.clone().action;
                prev_command.stick_x = _command.clone().stick_x;
                prev_command.stick_y = _command.clone().stick_y;
                return Ok(flag);
            }
        }
    }
    
    return Err(Error::new(ErrorKind::Other, "NO CMD"));
}

macro_rules! actionable_statuses {
    () => {
        vec![
            FIGHTER_STATUS_TRANSITION_TERM_ID_CONT_ESCAPE_AIR,
            FIGHTER_STATUS_TRANSITION_TERM_ID_CONT_ATTACK_AIR,
            FIGHTER_STATUS_TRANSITION_TERM_ID_CONT_GUARD_ON,
            FIGHTER_STATUS_TRANSITION_TERM_ID_CONT_ESCAPE,
        ]
    };
}

unsafe fn is_actionable(module_accessor: *mut app::BattleObjectModuleAccessor) -> bool {
    actionable_statuses!().iter().any(|actionable_transition| {
        WorkModule::is_enable_transition_term(module_accessor, **actionable_transition)
    }) || CancelModule::is_enable_cancel(module_accessor)
}

#[allow(improper_ctypes)]
extern "C" {
    fn add_nn_hid_hook(callback: fn(*mut NpadGcState, *const u32));
}

fn nro_main(nro: &NroInfo<'_>) {
    if nro.module.isLoaded {
        return;
    }

    if nro.name == "common" {
        unsafe {
            if (add_nn_hid_hook as *const ()).is_null() {
                panic!("The NN-HID hook plugin could not be found and is required to add NRO hooks. Make sure libnn_hid_hook.nro is installed.");
            }
            add_nn_hid_hook(handle_get_npad_state);
        }
        skyline::install_hooks!(
            handle_get_command_flag_cat,
        );
    }
}

fn touch(path: &Path) -> Result<(), Error> {
    match OpenOptions::new().create(true).write(true).open(path) {
        Ok(_) => Ok(()),
        Err(e) => Err(e),
    }
}

fn create_data() {
    println!("[libultimate] create data.");
    fs::create_dir_all("sd:/libultimate").expect("could not create data directory.");
    touch(&Path::new("sd:/libultimate/game_state.json")).expect("Error on creating game_state.json.");
    touch(&Path::new("sd:/libultimate/config.json")).expect("Error on creating config.json.");
    touch(&Path::new("sd:/libultimate/command.json")).expect("Error on creating command.json.");
}

#[skyline::main(name = "libultimate-plugin")]
pub fn main() {
    println!("[libultimate] Initializing...");
    //globalGameState.set(gamestate::GameState::default());
    create_data();
    nro::add_hook(nro_main).unwrap();
    println!("[libultimate] Finished Initializing.");
}
