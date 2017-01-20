from scrapy import Spider
from scrapy.selector import Selector
import os, sys
sys.path.append(os.path.join(sys.path[-1],'jokes'))
from items import JokesItem

class JokesSpider(Spider):
    name = "onelinefun"
    print(name)
    allowed_domains =["onelinefun.com"]
    start_urls = [
        "http://onelinefun.com/",
    ]

    def parse(self, response):
        jokes = Selector(response).xpath('//div[@class="oneliner"]')
        print('LENGTH',len(jokes))
      #  print(jokes)
        for joke in jokes:
            #print('K', joke)
            item = JokesItem()
            item['joke'] = joke.xpath('.//p/text()').extract()
            item['url'] = joke.xpath('.//div/a/@href').extract()[0]
            item['topic'] = [a.strip('/') for a in joke.xpath('.//span/a/@href').extract()]
            yield item

