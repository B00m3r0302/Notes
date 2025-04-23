@echo off
echo Building implant...
nim c -d:release --opt:size --passL:-static --passC:-flto --passL:-flto implant.nim
echo Done!
pause
