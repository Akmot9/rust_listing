# Results
commande: 
```bash
find / -type f
```
## Without 'sudo' 
### Numbers of files and errors
```
╰─$ cat list_files.txt | wc -l
3816197

╰─$ cat list_files.log | wc -l
10
```
### Speed
Execution time: 13.319080936 seconds
### type of files 
{'regular_files': 3810572, 'directories': 0, 'symbolic_links': 0, 'pipes': 0, 'sockets': 0, 'unknown': 5625, 'total': 3816197}
### root directories
{'timeshift': 1644277, 'snap': 215211, 'opt': 111, 'boot': 316, 'run': 1111, 'root': 3604, 'var': 332042, 'sys': 83260, 'tmp': 8, 'home': 910853, 'swapfile': 1, 'etc': 2187, 'proc': 337711, 'dev': 2, 'usr': 285503}