@echo off

REM ADD Stage area
git add -A

REM Ejecutar commit interactivo
set /p comment="Enter comment: "
git commit -m "%comment%"

REM Mostrar mensaje de confirmación
echo Commit sucessful.
