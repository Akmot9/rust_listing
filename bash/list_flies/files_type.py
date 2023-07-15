import os
import stat

def count_file_types(file_path):
    regular_files = 0
    directories = 0
    symbolic_links = 0
    pipes = 0
    sockets = 0
    unknown =0
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                file_type = os.stat(line).st_mode

                if os.path.isfile(line):
                    regular_files += 1
                elif os.path.isdir(line):
                    directories += 1
                elif os.path.islink(line):
                    symbolic_links += 1
                elif stat.S_ISFIFO(file_type):
                    pipes += 1
                elif stat.S_ISSOCK(file_type):
                    sockets += 1

            except FileNotFoundError:
                print(f"File or directory not found: {line}")
                unknown+=1
            except OSError as e:
                if e.errno == 40:
                    unknown+=1
                    print(f"Too many levels of symbolic links: {line}")
                else:
                    unknown+=1
                    print(f"Error accessing file or directory: {line}, {e}")
    
    result = {
        'regular_files': regular_files,
        'directories': directories,
        'symbolic_links': symbolic_links,
        'pipes': pipes,
        'sockets': sockets,
        'unknown': unknown,
        'total':unknown+sockets+pipes+symbolic_links+
        directories+regular_files
    }
    
    return result

def count_files_per_directory(file_path):
    result = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            directory = line.split('/')[1]
            if directory in result:
                result[directory] += 1
            else:
                result[directory] = 1
    
    return result


path_files = "/home/akmot/Documents/GitHub/rust_listing/bash/list_flies/list_files.txt"
liste_types_files = count_files_per_directory(path_files)
print(liste_types_files)
