use smash::lib::L2CValue;
use smash::lua2cpp::L2CFighterBase;
use smash::app::sv_system;
use smash::app::{self, lua_bind::*};
use smash::lib::lua_const::*;
use skyline::nro::{self, NroInfo};
mod charge;
use std::fs;
use std::io::Write;
use serde::{Deserialize, Serialize};

trait APIModule {
    fn open(&self) -> u64;
    fn close(&self) -> u64;
    fn save(&self) -> u64;
}

struct APIModuleStruct {
    game_state: API
}

impl APIModule for APIModuleStruct {
    fn open(&self) -> u64 {
        println!("open");
    }

    fn save(&self, fpath) -> u64 {
        println!("save");
        let mut f = fs::File::open(fpath).expect("file not found");
        f.write_all(b"nju33").expect("something went wrong reading the file");
    }

    fn close(&self) -> u64 {
        println!("close");
    }
}

struct Memo {
    id: isize,
    body: String,
    star: bool,
}

fn write_file(body: String) -> std::io::Result<()> {
    let mut file = OpenOptions::new()
        .read(true)
        .write(true)
        .open("memo.json")?;
    println!("file: {:#?}", file);

    let memo = Memo {
        id: 100,
        body: body,
        star: true,
    };

    let memo_text = serde_json::to_string(&memo).unwrap();
    println!("memo: {}", &memo_text);
    write!(&file, "{}", memo_text)?;

    Ok(())
}
