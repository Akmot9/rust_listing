import matplotlib.pyplot as plt

# Type of Files
file_types = {'regular_files': 4050860, 'directories': 438632, 'symbolic_links': 38448, 'pipes': 13, 'sockets': 132, 'unknown': 129523, 'total': 4657608}

# Root Directories
root_directories = {'/': 1, 'timeshift': 2052013, 'lost+found': 1, 'snap': 321586, 'sbin': 1, 'cdrom': 1, 'opt': 124, 'boot': 313, 'libx32': 1, 'run': 2291, 'root': 1, 'var': 326400, 'mnt': 1, 'sys': 60900, 'tmp': 229, 'bin': 1, 'lib32': 1, 'media': 2, 'home': 1028934, 'swapfile': 1, 'etc': 4099, 'lib64': 1, 'proc': 491679, 'srv': 1, 'dev': 712, 'lib': 1, 'usr': 368657}

# Plotting the Type of Files
labels = list(file_types.keys())
counts = list(file_types.values())

plt.figure(figsize=(8, 5))
plt.bar(labels, counts)
plt.title("Type of Files")
plt.xlabel("File Types")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting the Root Directories
labels = list(root_directories.keys())
counts = list(root_directories.values())

plt.figure(figsize=(10, 6))
plt.bar(labels, counts)
plt.title("Files Count per Root Directory")
plt.xlabel("Root Directories")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
