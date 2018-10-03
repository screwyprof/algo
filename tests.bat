@echo off
IF NOT EXIST "%1" (
  echo "'%1' doesn't exist"
  pause
  exit /B
)

SET PYTHONPATH=./
python -m pytest %1
