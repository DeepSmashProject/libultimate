//use crate::charge::ChargeState;
use std::io::{Write, BufReader, Error, ErrorKind};
use serde::{Serialize, Deserialize};
use std::fs::{OpenOptions, File};
use std::fs;
use std::path::Path;
use skyline::nn::hid::{NpadGcState};

#[derive(Serialize, Deserialize, Clone)]
pub struct ControllerState {
    pub id: String,
    pub player_id: u32,
    pub update_count: i64,
    pub buttons: u64,
    pub l_stick_x: i32,
    pub l_stick_y: i32,
    pub r_stick_x: i32,
    pub r_stick_y: i32,
    pub flags: u32,
    pub l_trigger: u32,
    pub r_trigger: u32,
    pub hold: bool,
}

impl ControllerState {
    fn new() -> Self {
        Self {
            id: "".to_string(),
            player_id: 0,
            update_count: 0,
            buttons: 0,
            l_stick_x: 0,
            l_stick_y: 0,
            r_stick_x: 0,
            r_stick_y: 0,
            flags: 0,
            l_trigger: 0,
            r_trigger: 0,
            hold: false,
        }
    }
}

pub trait ControllerTrait {
    fn new(controller_id: usize) -> Controller;
    fn operate(&mut self, state: *mut NpadGcState) -> Result<(), Error>;
    fn get_state(&mut self) -> ControllerState;
    fn read_input(&mut self) -> Result<ControllerState, Error>;
}

pub struct Controller{
    pub id: usize,
    pub state: ControllerState,
}

impl ControllerTrait for Controller {
    fn new(controller_id: usize) -> Controller {
        Controller {
            id: controller_id,
            state: ControllerState::new(),
        }
    }

    fn get_state(&mut self) -> ControllerState {
        return self.state.clone();
    }

    fn operate(&mut self, state: *mut NpadGcState) -> Result<(), Error>{
        let input_state = self.read_input()?;
        unsafe {
            if input_state.id != self.state.id || input_state.hold {
                (*state).Buttons = input_state.buttons;
                (*state).LStickX = input_state.l_stick_x;
                (*state).LStickY = input_state.l_stick_y;
                (*state).RStickX = input_state.r_stick_x;
                (*state).RStickY = input_state.r_stick_y;
                (*state).Flags = input_state.flags;
                (*state).LTrigger = input_state.l_trigger;
                (*state).RTrigger = input_state.r_trigger;
                // update prev_control_state
                self.state = input_state;
            }
        }
        return Ok(());
    }

    fn read_input(&mut self) -> Result<ControllerState, Error>{
        let mut control_state: ControllerState = self.state.clone();
        let control_state_ok_path = format!("sd:/libultimate/control_state_{}.ok.json", self.id);
        let control_state_path = format!("sd:/libultimate/control_state_{}.json", self.id);
        if Path::new(&control_state_ok_path).exists() {
            let file = File::open(&control_state_path)?;
            let reader = BufReader::new(file);
            control_state = serde_json::from_reader(reader)?;
            // remove ok.json
            fs::remove_file(&control_state_ok_path).unwrap();
        }else{
            return Err(Error::new(ErrorKind::Other, "control_state.json does not exist"));
        }
        return Ok(control_state);
    }

}

pub trait ControllerManagerTrait {
    fn new() -> ControllerManager;
    fn get_controller(&mut self, id: usize) -> Result<&mut Controller, Error>;
    fn exist_controller(&mut self, id: usize) -> bool;
    fn operate(&mut self, id: usize, state: *mut NpadGcState) -> Result<(), Error>;
}

pub struct ControllerManager{
    pub controllers: Vec<Controller>,
}

impl ControllerManagerTrait for ControllerManager {
    fn new() -> ControllerManager {
        ControllerManager {
            controllers: Vec::new(),
        }
    }

    fn get_controller(&mut self, id: usize) -> Result<&mut Controller, Error>{
        if id < self.controllers.len() {
            return Ok(&mut self.controllers[id]);
        }else{
            return Err(Error::new(ErrorKind::Other, "controller does not exist"));
        }
    }

    fn exist_controller(&mut self, id: usize) -> bool{
        for controller in self.controllers.iter() {
            if controller.id == id {
                return true;
            }
        }
        return false;
    }

    fn operate(&mut self, id: usize, state: *mut NpadGcState) -> Result<(), Error>{
        if self.exist_controller(id) {
            let controller = self.get_controller(id)?;
            controller.operate(state)?;
        }else{
            let mut controller = Controller::new(id);
            controller.operate(state)?;
            self.controllers.push(controller);
        }
        return Ok(());
    }
}
