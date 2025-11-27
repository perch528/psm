@echo off
REM Build script for psm
pyinstaller -F .\master.py
pyinstaller -w -F .\minion.py
copy .\dist\master.exe .\final\
copy .\dist\minion.exe .\final\