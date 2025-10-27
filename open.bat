@echo off
cd /d "C:\Users\admin\Desktop\hand"

echo new file: test.FCStd
echo open file...

:: Используем полный путь к FreeCAD
"C:\Program Files\FreeCAD 1.0\bin\freecad.exe" "test.FCStd"

echo Файл должен открыться в FreeCAD
pause