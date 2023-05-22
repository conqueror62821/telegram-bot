@echo off

REM ADD Stage area
git add -A

REM Interactive commit
set /p comment="Enter comment: "
git commit -m "%comment%"

REM Successfully message
cls
echo Commit successfully :D
