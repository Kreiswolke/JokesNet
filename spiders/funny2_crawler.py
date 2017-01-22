# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os, sys
sys.path.append(os.path.join(sys.path[-1],'jokes'))
sys.path.append('/home/oliver/Projects/jokes/jokes/')
from items import JokesItem


class JokesCrawlerSpider(CrawlSpider):
    name = 'funny2'
    allowed_domains = ['funny2.com']
    start_urls = ['http://funny2.com/jokes.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://funny2.com/jokes[a-z]+\.htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        jokes =  response.xpath('.//*[@id="divMain"]/div[1]/text()[normalize-space()]')
        print('LENGTH', len(jokes))
        #  print(jokes)
        for joke in jokes:
            #print('K', joke)
            item = JokesItem()
            item['joke'] = joke.extract().strip().replace("\\", "")
          #  item['url'] = joke.xpath('.//div/a/@href').extract()[0]
          #  item['topic'] = [a.strip('/') for a in joke.xpath('.//span/a/@href').extract()]
            yield item
