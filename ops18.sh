#!/bin/bash

# Today's challenges is to create a script in bash that navigates to the document directory and list the files in there
# Then ask the user to create or edit a file, and then opens the file up in the terminal

cd ~/Documents
ls

read -p "Enter the name of the file you wish to create/edit: " aFileName
nano $aFileName
cat $aFileName

