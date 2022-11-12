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
mod controlstate;
mod command;
mod frame_counter;
use crate::frame_counter::{FrameCounter, FrameCounterTrait};
use crate::game_state::{GameState, GameStateTrait, PlayerState, Speed, Position, FighterId};
use once_cell::sync::Lazy;
use once_cell::sync::OnceCell;

static GAME_STATE: Lazy<Mutex<GameState>> = Lazy::new(|| Mutex::new(GameState::new()));
static CONTROLSTATE: Lazy<Mutex<controlstate::ControlState>> = Lazy::new(|| Mutex::new(controlstate::ControlState::default()));
static FRAME_COUNTER: Lazy<Mutex<FrameCounter>> = Lazy::new(|| Mutex::new(FrameCounter::new()));
static FRAME_COUNTER_ID: Lazy<Mutex<usize>> =  Lazy::new(|| Mutex::new(FRAME_COUNTER.lock().unwrap().register_counter()));
static COMMAND: Lazy<Mutex<command::Command>> = Lazy::new(|| Mutex::new(command::Command::default()));
static mut FIGHTER_MANAGER_ADDR: usize = 0;

pub fn handle_get_npad_state(state: *mut NpadGcState, _controller_id: *const u32){
    unsafe {
        match get_npad_state(state, _controller_id){
            Ok(_) => {},
            Err(_) => {},
        };
    }
}

unsafe fn get_npad_state(state: *mut NpadGcState, _controller_id: *const u32) -> Result<(), Error>{
    let mut prev_control_state = CONTROLSTATE.lock().unwrap();
    let control_state = match controlstate::ControlState::get(*_controller_id){
        Ok(cs) => cs,
        Err(_) => prev_control_state.clone(),
    };
    if control_state.player_id == *_controller_id{
        //(*state).updateCount = control_state.update_count;
        if control_state.id != prev_control_state.id || control_state.hold {
            (*state).Buttons = control_state.buttons;
            (*state).LStickX = control_state.l_stick_x;
            (*state).LStickY = control_state.l_stick_y;
            (*state).RStickX = control_state.r_stick_x;
            (*state).RStickY = control_state.r_stick_y;
            (*state).Flags = control_state.flags;
            (*state).LTrigger = control_state.l_trigger;
            (*state).RTrigger = control_state.r_trigger;
            // update prev_control_state
            prev_control_state.id = control_state.clone().id;
            prev_control_state.player_id = control_state.clone().player_id;
            prev_control_state.update_count = control_state.clone().update_count;
            prev_control_state.buttons = control_state.clone().buttons;
            prev_control_state.l_stick_x = control_state.clone().l_stick_x;
            prev_control_state.l_stick_y = control_state.clone().l_stick_y;
            prev_control_state.r_stick_x = control_state.clone().r_stick_x;
            prev_control_state.r_stick_y = control_state.clone().r_stick_y;
            prev_control_state.flags = control_state.clone().flags;
            prev_control_state.l_trigger = control_state.clone().l_trigger;
            prev_control_state.r_trigger = control_state.clone().r_trigger;
            prev_control_state.hold = control_state.clone().hold;
        }
    }
    return Ok(());
}

#[skyline::hook(replace = ControlModule::get_command_flag_cat)]
pub unsafe fn handle_get_command_flag_cat(
    module_accessor: &mut app::BattleObjectModuleAccessor,
    category: i32,
) -> i32 {
    // once per frame
    let mut flag = original!()(module_accessor, category);
    if category == FIGHTER_PAD_COMMAND_CATEGORY1 {
        save_gamestate(module_accessor);
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

unsafe fn save_gamestate(module_accessor: &mut app::BattleObjectModuleAccessor){
    let entry_id_int = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) as i32;
    let entry_id = app::FighterEntryID(entry_id_int);
    let x = PostureModule::pos_x(module_accessor);
    let y = PostureModule::pos_y(module_accessor);
    let lr = PostureModule::lr(module_accessor); //left or right
    let speed_x = KineticModule::get_sum_speed_x(module_accessor, *KINETIC_ENERGY_RESERVE_ATTRIBUTE_MAIN);
    let speed_y = KineticModule::get_sum_speed_y(module_accessor, *KINETIC_ENERGY_RESERVE_ATTRIBUTE_MAIN);
    let button_attack = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_ATTACK);
    let button_special = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_SPECIAL);
    let button_smash = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_SMASH);
    let button_guard = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_GUARD);
    let button_guard_hold = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_GUARD_HOLD);
    let button_catch = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_CATCH);
    let button_jump = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_JUMP);
    let button_jump_mini = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_JUMP_MINI);
    let button_invalid = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_INVALID);
    let stick_x = ControlModule::get_stick_x(module_accessor);
    let stick_y = ControlModule::get_stick_y(module_accessor);
    let percent = DamageModule::damage(module_accessor, 0);
    let situation_kind = StatusModule::situation_kind(module_accessor);
    let fighter_kind = app::utility::get_kind(module_accessor);
    let fighter_status_kind = StatusModule::status_kind(module_accessor);
    let frame = MotionModule::frame(module_accessor);
    let end_frame = MotionModule::end_frame(module_accessor);
    let is_dead = StatusModule::status_kind(module_accessor) == *FIGHTER_STATUS_KIND_DEAD;
    let is_actionable = is_actionable(module_accessor);
    //let fighter_manager = *(FIGHTER_MANAGER_ADDR as *mut *mut app::FighterManager);
    //let fighter_info = FighterManager::get_fighter_information(fighter_manager, entry_id);
    let _charge = charge::get_charge(module_accessor, fighter_kind);
    let is_cpu = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) == FighterId::CPU as i32;

    let player_state = PlayerState {
        id: entry_id_int as usize,
        fighter_kind: fighter_kind,
        fighter_status_kind: fighter_status_kind,
        situation_kind: situation_kind,
        lr: lr,
        percent: percent,
        position: Position{
            x: x,
            y: y,
        },
        speed: Speed{
            x: speed_x,
            y: speed_y,
        },
        /*control_state: gamestate::ControlState{
            stick_x: stick_x,
            stick_y: stick_y,
            button_attack: button_attack,
            button_special: button_special,
            button_smash: button_smash,
            button_guard: button_guard,
            button_guard_hold: button_guard_hold,
            button_catch: button_catch,
            button_jump: button_jump,
            button_jump_mini: button_jump_mini,
            button_invalid: button_invalid,
        },*/
        frame: frame,
        end_frame: end_frame,
        is_cpu: is_cpu,
        is_dead: is_dead,
        is_actionable: is_actionable,
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
    GAME_STATE.lock().unwrap().set_player_state(player_state).unwrap();
    GAME_STATE.lock().unwrap().save().unwrap();
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

/*pub fn init() {
    unsafe {
        let mut frame_counter = FrameCounter::new();
        FRAME_COUNTER = frame_counter.register_counter();
        let mut game_state = GameState::new();
    }
}*/

#[skyline::main(name = "libultimate-plugin")]
pub fn main() {
    println!("[libultimate] Initializing...");
    //globalGameState.set(gamestate::GameState::default());
    create_data();
    nro::add_hook(nro_main).unwrap();
    println!("[libultimate] Finished Initializing.");
}
