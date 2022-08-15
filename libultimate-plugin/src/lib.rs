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
use once_cell::sync::OnceCell;

static GAMESTATE: OnceCell<Mutex<gamestate::GameState>> = OnceCell::new();

#[skyline::hook(replace = ControlModule::get_command_flag_cat)]
pub unsafe fn handle_get_command_flag_cat(
    module_accessor: &mut app::BattleObjectModuleAccessor,
    category: i32,
) -> i32 {
    // once per frame
    if category == FIGHTER_PAD_COMMAND_CATEGORY1 {
        let entry_id_int = WorkModule::get_int(module_accessor, *FIGHTER_INSTANCE_WORK_ID_INT_ENTRY_ID) as i32;
        //let entry_id = app::FighterEntryID(entry_id_int);
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
    return original!()(module_accessor, category);
}

fn nro_main(nro: &NroInfo<'_>) {
    println!("[libultimate] nro module.");
    if nro.module.isLoaded {
        return;
    }
    println!("[libultimate] nro module.2");

    if nro.name == "common" {
        skyline::install_hooks!(
            //handle_change_status,
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
