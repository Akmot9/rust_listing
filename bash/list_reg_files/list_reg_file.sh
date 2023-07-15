#!/bin/bash

# Capture the start time
start_time=$(date +%s.%N)

# Run the find command, redirect output and errors
find / -type f > list_files.txt 2> list_files.log

# Capture the end time
end_time=$(date +%s.%N)

# Calculate the execution time
execution_time=$(echo "$end_time - $start_time" | bc)

# Display the execution time
echo "Execution time: $execution_time seconds"
