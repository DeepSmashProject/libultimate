use smash::app::{self, lua_bind::*};
use smash::lib::lua_const::*;
use skyline::nro::{self, NroInfo};
mod charge;
use std::fs;
use std::fs::{OpenOptions};
use std::io;
use std::path::Path;
use std::sync::Mutex;
mod gamestate;
mod command;
use once_cell::sync::OnceCell;

static GAMESTATE: OnceCell<Mutex<gamestate::GameState>> = OnceCell::new();
static COMMAND: OnceCell<Mutex<command::Command>> = OnceCell::new();
pub static mut FIGHTER_MANAGER_ADDR: usize = 0;

#[skyline::hook(replace = ControlModule::get_command_flag_cat)]
pub unsafe fn handle_get_command_flag_cat(
    module_accessor: &mut app::BattleObjectModuleAccessor,
    category: i32,
) -> i32 {
    // once per frame
    let mut flag = original!()(module_accessor, category);
    if category == FIGHTER_PAD_COMMAND_CATEGORY1 {
        save_gamestate(module_accessor);
        flag = get_command_flag(module_accessor);
    }
    return flag;
}

unsafe fn get_command_flag(module_accessor: &mut app::BattleObjectModuleAccessor) -> i32{
    let _command = command::Command::get();
    let entry_id_int = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) as i32;

    let mut prev_command = COMMAND
        .get_or_init(|| Mutex::new(command::Command::default()))
        .lock()
        .unwrap();
    let mut flag = 0;

    if _command.id != prev_command.id && entry_id_int == _command.player_id {
        *prev_command = _command;
        match prev_command.action {
            command::Action::AIR_ESCAPE => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_AIR_ESCAPE;
            }
            command::Action::ATTACK_HI3 => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_HI3;
            }
            command::Action::ATTACK_HI4 => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_HI4;
            }
            command::Action::ATTACK_LW3 => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_LW3;
            }
            command::Action::ATTACK_LW4 => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_LW4;
            }
            command::Action::ATTACK_N => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_N;
            }
            command::Action::ATTACK_S3 => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_S3;
            }
            command::Action::ATTACK_S4 => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ATTACK_S4;
            }
            command::Action::CATCH => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_CATCH;
            }
            command::Action::DASH => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_DASH;
            }
            command::Action::ESCAPE => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ESCAPE;
            }
            command::Action::ESCAPE_B => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ESCAPE_B;
            }
            command::Action::ESCAPE_F => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_ESCAPE_F;
            }
            command::Action::JUMP => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_JUMP;
            }
            command::Action::JUMP_BUTTON => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_JUMP_BUTTON;
            }
            command::Action::SPECIAL_ANY => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_ANY;
            }
            command::Action::SPECIAL_HI => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_HI;
            }
            command::Action::SPECIAL_LW => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_LW;
            }
            command::Action::SPECIAL_N => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_N;
            }
            command::Action::SPECIAL_S => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_SPECIAL_S;
            }
            command::Action::TURN => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_TURN;
            }
            command::Action::TURN_DASH => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_TURN_DASH;
            }
            command::Action::WALK => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_WALK;
            }
            command::Action::WALL_JUMP_LEFT => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_WALL_JUMP_LEFT;
            }
            command::Action::WALL_JUMP_RIGHT => {
                return *FIGHTER_PAD_CMD_CAT1_FLAG_WALL_JUMP_RIGHT;
            }
            _ => return 0,
        }
        return flag;
    }
    
    return 0;
}

unsafe fn save_gamestate(module_accessor: &mut app::BattleObjectModuleAccessor){
    let entry_id_int = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) as i32;
    let entry_id = app::FighterEntryID(entry_id_int);
    let x = PostureModule::pos_x(module_accessor);
    let y = PostureModule::pos_y(module_accessor);
    let lr = PostureModule::lr(module_accessor); //left or right
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
    let is_dead = StatusModule::status_kind(module_accessor) == *FIGHTER_STATUS_KIND_DEAD;
    //let fighter_manager = *(FIGHTER_MANAGER_ADDR as *mut *mut app::FighterManager);
    //let fighter_info = app::FighterManager::get_fighter_information(fighter_manager, entry_id);
    let _charge = charge::get_charge(module_accessor, fighter_kind);
    let is_cpu = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) == gamestate::FighterId::CPU as i32;

    let player_state = gamestate::PlayerState {
        id: entry_id_int,
        fighter_kind: fighter_kind,
        fighter_status_kind: fighter_status_kind,
        situation_kind: situation_kind,
        lr: lr,
        percent: percent,
        position: gamestate::Position{
            x: x,
            y: y,
        },
        control_state: gamestate::ControlState{
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
        },
        is_cpu: is_cpu,
        is_dead: is_dead,
        //charge: _charge,
    };
    let mut game_state = GAMESTATE
        .get_or_init(|| Mutex::new(gamestate::GameState::default()))
        .lock()
        .unwrap();
    *game_state = gamestate::GameState::update_player_state(&game_state, player_state);
    gamestate::GameState::save(&game_state);
    //println!("[libultimate] fighter change status. id {} category: {}, x {}, y {}, lr {}", entry_id_int, category, x, y, lr);
}

fn nro_main(nro: &NroInfo<'_>) {
    if nro.module.isLoaded {
        return;
    }

    if nro.name == "common" {
        skyline::install_hooks!(
            handle_get_command_flag_cat,
        );
    }
}

fn touch(path: &Path) -> io::Result<()> {
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
