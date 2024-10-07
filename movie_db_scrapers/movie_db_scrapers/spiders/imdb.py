# -*- coding: utf-8 -*-

#
# parameters (-a name=value)
#
# title                 movie title             default: ''
# filters               query filters           default: 'countries=US&languages=EN&count=10'
#
# exemple filters:
# user-rating           1.0,10.0
# countries             US
# languages             EN
# count                 10
#
# must form a valid query, for example: title_type=feature&languages=fr


import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

QUERY_URL = 'https://www.imdb.com/search/title?'
DEFAULT_FILTERS = 'countries=US&languages=EN&count=10'
ATTR_TITLE = 'title'
ATTR_MUTE = 'mute'
ATTR_FILTERS = 'filters'

REFERRER = 'https://www.imdb.com'
USER_AGENT = 'PostmanRuntime/7.32.3'
ACCEPT_ENCODING = 'gzip, deflate, br, zstd'
ACCEPT_LANGUAGE = 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
CACHE_CONTROL = 'no-cache'

DEFAULT_REQUEST_HEADERS = "DEFAULT_REQUEST_HEADERS"


class ImdbSpider(CrawlSpider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    rules = (Rule(
        LinkExtractor(
            # pages of details
            allow=r".*/title/tt.*/?ref_=sr_t"
        ),
        follow=False,
        callback='parse_detail_page',
    ),)

    @staticmethod
    def s(o):
        return o if o is not None else ''

    @staticmethod
    def q(name, value):
        return name + '=' + value if value is not None else ''

    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)
        h = {
            'Referer': REFERRER,
            'User-Agent': USER_AGENT,
            'accept-encoding': ACCEPT_ENCODING,
            # setup lang here. /!\ may change parse patterns
            'accept-language': ACCEPT_LANGUAGE,
            'cache-control': CACHE_CONTROL
        }
        settings.set(DEFAULT_REQUEST_HEADERS, h, priority="spider")

    def __init__(self, **kwargs):

        if kwargs is not None:
            self.title = kwargs[ATTR_TITLE] if ATTR_TITLE in kwargs else None
            self.filters = kwargs[ATTR_FILTERS] if ATTR_FILTERS in kwargs else DEFAULT_FILTERS
            self.logger.info(ATTR_TITLE + '=' + ImdbSpider.s(self.title))
            self.logger.info(ATTR_FILTERS + '=' + ImdbSpider.s(self.filters))

        title = ImdbSpider.q(ATTR_TITLE, self.title)
        sep1 = '&' if title is not None else ''
        filters = ImdbSpider.q(ATTR_FILTERS, self.filters)
        self.start_urls = [QUERY_URL + title + sep1 + filters]

        super().__init__(**kwargs)

    @staticmethod
    def exf(selector):
        return selector.extract_first() if len(selector) > 0 else None

    def ex(self, selector):
        return selector.extract() if len(selector) > 0 else None

    def atr(self, selector, attr):
        return selector.attrib[attr] if len(selector) > 0 else None

    def isUrl(self, text):
        return text.startswith('http')

    def parse_detail_page(self, response):

        self.logger.info('parse_detail_page:')
        self.logger.info(response)

        # ids

        data = {'url': response.url.split('?')[0]}
        t = response.url.split('?')[0].split('/')
        t = list(filter(lambda x: x != '',t))
        data['id'] = t.pop()

        # global infos

        data['title'] = self.exf(response.css('h1 > span::text'))

        data['summary'] = self.exf(response.css('div[data-testid="interests"]+p > span::text'))
        data['interests'] = self.ex(
            response.css('div[data-testid="interests"] > div[class*="scroll"] > a > span::text'))

        data['rating'] = self.exf(
            response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"] > span::text'))
        r = response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"] > span::text')
        data['ratingCount'] = r.extract()[2] if len(r) > 2 else None
        data['duration'] = self.exf(response.css('ul[role="presentation"] > li::text'))
        r = response.css('ul[role="presentation"] > li::text')
        data['releaseDate'] = r.extract()[1] if len(r) > 1 else None
        r = response.css('ul[role="presentation"] > li::text')
        t = self.ex(r)[1].split(' ') if len(r) > 1 else None
        data['year'] = t[2] if t is not None and len(t) > 2 else None
        data['vote'] = self.exf(
            response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"]+div+div::text'))

        # main crew

        data['director'] = self.exf(
            response.css('li[data-testid="title-pc-principal-credit"] > div > ul > li > a::text'))
        t = response.css('li[data-testid="title-pc-principal-credit"] > div')
        data['writers'] = self.ex(t[1].css('ul > li > a::text')) if len(t) > 1 else None
        t = response.css('li[data-testid="title-pc-principal-credit"] > div')
        data['stars'] = self.ex(t[2].css('ul > li > a::text')) if len(t) > 2 else None

        # actors

        actors = self.ex(
            response.css('div[data-testid="shoveler-items-container"][class*="wraps"] > div > div > a::text'))

        actorsPics = response.css('div[data-testid="shoveler-items-container"][class*="wraps"] > div')
        actorsChs = response.css('div[data-testid="shoveler-items-container"][class*="wraps"] > div > div+div > div')

        if actors is not None:
            t = [None] * len(actors)
            for i, actor in enumerate(actors):
                t[i] = {'actor': actor, 'picUrl': None}
                pic = self.ex(actorsPics[i].css('img::attr(src)'))
                if pic is not None: t[i]['picUrl'] = pic
                chs = self.ex(actorsChs[i].css('span::text')) if len(actorsChs) > i else None
                t[i]['characters'] = chs
            data['actors'] = t
        else:
            data['actors'] = None

        # anecdotes

        t = self.ex(response.css('section[data-testid="DidYouKnow"] div.ipc-html-content-inner-div *::text'))
        if t is not None:
            t = ''.join(t).split('.')
            data['anecdotes'] = '.'.join(t)
        else:
            data['anecdotes'] = None

        # pics

        data['minPicUrl'] = self.atr(response.css('div[data-testid="hero-media__poster"] > div > img'), 'src')
        data['minPicWidth'] = self.atr(response.css('div[data-testid="hero-media__poster"] > div > img'), 'width')
        data['minPicAlt'] = self.atr(response.css('div[data-testid="hero-media__poster"] > div > img'), 'alt')
        a = self.atr(response.css('div[data-testid="hero-media__poster"] > div > img'), 'srcset')
        data['picsUrls'] = list(filter(self.isUrl, a.split(' '))) if a is not None else None
        if data['picsUrls'] is not None:
            picdef = data['picsUrls'][0]
            t = picdef.split('.')
            t.pop()
            data['picFullUrl'] = '.'.join(t).split(',')[0]
        else:
            data['picFullUrl'] = None
        a = self.atr(response.css('div[data-testid="hero-media__poster"] > div > img'), 'sizes')
        data['picsSizes'] = a.split(',') if a is not None else None

        return data
