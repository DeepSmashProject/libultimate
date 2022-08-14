use smash::lib::L2CValue;
use smash::lua2cpp::L2CFighterBase;
use smash::app::sv_system;
use smash::app::{self, lua_bind::*};
use smash::lib::lua_const::*;
use skyline::nro::{self, NroInfo};
mod charge;
use std::fs;
use std::fs::{File, OpenOptions};
use std::io::Write;
use std::io;
use std::path::Path;
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


#[skyline::hook(replace = smash::lua2cpp::L2CFighterBase_change_status)]
pub unsafe fn handle_change_status(
    _fighter: &mut L2CFighterBase,
    _status_kind: L2CValue,
    _unk: L2CValue,
){
    //let mut status_kind = status_kind;
    //let mut unk = unk;
    //let fighter_str = _fighter.try_get_string().unwrap_or("");
    let module_accessor = sv_system::battle_object_module_accessor(_fighter.lua_state_agent);
    let fighter_kind = app::utility::get_kind(module_accessor);
    let status_kind_int = _status_kind
        .try_get_int()
        .unwrap_or(*FIGHTER_STATUS_KIND_WAIT as u64) as i32;

    let attack = ControlModule::check_button_on(module_accessor, *CONTROL_PAD_BUTTON_ATTACK);
    let stick_x = ControlModule::get_stick_x(module_accessor);
    let stick_y = ControlModule::get_stick_y(module_accessor);
    let x = PostureModule::pos_x(module_accessor);
    let y = PostureModule::pos_y(module_accessor);
    let lr = PostureModule::lr(module_accessor); //left or right
    let percent = DamageModule::damage(module_accessor, 0);
    let situation_kind = StatusModule::situation_kind(module_accessor);
    let _charge = charge::get_charge(module_accessor, fighter_kind);
    println!("[Skyline Test4] fighter change status. {}, status {}, percent {}, xy {} {}, lr {}, attack {}", fighter_kind, status_kind_int, percent, x, y, lr, attack);
    let stick_x = ControlModule::set_main_stick_x(module_accessor, 1.0);
    //get_file();
    original!()(_fighter, _status_kind, _unk);
}

/*fn get_file() -> Result<(), Box<dyn std::error::Error>>{
    println!("[Skyline Test4] Read Start");
    let filename = "/home/map4/.config/Ryujinx/sdcard/test.txt";
    let mut f = fs::File::open(filename).expect("file not found");
    let content = fs::read_to_string(filename).expect("file cannot read");
    println!("[Skyline Test4] Read {}", content);
    Ok(())
}*/

fn save_state(){
    const fpath: &str = "sd:/TrainingModpack/fifo_test";
    match fs::File::create(fpath){
        Ok(file) => println!("Path {:?}", fpath),
        Err(err) => println!("Error creating file: {}", err),
    }
    let mut f = fs::File::open(fpath).expect("file not found");
    f.write_all(b"nju33").expect("something went wrong reading the file");
    /*match fs::File::open(fpath){
        Ok(file) => {
            println!("Opened Path");
            file.write_all(b"nju33").unwrap();
        },
        Err(err) => println!("Error creating fifo: {}", err),
    }*/
    /*let tmp_dir = TempDir::new("test_fifo").unwrap();
    let fifo_path = tmp_dir.path().join("foo.pipe");*/

    // create new fifo and give read, write and execute rights to the owner
    /*const fifo_path: &str = "sd:/TrainingModpack/fifo_test";
    match unistd::mkfifo(&fifo_path, stat::Mode::S_IRWXU) {
       Ok(_) => println!("created {:?}", fifo_path),
       Err(err) => println!("Error creating fifo: {}", err),
    }*/
}

fn nro_main(nro: &NroInfo<'_>) {
    println!("[Skyline Test4] nro module.");
    if nro.module.isLoaded {
        return;
    }
    println!("[Skyline Test4] nro module.2");

    if nro.name == "common" {
        skyline::install_hooks!(
            handle_change_status,
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
    println!("[Skyline Test4] create data.");
    fs::create_dir_all("sd:/LibUltimate").expect("could not create data directory.");
    touch(&Path::new("sd:/LibUltimate/game_state.json")).expect("Error on creating game_state.json.");
    touch(&Path::new("sd:/LibUltimate/config.json")).expect("Error on creating config.json.");
    touch(&Path::new("sd:/LibUltimate/command.json")).expect("Error on creating command.json.");
}

#[skyline::main(name = "libultimate-plugin")]
pub fn main() {
    println!("[Skyline Test4] Hello from skyline plugin");
    create_data();
    //save_state();
    println!("[Skyline Test4] finish savestate");

    nro::add_hook(nro_main).unwrap();
}
