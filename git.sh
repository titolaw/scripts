#!/bin/bash

# Takes an argument, changes to a folder and commits all the changes.

# Get the time in nanoseconds
current_time=$(date +%s%N)

if [ "$1" == "obs" ]; then
  cd ~/Documents/workspace_/receitas
  git add .
  git commit -m "$current_time"
  git push
elif [ "$1" == "dot" ]; then
  cd ~/.dotfiles
  git add .
  git commit -m "$current_time"
  git push
else
  echo "Invalid argument. Try "obs, dot""
fi
