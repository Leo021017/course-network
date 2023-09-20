'''
Author: Leo
Date: 2023-05-06 20:23:57
LastEditTime: 2023-06-03 15:59:11
FilePath: \network\damus\damus\spiders\snort.py
Description: Leo的一些没用的代码
'''
import scrapy
from damus.items import DamusItem


class SnortSpider(scrapy.Spider):
    name = "snort"
    allowed_domains = ["snort.social"]
    start_urls = []

    with open("D:/Python/workspace_pycharm/network/damus/damus/test.txt", "r") as f:
        for line in f:
            url = "https://snort.social" + line.strip()
            start_urls.append(url)

    # start_urls = ["https://snort.social/p/npub107jk7htfv243u0x5ynn43scq9wrxtaasmrwwa8lfu2ydwag6cx2quqncxg"]

    # num = 1

    def start_requests(self):
        print("一共{}\n".format(len(self.start_urls)))
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url
        print("现在在爬取的url: %d", url)
        post_list = response.xpath('//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]/text()').extract()
        time_list = response.xpath(
            '//*[@id="root"]/div/div[3]//div[@class="header flex"]/div/time/text()').extract()
        like_list = response.xpath(
            '//*[@id="root"]/div/div[3]//div[@class="footer"]/div/div[2]/div/text()').extract()
        name = response.xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/h2/text()').extract()
        resume = response.xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[3]/div/div/text()').extract()
        background = response.xpath('//*[@id="root"]/div/div[1]/img/@src').extract()
        profile = response.xpath('//*[@id="root"]/div/div[1]/div/div[1]/div').extract()
        id = []
        temp = url.split("/p/")[1]
        id.append(temp)

        yield DamusItem(post_list=post_list, name=name, background=background,
                        time_list=time_list, like_list=like_list, resume=resume, profile=profile, id=id)
        
    def closed(self, reason):
        self.logger.info('Spider closed: %s' % reason)
