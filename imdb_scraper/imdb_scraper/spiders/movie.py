# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import open_in_browser

SEARCH_QUERY = (
    'https://www.imdb.com/search/title?'
    'title_type=feature&'
    'user_rating=1.0,10.0&'
    'countries=us&'
    'languages=en&'
    'count=1&'
    'view=simple'
)

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['imdb.com']
    start_urls = [SEARCH_QUERY]

    rules = (Rule(
        LinkExtractor(
            #restrict_css=('div.desc a')
            allow=r".*/title/tt.*/?ref_"
        ),
        follow=False,
        callback='parse_query_page',
    ),)

    def parse_query_page(self, response):

        self.logger.info('parse_query_page:')
        self.logger.info(response)

        data = {}

        # global infos
        data['title'] = response.css('h1 > span::text').extract_first()
        data['summary'] = ''
        data['rating'] = response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"] > span::text').extract_first()
        data['ratingCount'] = response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"] > span::text').extract()[2]
        data['duration'] = response.css('ul[role="presentation"] > li::text').extract_first()
        data['releaseDate'] = response.css('ul[role="presentation"] > li::text').extract()[1]
        data['year'] = response.css('ul[role="presentation"] > li::text').extract()[1].split(' ')[2]
        data['vote'] = response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"]+div+div::text').extract_first()

        # pics
        data['minPicUrl'] = response.css('div[data-testid="hero-media__poster"] > div > img').attrib['src']
        data['minPicWidth'] = response.css('div[data-testid="hero-media__poster"] > div > img').attrib['width']
        data['minPicAlt'] = response.css('div[data-testid="hero-media__poster"] > div > img').attrib['alt']
        data['picsUrls'] = response.css('div[data-testid="hero-media__poster"] > div > img').attrib['srcset'].split(' ')
        picdef = data['picsUrls'][0]
        t = picdef.split('.')
        t.pop()
        data['picFullUrl'] = '.'.join(t).split(',')[0]
        data['picsSizes'] = response.css('div[data-testid="hero-media__poster"] > div > img').attrib['sizes'].split(',')

        # casting

        #open_in_browser(response)

        data['metascore'] = response.xpath(
            '//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
        data['img_url'] = response.xpath(
            '//div[contains(@class, "poster")]/a/img/@src').extract_first()
        countries = response.xpath(
            '//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
        data['countries'] = [country.strip() for country in countries]
        languages = response.xpath(
            '//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
        data['languages'] = [language.strip() for language in languages]
        actors = response.xpath('//td[not(@class)]/a/text()').extract()
        data['actors'] = [actor.strip() for actor in actors]
        genres = response.xpath(
            "//div[contains(.//h4, 'Genres')]/a/text()").extract()
        data['genre'] = [genre.strip() for genre in genres]
        tagline = response.xpath(
            '//div[contains(string(), "Tagline")]/text()').extract()
        data['tagline'] = ''.join(tagline).strip() or None
        data['description'] = response.xpath(
            '//div[contains(@class, "summary_text")]/text()').extract_first().strip() or None
        directors = response.xpath(
            "//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or None
        if directors:
            data['directors'] = [director.strip() for director in directors]
        data['runtime'] = response.xpath(
            "//div[contains(@class, 'txt-block') and contains(.//h4, 'Runtime')]/time/text()").extract_first() or None
        data['imdb_url'] = response.url.replace('?ref_=adv_li_tt', '')

        yield data
