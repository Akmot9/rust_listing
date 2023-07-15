# Results
commande: 
```bash
find /
```
## Without 'sudo' 
### Numbers of files and errors
```
╰─$ cat list_files.txt | wc -l
5463471

╰─$ cat list_files.log | wc -l
3905
```
### Speed
Execution time: 10.583639236 seconds
### type of files 
{
    'regular_files': 4724167, 
    'directories': 503656, 
    'symbolic_links': 52261, 
    'pipes': 13, 
    'sockets': 141, 
    'unknown': 182887, 
    'total': 5463125
}
### root directories
{
    '/': 1, 
    'timeshift': 2728785, 
    'lost+found': 1, 
    'snap': 321586, 
    'sbin': 1, 
    'cdrom': 1, 
    'opt': 124, 
    'boot': 313, 
    'libx32': 1, 
    'run': 2354, 
    'root': 1, 
    'var': 326357, 
    'mnt': 1, 
    'sys': 61092, 
    'tmp': 260, 
    'bin': 1, 
    'lib32': 1, 
    'media': 2, 
    'home': 1026541, 
    'swapfile': 1, 
    'etc': 4098, 
    'lib64': 1, 
    'proc': 625735, 
    'srv': 1, 
    'dev': 713, 
    'lib': 1, 
    'usr': 365498
}