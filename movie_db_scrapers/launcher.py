from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys
import os
from movie_db_scrapers.spiders.imdb import ImdbSpider

#from movie_db_scrapers.movie_db_scrapers.spiders.imdb import ImdbSpider

settings = get_project_settings()

# intro

settings.set('BOT_NAME', 'movie_db_scrapers')
settings.set('SPIDER_MODULES', ['movie_db_scrapers.spiders'])
settings.set('NEWSPIDER_MODULE', 'movie_db_scrapers.spiders')
settings.set('ROBOTSTXT_OBEY', True)

SPIDERS_LIST = ['imdb']


def dump_title():
    sys.stdout.write('| MovieDbScraper 1.1.1 |\n')


def sep():
    #                 | MovieDbScraper x.y.z |
    sys.stdout.write('| ----------------------\n')


def help():
    sys.stdout.write('| ----------------------------------------------------------------------------------\n')
    sys.stdout.write('|  website crawler | scrap movies information and then store the data in json format\n')
    sys.stdout.write('|  project link: https://github.com/franck-gaspoz/MovieDbScraper\n')
    sys.stdout.write('| ----------------------------------------------------------------------------------\n')
    sys.stdout.write('\n')
    sys.stdout.write('syntaxes: \n')
    sys.stdout.write('----------\n')
    sys.stdout.write('1: <SpiderId> <OutputFile> <Title> [<Filters>]\n')
    sys.stdout.write('2: -h | --help\n')
    sys.stdout.write('\n')
    sys.stdout.write('arguments:\n')
    sys.stdout.write('----------\n')
    sys.stdout.write('<SpiderId>   : id of the invoked spider (eg: imdb). always in lower case\n')
    sys.stdout.write('<OutputFile> : absolute or relative path of the json file output\n')
    sys.stdout.write('<Title>      : query movies having title like this one\n')
    sys.stdout.write('<Filters>    : optional filters. default is: "countries=US&languages=EN&count=10"\n')
    sys.stdout.write('-h | --help  : dump this text and exit')
    sys.stdout.write('\n')


def list_spiders():
    for spiderI in SPIDERS_LIST:
        sys.stdout.write(spiderI+'\n')


# default output file
outputFile = None
# default title
title = None
# default filters
filters = None
# scraper id
spiderId = None

# parse args
# <SpiderId> <OutputFile> <Title> [<Filters>]
# -h | --help
# -l | --list

k = len(sys.argv)

if k == 2 and sys.argv[1] == '-h' or sys.argv[1] == '--help':
    dump_title()
    help()
    sys.exit(0)

if k == 2 and sys.argv[1] == '-l' or sys.argv[1] == '--list':
    list_spiders()
    sys.exit(0)

dump_title()

if k > 1:
    spiderId = sys.argv[1]
if k > 2:
    outputFile = sys.argv[2]
if k > 3:
    title = sys.argv[3]
if k > 4:
    filters = sys.argv[4]
if k < 4 or len(sys.argv) > 5:
    help()
    sys.stderr.write("ERROR:\n")
    sys.stderr.write('bad number of parameters. expected: 1, or 3 or 4, but got: ' + str(len(sys.argv) - 1) + '\n')
    sys.exit(0)

sys.stdout.write('## outputFile=' + outputFile + '\n')
sys.stdout.write('## spiderId=' + spiderId + '\n')
sys.stdout.write('## title=' + title + '\n')
if filters is not None:
    sys.stdout.write('## filters=' + filters + '\n')

# setup

feeds = {outputFile: {
    'format': 'json',
    'overwrite': True
}}
settings.get('FEEDS').update(feeds)

# setup modules


def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")


def module_path():
    if we_are_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


#modPath = module_path()
#sys.stdout.write('modPath='+modPath + '\n')
#sys.path.append(modPath)
#baseName = modPath + '/' + os.path.basename(sys.argv[0])
#sys.stdout.write('baseName='+baseName+'\n')
#sys.path.append(baseName)
#sys.stdout.write(str(sys.path)+'\n')

#module = importlib.import_module('movie_db_scrapers.spiders.' + spiderId)
#sys.stdout.write(str(module)+'\n')

#mclass = getattr( module, spiderId.title() + 'Spider')
#sys.stdout.write(str(mclass)+'\n')


# Create a process
process = CrawlerProcess(settings)

process.crawl(ImdbSpider, title=title, filters=filters)

process.start()
