#!/bin/bash


#!/bin/bash

# Get the current time in nanoseconds
current_time=$(date +%s%N)

# Check if the argument is "obs"
if [ "$1" == "obs" ]; then
  # Change to the ~/Documents/workspace_/receitas directory
  cd ~/Documents/workspace_/receitas

  # Add all changes in the current directory to the index
  git add .

  # Commit the changes with the current time as the commit message
  git commit -m "$current_time"

  # Push the changes to the remote repository
  git push
elif [ "$1" == "dot" ]; then
  # Change to the ~/Documents/workspace_/receitas directory
  cd ~/.dotfiles

  # Add all changes in the current directory to the index
  git add .

  # Commit the changes with the current time as the commit message
  git commit -m "$current_time"

  # Push the changes to the remote repository
  git push

else
  echo "Invalid argument. Try "obs, dot""
fi
