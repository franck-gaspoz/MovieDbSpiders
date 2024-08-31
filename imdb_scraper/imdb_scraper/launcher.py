import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import imdb_scraper

# useful if you have settings.py
from imdb_scraper.imdb_scraper.spiders.movie import MovieSpider

settings = get_project_settings()

# Create a process
process = CrawlerProcess( settings )
process.crawl(MovieSpider)
process.start()
