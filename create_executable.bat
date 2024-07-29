@ECHO OFF
set arg1=%1

ECHO(
ECHO == Updating Python packages ==
pip install pyinstaller

ECHO(
ECHO == Running pyinstaller ==
pyinstaller --onefile %arg1%

ECHO(
ECHO == Deleting temp files ==
move dist\*.exe .\
rmdir dist
rmdir /s /q build
del /f *.spec
