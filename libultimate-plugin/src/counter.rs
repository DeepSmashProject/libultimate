pub trait CounterTrait {
    fn new() -> Counter;
    fn start_counting(&mut self);
    fn stop_counting(&mut self);
    fn reset_frame_count(&mut self);
    fn full_reset(&mut self);
    fn should_delay(&mut self, delay: u32) -> bool;
    fn get_frame_count(&mut self) -> u32;
    fn tick(&mut self);
}

pub struct Counter{
    should_count: bool,
    count: u32,
}

impl CounterTrait for Counter {
    fn new() -> Counter {
        Counter {
            should_count: false,
            count: 0
        }
    }

    fn start_counting(&mut self) {
        self.should_count = true;
    }

    fn stop_counting(&mut self) {
        self.should_count = false;
    }

    fn reset_frame_count(&mut self) {
        self.count = 0;
    }

    fn full_reset(&mut self) {
        self.reset_frame_count();
        self.stop_counting();
    }

    fn should_delay(&mut self, delay: u32) -> bool {
        if delay == 0 {
            return false;
        }

        let current_frame = self.get_frame_count();

        if current_frame == 0 {
            self.start_counting();
        }

        if current_frame >= delay-1 {
            self.full_reset();
            return false;
        }

        true
    }

    fn get_frame_count(&mut self) -> u32 {
        self.count
    }

    fn tick(&mut self) {
        if self.should_count {
            self.count += 1;
        }
    }    
}

/*
Example usage:
let mut frame_counter = Counter::new();
    let index = frame_counter.register_counter();
    println!("index: {}", index);
    frame_counter.start_counting(index);
    for i in 0..20 {
        println!("frame_counter: {}", frame_counter.get_frame_count(index));
        //println!("should_delay: {}", frame_counter.should_delay(5, index));
        if !frame_counter.should_delay(5, index) {
            println!("do!");
        }
        frame_counter.tick();
    }
    println!("frame_count: {}", frame_counter.get_frame_count(index));
*/
