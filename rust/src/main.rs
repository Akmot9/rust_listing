//use std::fs;
use walkdir::WalkDir;

fn main() {
    let mut count = 0;
    for entry in WalkDir::new("/").into_iter().filter_map(|entry| entry.ok()) {
        let path = entry.path();
        if path.is_file() {
            //println!("{}", path.display());
            count+=1;
        }
    }
    println!("{}", count);
}