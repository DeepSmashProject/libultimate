pub trait FrameCounterTrait {
    fn new() -> FrameCounter;
    fn register_counter(&mut self) -> usize;
    fn start_counting(&mut self, index: usize);
    fn stop_counting(&mut self, index: usize);
    fn reset_frame_count(&mut self, index: usize);
    fn full_reset(&mut self, index: usize);
    fn should_delay(&mut self, delay: u32, index: usize) -> bool;
    fn get_frame_count(&mut self, index: usize) -> u32;
    fn tick(&mut self);
    fn reset_all(&mut self);
}

struct Counter{
    should_count: bool,
    count: u32,
}

pub struct FrameCounter{
    counters: Vec<Counter>
}

impl FrameCounterTrait for FrameCounter {
    fn new() -> FrameCounter {
        FrameCounter {
            counters: Vec::new()
        }
    }

    fn register_counter(&mut self) -> usize{
        let index = self.counters.len();
        self.counters.push(Counter{
            should_count: false,
            count: 0
        });
        index
    }

    fn start_counting(&mut self, index: usize) {
        self.counters[index].should_count = true;
    }

    fn stop_counting(&mut self, index: usize) {
        self.counters[index].should_count = false;
    }

    fn reset_frame_count(&mut self, index: usize) {
        self.counters[index].count = 0;
    }

    fn full_reset(&mut self, index: usize) {
        self.reset_frame_count(index);
        self.stop_counting(index);
    }

    fn should_delay(&mut self, delay: u32, index: usize) -> bool {
        if delay == 0 {
            return false;
        }

        let current_frame = self.get_frame_count(index);

        if current_frame == 0 {
            self.start_counting(index);
        }

        if current_frame >= delay-1 {
            self.full_reset(index);
            return false;
        }

        true
    }

    fn get_frame_count(&mut self, index: usize) -> u32 {
        self.counters[index].count
    }

    fn tick(&mut self) {
        for mut counter in self.counters.iter_mut() {
            if counter.should_count {
                counter.count += 1;
            }
        }
    }

    fn reset_all(&mut self) {
        for mut counter in self.counters.iter_mut() {
            counter.count = 0;
            counter.should_count = false;
        }
    }
    
}
