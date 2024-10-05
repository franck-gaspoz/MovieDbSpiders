from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys

settings = get_project_settings()

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
if len(sys.argv) > 3:
    filters = sys.argv[3]

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
