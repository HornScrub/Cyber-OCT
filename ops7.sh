#!/bin/bash
# Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

# Create a new bash script that performs the following:

# Prompts user for input directory path or file.
echo "Enter a directory path: "
read input_path

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777, 775, 664)
echo "Enter permissions number (777, 775, 664): "
read input_number

# Navigates to the directory input by the user and changes all files inside it to the input setting.
cd "$input_path"
chmod -R "$input_number" .

# Prints to the screen the directory contents and the new permissions settings of everything in the directory or file you selected.
ls -l

