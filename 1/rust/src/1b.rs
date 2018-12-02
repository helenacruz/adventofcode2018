use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::collections::HashSet;

fn main() {
    println!("frequency: {}", twice());
}

fn twice() -> i32 {
    let mut frequency = 0;
    let mut frequencies = HashSet::new();
    frequencies.insert(0);

   loop {
        let file = File::open("input.txt").unwrap();
        let reader = BufReader::new(&file);
            
        for line in reader.lines() {
            frequency += line.unwrap().parse::<i32>().unwrap();
            if frequencies.contains(&frequency) {
                return frequency;
            }
            frequencies.insert(frequency);
        }
    }
}