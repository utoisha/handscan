@echo off
cd /d "C:\Users\admin\Desktop\hand"
echo starting project creation...
"C:\Program Files\FreeCAD 1.0\bin\freecadcmd.exe" add.py
echo checking created files:
dir *.FCStd
pause