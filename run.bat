@echo off
IF NOT EXIST "%1/main.py" (
  echo "'%1/main.py' doesn't exist"
  pause
  exit /B
) 

SET PYTHONPATH=./

python %1/main.py

