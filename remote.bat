@echo off

REM pull request
echo Git pull..
git pull
if %errorlevel% neq 0 (
    echo Error when doing git pull :c
    pause
    exit /b
)

pause
cls

REM push request
echo Git push..
git push
if %errorlevel% neq 0 (
    echo Error when doing git push :c
    pause
    exit /b
)
cls

REM successful
echo Operations carried out successfully :D
pause
