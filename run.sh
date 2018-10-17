#!/bin/sh
if [ ! -e "$1/main.py" ]; then
  echo "'$1/main.py' module doesn't exist"
  exit
fi
PYTHONPATH=./ python $1/main.py


