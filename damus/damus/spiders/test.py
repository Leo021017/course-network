'''
Author: Leo
Date: 2023-05-31 15:42:56
LastEditTime: 2023-06-03 16:41:57
FilePath: \network\damus\damus\spiders\test.py
Description: Leo的一些没用的代码
'''
import scrapy
from damus.items import SearchItem


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["snort.social/search"]
    start_urls = ["https://snort.social/search/"]

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            "damus.middlewares.SearchDownloaderMiddleware": 544,
        },
        'ITEM_PIPELINES': {
            "damus.pipelines.SearchPipeline": 300,
        }
    }

    def parse(self, response):
        url = response.url
        post_list = response.xpath(
            '//*[@id="root"]/div[@class="page"]/div[1]//div[@class="body"]//div[@class="text"]/text()').extract()
        time_list = response.xpath(
            '//*[@id="root"]/div/div[1]//div[@class="header flex"]/div/time/text()').extract()
        like_list = response.xpath(
            '//*[@id="root"]/div/div[1]//div[@class="footer"]/div/div[2]/div/text()').extract()
        keyword = response.xpath('//*[@id="root"]/div/div[1]/div[1]/input/@value').extract()
        yield SearchItem(post_list=post_list, time_list=time_list, like_list=like_list, keyword=keyword)
