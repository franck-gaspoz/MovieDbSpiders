from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

# Create a process
process = CrawlerProcess( settings )
process.crawl('movie')
process.start()
