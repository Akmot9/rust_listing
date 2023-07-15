# Results
commande: 
```bash
sudo find /
```
## Without 'sudo' 
### Numbers of files and errors
```
╰─$ cat list_files.txt | wc -l
4854982

╰─$ cat list_files.log | wc -l
9
```
### Speed
Execution time: 50.736926659 seconds
### type of files 
{'regular_files': 4050860, 'directories': 438632, 'symbolic_links': 38448, 'pipes': 13, 'sockets': 132, 'unknown': 129523, 'total': 4657608}
### root directories
{'/': 1, 'timeshift': 2052013, 'lost+found': 1, 'snap': 321586, 'sbin': 1, 'cdrom': 1, 'opt': 124, 'boot': 313, 'libx32': 1, 'run': 2291, 'root': 1, 'var': 326400, 'mnt': 1, 'sys': 60900, 'tmp': 229, 'bin': 1, 'lib32': 1, 'media': 2, 'home': 1028934, 'swapfile': 1, 'etc': 4099, 'lib64': 1, 'proc': 491679, 'srv': 1, 'dev': 712, 'lib': 1, 'usr': 368657}

## Conclusion
### time
5x longer than without sudo
### listing
more files
less errors