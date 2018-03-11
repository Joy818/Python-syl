# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    summary = scrapy.Field()
    score = scrapy.Field()