from scrapy import Spider
from scrapy.selector import Selector
import os, sys
sys.path.append(os.path.join(sys.path[-1],'jokes'))
sys.path.append('/home/oliver/Projects/jokes/jokes/')
from items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["funny2.com"]
    start_urls = [
        "'http://funny2.com/jokes.htm'",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        print(questions)
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item