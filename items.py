# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class JokesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    joke = Field()
    url = Field()
    topic = Field()
    



class StackItem(Item):
    title = Field()
    url = Field()