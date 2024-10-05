rem publish stand alone .exe
rem made with auto-py-to-ex
pyinstaller --noconfirm --onefile --console --hidden-import ""  ".\launcher.py"
