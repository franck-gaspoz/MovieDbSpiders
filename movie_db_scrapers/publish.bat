@rem publish stand alone .exe
@rem made with auto-py-to-ex
@rem syntax: publish.bat <nover>
@rem   <nover> : version number
@rem   example: publish.bar 1.1.0

pipenv shell

del .\dist\M*
del dist/launcher.exe

pyinstaller --paths="C:\Users\franc\PycharmProjects\MovieDbScraper" --paths="C:\Users\franc\PycharmProjects\MovieDbScraper\movie_db_scrapers" --noconfirm --onefile --console ".\launcher.py"

cd dist
rename "launcher.exe" "movie-db-scrapper-windows-64bit-intel-%1.exe "
dir
