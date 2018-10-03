#!/bin/sh
if [ ! -e "$1/main.py" ]; then
  echo "'$1/main.py' doesn't exist"
  exit
fi

PYTHONPATH=./ python -m pytest ./$1


