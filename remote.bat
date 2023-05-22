@echo off

REM pull request
echo ^[[32mGit pull..^[[0m
git pull
if %errorlevel% neq 0 (
    echo ^[[31;47mError when doing git pull :c^[[0m
    pause
    exit /b
)

REM push request
echo ^[[32mGit push..^[[0m
git push
if %errorlevel% neq 0 (
    echo ^[[31;47mError when doing git push :c^[[0m
    pause
    exit /b
)

REM successful
echo ^[[Operations carried out successfully :D^[[0m
pause
