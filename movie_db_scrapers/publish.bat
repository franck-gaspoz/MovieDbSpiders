@rem publish stand alone .exe
@rem made with auto-py-to-ex
@rem syntax: publish.bat <nover>
@rem   <nover> : version number
@rem   example: publish.bar 1.1.0

del .\dist\M*
del dist/launcher.exe

pyinstaller --noconfirm --onefile --console ".\launcher.py"

cd dist
rename "launcher.exe" "movie-db-scrapper-windows-64bit-intel-%1.exe "
dir
