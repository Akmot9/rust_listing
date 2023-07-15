use walkdir::WalkDir;

fn main() {
    let mut count=0;
    for _ in WalkDir::new("/").into_iter().filter_map(|file| file.ok()) {
        //println!("{}", file.path().display());
        count+=1;
    }
    println!("{}", count)
}