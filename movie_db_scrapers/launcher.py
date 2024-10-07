from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys

settings = get_project_settings()

# intro

sys.stdout.write('| MovieDbScraper 1.1.0 |\n')

settings.set('BOT_NAME','movie_db_scrapers')
settings.set('SPIDER_MODULES',['movie_db_scrapers.spiders'])
settings.set('NEWSPIDER_MODULE','movie_db_scrapers.spiders')
settings.set('ROBOTSTXT_OBEY',True)

def help():
    sys.stdout.write('| ----------------------------------------------------------------------------------\n')
    sys.stdout.write('|  website crawler | scrape movies information and then store the data in json format\n')
    sys.stdout.write('|  project link: https://github.com/franck-gaspoz/MovieDbScraper\n')
    sys.stdout.write('| ----------------------------------------------------------------------------------\n')
    sys.stdout.write('\n')
    sys.stdout.write('arguments:\n')
    sys.stdout.write('----------\n')
    sys.stdout.write('<OutputFile> <ScraperId> <Title> [<Filters>]\n')
    sys.stdout.write('\n')
    sys.stdout.write('<OutputFile> : absolute or relative path of the json file output\n')
    sys.stdout.write('<Title>      : query movies having title like this one\n')
    sys.stdout.write('<Filters>    : optional filters. default is: "countries=US&languages=EN&count=10"\n')
    sys.stdout.write('\n')
    sys.stdout.write('syntax: outputFile title [filters]=countries=US&languages=FR&count=10\n\n')


# default output file
outputFile = None
# default title
title = None
# default filters
filters = None
# scraper id
spiderId = None

# parse args
# <SpiderId> <OutputFile> <Title> [<filters>]

if len(sys.argv) > 1:
    spiderId = sys.argv[1]
if len(sys.argv) > 2:
    outputFile = sys.argv[2]
if len(sys.argv) > 3:
    title = sys.argv[3]
if len(sys.argv) > 4:
    filters = sys.argv[4]
if len(sys.argv) < 4 or len(sys.argv)>5:
    help()
    sys.stderr.write("ERROR:\n")
    sys.stderr.write('bad number of parameters. expected 3 or 4 args but got: '+str(len(sys.argv)-1)+'\n')
    sys.exit(0)

sys.stdout.write('## outputFile='+outputFile+'\n')
sys.stdout.write('## spiderId='+spiderId+'\n')
sys.stdout.write('## title='+title+'\n')
if filters is not None:
    sys.stdout.write('## filters='+filters+'\n')

# setup

feeds = {}
feed = {
    'format': 'json',
    'overwrite': True
}
feeds[outputFile] = feed

settings.get('FEEDS').update(feeds)

# Create a process
process = CrawlerProcess(settings)

if filters is not None:
    process.crawl(spiderId, title=title, filters=filters)
else:
    process.crawl(spiderId, title=title )

process.start()
