# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import sys
sys.path.append('/home/oliver/Projects/jokes/jokes/')
from items import JokesItem


class JokesCrawlerSpider(CrawlSpider):
    name = 'jokes_crawler'
    allowed_domains = ['onelinefun.com']
    start_urls = ['http://onelinefun.com/1/']

    rules = (
        Rule(LinkExtractor(allow=r'http://onelinefun.com/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        jokes = response.xpath('//div[@class="oneliner"]')
        print('LENGTH', len(jokes))
        #  print(jokes)
        for joke in jokes:
           # print('K', joke)
            item = JokesItem()
            item['joke'] = joke.xpath('.//p/text()').extract()
            item['url'] = joke.xpath('.//div/a/@href').extract()[0]
            item['topic'] = [a.strip('/') for a in joke.xpath('.//span/a/@href').extract()]
            yield item
