# Movie Db Scraper

![python](https://img.shields.io/static/v1?label=&message=Python&color=cdf998&style=plastic&logo=python)
![json](https://img.shields.io/static/v1?label=&message=JSON&color=cdf998&style=plastic&logo=javascript&logoColor=darkgreen) 
![linux](https://img.shields.io/static/v1?label=&message=Linux&color=285fdd&style=plastic&logo=linux) ![windows](https://img.shields.io/static/v1?label=&message=Windows&color=285fdd&style=plastic&logo=windows&logoColor=77DDFF) ![osx](https://img.shields.io/static/v1?label=&message=OSX&color=285fdd&style=plastic&logo=apple&logoColor=AAFFAA)

![release](https://img.shields.io/github/release-date-pre/franck-gaspoz/MovieDbScraper?&style=plastic&label=release)
![release](https://img.shields.io/github/v/release/franck-gaspoz/MovieDbScraper?&style=plastic&label=)

## Overview

This is a [Scrapy](https://github.com/scrapy/scrapy) project to crawl movie 'databases' web sites.
Currently these sites are supported:
- [IMDB](https://www.imdb.com/)

this software scrap movies' information and then store the data in `json` format. 

## Get & Run release

### Download a  release:

- [MovieDbScrapper-Windows-64bit-intel-1.1.0](https://github.com/franck-gaspoz/MovieDbScraper/releases/tag/1.1.0)
- [MovieDbScrapper-Windows-64bit-intel-1.0.0](https://github.com/franck-gaspoz/MovieDbScraper/releases/tag/1.0.0)

links to a standalone executable (windows,64bit intel) and release source archive

### Usage:

```bash
# run the crawler:
#  - choose which spider to use
#  - search for movies having <Title>
#  - eventually use extended filters if specified in <Filters>
#  - output to a json file

# exemple:

./movie-db-scrapper-1.1.0.exe imdb movies.json "Any movie" countries=US&languages=US&count=10
```

#### syntaxes:

- `<SpiderId> <OutputFile> <Title> [<Filters>]`
- `-l | --list`
- `-h | --help`

#### arguments:

- `SpiderId`: id of the spider to use. currently only one is accepted: `imdb`
- `OutputFile`: relative or absolute path to the `Json` outputs
- `Title` : search the title
- `Filters` : optional filters. default is `countries=US&languages=FR&count=10`
- `-l | --list` : dump spiders ids (one per line)
- `-h | --help` : dump the help

## Install & run / develop

1. Clone the repo and navigate into `IMDBsScraper` folder.
```bash
$ git clone https://github.com/franck-gaspoz/MovieDbScraper.git
$ cd MovieDbScraper/
```
2. Create and activate a virtual environment.
```bash
(MovieDbScraper) $ pipenv shell
```
3. Install all dependencies.
```bash
(MovieDbScraper)$ pipenv install
```
4. Navigate into `imdb_scraper` folder.
```bash
(MovieDbScraper) $ cd movie_db_scrapers/
```

5. Start the crawler named `imdb` :
```
syntax:

scrapy crawl imdb [-O <OUTPUT_FILE>] -L <LOG_LEVEL> [-a title=<TITLE>] [-a filters=<FILTERS>]

* default file: ./data/movie.json
* -O <OUTPUT_FILE>      : write in file <OUTPUT_FILE>
* -L <LOG_LEVEL>        : CRITICAL | ERROR | WARNING | INFO | DEBUG
* -a title=<TITLE>      : search movie with <TITLE> (default: '')
* -a filters=<FILTERS>  : query filters. reference is https://www.imdb.com/search/title? (default: 'countries=US&languages=FR&count=10')

# exemple filters:
# user-rating           1.0,10.0
# countries             US
# languages             EN
# count                 10

example:

(MovieDbScraper/movie_db_scrapers) $ scrapy crawl movie -O data/movie.json -L ERROR -a title="alien" -a filters="countries=US&languages=FR&count=10" 
```

You can get your own query from here: [imdb.com/search/title](https://www.imdb.com/search/title). Copy the generated URL and 
put it into the `filters` parameter in the command line

```bash
(MovieDbScraper/movie_db_scrapers) $ scrapy crawl -h
```

6. Data will be stored in `json` file named `movie.json` located at `MovieDbScraper/movie_db_scrapers/data/movie.json`.

The final data will be structured like this (an object per movie in an array):

```json
[{
    "title": "Alien: Romulus",
    "summary": "Des jeunes d'un monde lointain doivent affronter la forme de vie la plus terrifiante de l'univers.",
    "interests": ["Monster Horror", "Space Sci-Fi", "Horror", "Sci-Fi", "Thriller"],
    "rating": "7,4",
    "ratingCount": "10",
    "duration": "1h 59min",
    "releaseDate": "13 ao\u00fbt 2024",
    "year": "2024",
    "vote": "76\u00a0k",
    "director": "Fede Alvarez",
    "writers": ["Fede Alvarez", "Rodo Sayagues", "Dan O'Bannon"],
    "stars": ["Cailee Spaeny", "David Jonsson", "Archie Renaux"],
    "actors": [{
        "actor": "Cailee Spaeny",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BMTU1NzA0MjEwNV5BMl5BanBnXkFtZTgwNTE5ODczNjM@._V1_QL75_UX140_CR0,0,140,140_.jpg"],
        "characters": ["Rain"]
    }, {
        "actor": "David Jonsson",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BOGZjZjZhYzUtNjkyZi00MjQyLTliNjYtMDMxNDc2NDlhOTU5XkEyXkFqcGdeQXVyOTA2MTgwNTA@._V1_QL75_UX140_CR0,16,140,140_.jpg"],
        "characters": ["Andy"]
    }, {
        "actor": "Archie Renaux",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BZmUxZmY1NGQtMmIzYS00OWE2LThkNTgtNDYyMDI3Njg4MDdiXkEyXkFqcGdeQXVyODg4NzYxNTM@._V1_QL75_UX140_CR0,1,140,140_.jpg"],
        "characters": ["Tyler"]
    }, {
        "actor": "Isabela Merced",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BYWE3ZGI0NWEtOGE1YS00NGVmLTg1ZWQtOThkOWI2MWUyZmU1XkEyXkFqcGc@._V1_QL75_UX140_CR0,12,140,140_.jpg"],
        "characters": ["Kay"]
    }, {
        "actor": "Spike Fearn",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BYWEzODJmN2YtZjgxYy00ZGUxLWFkZWYtZTM4OTY0MDY2NzA0XkEyXkFqcGc@._V1_QL75_UX140_CR0,0,140,140_.jpg"],
        "characters": ["Bjorn"]
    }, {
        "actor": "Aileen Wu",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BNmVkY2IwNmYtNDRhYy00ZDBmLTlmODEtMDk5N2M4ZGMxNzRmXkEyXkFqcGdeQXVyMTM1NjU0NjI0._V1_QL75_UX140_CR0,12,140,140_.jpg"],
        "characters": ["Navarro"]
    }, {
        "actor": "Rosie Ede",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BMTQ4NzkwNzk0M15BMl5BanBnXkFtZTgwMzAwMzIyNjE@._V1_QL75_UX140_CR0,0,140,140_.jpg"],
        "characters": ["WY Officer"]
    }, {
        "actor": "Soma Simon",
        "picUrl": null,
        "characters": ["10-Year Old Punk #1"]
    }, {
        "actor": "Bence Okeke",
        "picUrl": null,
        "characters": ["10-Year Old Punk #2"]
    }, {
        "actor": "Viktor Orizu",
        "picUrl": null,
        "characters": ["10-Year Old Punk #3"]
    }, {
        "actor": "Robert Bobroczkyi",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BMmVhYmU5NDgtMWI0Ny00MzA0LTk4MmMtNDEzMDI3MzMxYjFlXkEyXkFqcGc@._V1_QL75_UX140_CR0,12,140,140_.jpg"],
        "characters": ["Offspring"]
    }, {
        "actor": "Trevor Newlin",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BODMzNTM1NTAtNTUxZC00OGNjLWI3NGUtMzY5ZjVmZDQxODhlXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_QL75_UX140_CR0,12,140,140_.jpg"],
        "characters": ["Xenomorph"]
    }, {
        "actor": "Annemarie Griggs",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BYTVhMjE3MmEtMjVhMC00ZDU2LTljOWMtZmVhZTI3YzhlZDA5XkEyXkFqcGdeQXVyMTczNTQwOTE@._V1_QL75_UX140_CR0,1,140,140_.jpg"],
        "characters": ["Voice of MU", "(voix)", "\u2026"]
    }, {
        "actor": "Ian Holm",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BMTI0ODA2MjM2NF5BMl5BanBnXkFtZTYwNDg5NDIz._V1_QL75_UX140_CR0,13,140,140_.jpg"],
        "characters": ["Rook (facial and vocal reference)"]
    }, {
        "actor": "Daniel Betts",
        "picUrl": ["https://m.media-amazon.com/images/M/MV5BMTU0NjIxNjg4NV5BMl5BanBnXkFtZTgwOTE4NTc1MDI@._V1_QL75_UX140_CR0,12,140,140_.jpg"],
        "characters": ["Rook (facial and vocal performance)"]
    }],
    "anecdotes": "Director Fede Alvarez sought out the special effects crew from Aliens, le retour (1986) to work on the creatures. Physical sets, practical creatures, and miniatures were used wherever possible to help ground later VFX work.When the characters first enter the space station, the artificial gravity briefly turns on and then off again. Shortly thereafter, they enter a room where several objects are hovering in mid-air. If the objects had momentum immediately after the gravity switched off they should be moving on a trajectory, and if not they should still be against the floor. Either way, they should not be unmoving several feet off the floor.Andy: The solution for a claustrophobic astronaut is to give him more space.The 20th Century Studios fanfare freezes and turns ominous, as in Alien\u00b3 (1992), leading into the film's opening scene.The logo itself suffers a burst of static and turns green.Featured in Nerdrotic: The Acolyte: Force is Female CONFIRMED? The Death of Theaters - The Real BBC @MauLer @HeelvsBabyface (2024)Theme from AlienWritten by Jerry Goldsmith",
    "minPicUrl": "https://m.media-amazon.com/images/M/MV5BMDU0NjcwOGQtNjNjOS00NzQ3LWIwM2YtYWVmODZjMzQzN2ExXkEyXkFqcGc@._V1_QL75_UX190_CR0,0,190,281_.jpg",
    "minPicWidth": "190",
    "minPicAlt": "Aileen Wu in Alien: Romulus (2024)",
    "picsUrls": ["https://m.media-amazon.com/images/M/MV5BMDU0NjcwOGQtNjNjOS00NzQ3LWIwM2YtYWVmODZjMzQzN2ExXkEyXkFqcGc@._V1_QL75_UX190_CR0,0,190,281_.jpg", "https://m.media-amazon.com/images/M/MV5BMDU0NjcwOGQtNjNjOS00NzQ3LWIwM2YtYWVmODZjMzQzN2ExXkEyXkFqcGc@._V1_QL75_UX285_CR0,0,285,422_.jpg", "https://m.media-amazon.com/images/M/MV5BMDU0NjcwOGQtNjNjOS00NzQ3LWIwM2YtYWVmODZjMzQzN2ExXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"],
    "picFullUrl": "https://m.media-amazon.com/images/M/MV5BMDU0NjcwOGQtNjNjOS00NzQ3LWIwM2YtYWVmODZjMzQzN2ExXkEyXkFqcGc@._V1_QL75_UX190_CR0",
    "picsSizes": ["50vw", " (min-width: 480px) 34vw", " (min-width: 600px) 26vw", " (min-width: 1024px) 16vw", " (min-width: 1280px) 16vw"]
}]
```


### Stats

These are the **FINAL** stats when the default `SEARCH_QUERY` is used.

```python3
{'downloader/request_bytes': 1357,
 'downloader/request_count': 4,
 'downloader/request_method_count/GET': 4,
 'downloader/response_bytes': 458312,
 'downloader/response_count': 4,
 'downloader/response_status_count/200': 3,
 'downloader/response_status_count/308': 1,
 'elapsed_time_seconds': 3.196772,
 'feedexport/success_count/FileFeedStorage': 2,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2024, 8, 30, 20, 53, 51, 544194, tzinfo=datetime.timezone.utc),
 'httpcompression/response_bytes': 2191057,
 'httpcompression/response_count': 2,
 'item_scraped_count': 1,
 'log_count/DEBUG': 6,
 'log_count/INFO': 14,
 'log_count/WARNING': 2,
 'request_depth_max': 1,
 'response_received_count': 3,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 3,
 'scheduler/dequeued/memory': 3,
 'scheduler/enqueued': 3,
 'scheduler/enqueued/memory': 3,
 'start_time': datetime.datetime(2024, 8, 30, 20, 53, 48, 347422, tzinfo=datetime.timezone.utc)
 }
 ```

## Build a standalone executable

```bash
$ cd MovieDbScraper/movie_db_scrapers
(MovieDbScraper/movie_db_scrapers) $ ./publish.bat 1.1.0
```

this will build the file `movie-db-scrapper-windows-64bit-intel-1.1.0.exe` in the `/dist` folder

## Releases

1.1.0 - 2024/08/10 - support for multiple spiders

- refactoring: imdb-scrapper -> movie_db_scrappers
- move settings to launcher
- command line improvements (launcher.py)
- fix bug call executable from any path module error
- minor bugs fixes

1.0.0 - 2024/20/05 - initial version

- scrap from command line

## Notes

This project is a based on a fork of the project [https://github.com/dojutsu-user/IMDB-Scraper](https://github.com/dojutsu-user/IMDB-Scraper) from **Vaibhav Gupta** (2018,MIT)

## Disclaimer

The project and the obtained dataset is intended only for educational purpose. It is completely open source and has no value intentions to commercialise complete or any part of the same. The developer is on no part the owner of any resources used and does not claim to hold the permissions to use the project.
