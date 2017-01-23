# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os, sys
sys.path.append(os.path.join(sys.path[-1],'jokes'))
sys.path.append('/home/oliver/Projects/jokes/jokes/')
from items import JokesItem


class JokesCrawlerSpider(CrawlSpider):
    name = 'jokesoftheday'
    allowed_domains = ['jokesoftheday.net']
    start_urls = ['http://jokesoftheday.net/tag/short-jokes/0']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.jokesoftheday.net/tag/short-jokes/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        jokes = response.xpath('//*/div[@class="jokeContent"]')
        for joke in jokes:
            item = JokesItem()
            text = joke.xpath(".//h2/../text()[normalize-space()] | .//h2/../p//text()").extract()
            neg_list = ['Submitted', 'Edited']
            if len(text) > 1:

                # Get rid of redundent title in rare cases
                if text[0].split()[0:2] == text[1].split()[0:2]:
                    text = text[1:]
                text = [a.strip().strip(u'\u201c\u201d') for a in text if (not any(w in a.split() for w in neg_list))]
            else:
                text = [a.strip().strip(u'\u201c\u201d') for a in text if not any(w in a.split() for w in neg_list)]

            if len(text) > 0:
                item['joke'] = ' '.join(text)
                print( ' '.join(text))
                yield item
            else:
                pass
