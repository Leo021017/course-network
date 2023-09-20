'''
Author: Leo
Date: 2023-05-06 20:23:24
LastEditTime: 2023-06-03 16:14:06
FilePath: \network\damus\damus\items.py
Description: Leo的一些没用的代码
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DamusItem(scrapy.Item):
    # define the fields for your item here like:
    post_list = scrapy.Field()
    like_list = scrapy.Field()
    time_list = scrapy.Field()
    name = scrapy.Field()
    resume = scrapy.Field()
    background = scrapy.Field()
    id = scrapy.Field()
    profile = scrapy.Field()



class SearchItem(scrapy.Item):
    post_list = scrapy.Field()
    like_list = scrapy.Field()
    time_list = scrapy.Field()
    keyword = scrapy.Field()
