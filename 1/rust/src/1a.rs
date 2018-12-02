use std::io::BufReader;
use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let f = try!(File::open("input.txt"));
    let file = BufReader::new(&f);

    let sum = file.lines()
                  .fold(0, |sum, line| sum + line.unwrap().parse::<i32>().unwrap());

    println!("sum: {}", sum);
    Ok(())
}