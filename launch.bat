@echo off

set VENV_PATH=%CD%\.env\Scripts\activate
call %VENV_PATH%

python main.py

pause