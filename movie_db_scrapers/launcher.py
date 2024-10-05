from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys

settings = get_project_settings()

# intro

sys.stdout.write('MovieDbScraper 1.1.0\n')
sys.stdout.write('--------------------')
sys.stdout.write('website crawler | scrape movies information and then store the data in json format\n')
sys.stdout.write('project link: https://github.com/franck-gaspoz/MovieDbScraper\n')
sys.stdout.write('\n')
sys.stdout.write('arguments:\n')
sys.stdout.write('OutputFile Title [Filters]\n')
sys.stdout.write('\n')
sys.stdout.write('OutputFile: absolute or relative path of the output json file\n')
sys.stdout.write('Title: query movies having title\n')
sys.stdout.write('Filters: optional filters. default is countries=US&languages=FR&count=10\n')
sys.stdout.write('\n')

# parse args
# outputFile title [filters]

sys.stdout.write('syntax: outputFile title [filters]=countries=US&languages=FR&count=10 \n')
outputFile = 'result.json'
title = ''
filters = None

if len(sys.argv) > 1:
    outputFile = sys.argv[1]
if len(sys.argv) > 2:
    title = sys.argv[2]
if len(sys.argv) == 3:
    filters = sys.argv[3]
if len(sys.argv)==0 or len(sys.argv)>3:
    sys.stderr.write('bad number of parameters\n')
    exit(0)

sys.stdout.write('outputFile='+outputFile+'\n')
sys.stdout.write('title='+title+'\n')
if filters is not None:
    sys.stdout.write('filters='+filters+'\n')

# setup

settings.FEEDS = {}
feeds = {
    'format': 'json',
    'overwrite': True
}
settings.FEEDS[outputFile] = feeds

# Create a process
process = CrawlerProcess(settings)
if filters is not None:
    process.crawl('movie', title=title, filters=filters)
else:
    process.crawl('movie', title=title )

process.start()
