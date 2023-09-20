# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
import os.path
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import re

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class DamusSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class DamusDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def __init__(self):
        options = Options()  # 实例化Option对象
        options.page_load_strategy = 'none'
        options.add_argument("--headless")
        # self.driver = webdriver.Ie(options=options,
        #                            executable_path=r'D:\MyDownloads\edgedriver_win64\msedgedriver.exe')
        self.driver = webdriver.Chrome(options=options, executable_path=r'D:/MyDownloads/chromedriver_win32/chromedriver.exe')
        # print(edge_options.to_capabilities())
        # self.url = 'https://snort.social/p/npub1s277u5rww60te98w9umz6p7pjcxuus96cegdsf4y978qcqvu8jtq88dsym'

    def __del__(self):
        self.driver.close()

    def scroll(self, driver):
        driver.execute_script(""" 
            (function () { 
                var y = document.body.scrollTop; 
                var step = 150; 
                window.scroll(0, y); 
                function f() { 
                    if (y < document.body.scrollHeight) { 
                        y += step; 
                        window.scroll(0, y); 
                        setTimeout(f, 70); 
                    }
                    else { 
                        window.scroll(0, y); 
                        document.title += "scroll-done"; 
                    } 
                } 
                setTimeout(f, 1000); 
            })(); 
            """)

    def process_request(self, request, spider):
        """
        用selenium抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        try:
            # self.driver.get("https://snort.social/login")
            # self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[1]/input')[0].send_keys(
            #     "npub12ftld459xqw7s7fqnxstzu7r74l5yagxztwcwmaqj4d24jgpj2csee3mx0")
            # self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/button[1]')[0].click()
            # sleep(5)
            self.driver.get(request.url)
            print("现在爬取的url是"+request.url+"\n")
            sleep(10)
            # print("开始滚动")
            self.scroll(self.driver)
            sleep(20)
            # print("滚动结束")
            wait_time = 180
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]')))
            name = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/h2')
            resume = []
            background = []
            profile = []
            try:
                resume = self.driver.find_elements_by_xpath('//*[@id="root"]/div[@class="page"]/div[1]/div/div[2]/div[3]/div/div')
                background = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/img')
                profile = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div')
            except NoSuchElementException as e:
                print(e)
                pass
            time_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div/div[3]//div[@class="header flex"]/div/time')
            like_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div/div[3]//div[@class="footer"]/div/div[2]/div')
            post_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]')
            for time in time_list:
                print("这是时间：" + time.get_attribute('datetime'))
            
            for like in like_list:
                print("这是点赞：" + like.text)
            
            for post in post_list:
                print(post.text)
                print("----------------------------------------------------------------")
            
            if len(background) != 0:
                print("这是背景：" + background[0].get_attribute('src'))
            
            if len(resume) != 0:
                print("这是简介：" + resume[0].text)
            
            if len(name) != 0:
                print("这是姓名：" + name[0].text)

            userid = request.url.split("/p/")[1]
            if len(background) != 0:
                src = background[0].get_attribute('src')
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
                }
                r = requests.get(url=src, headers=headers)
                if not os.path.exists('./background'):
                    os.mkdir('./background')
                with open("background/bkg-{}.png".format(userid), "wb") as f:  # wb是写二进制
                    f.write(r.content)

            if len(profile) != 0:
                str = profile[0].get_attribute('style')
                pattern = r"url\((.*?)\)"
                match = re.search(pattern, str)

                if match:
                    src = match.group(1)
                    print(src)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
                }
                r = requests.get(url=src, headers=headers)
                if not os.path.exists('./profile'):
                    os.mkdir('./profile')
                with open("profile/profile-{}.png".format(userid), "wb") as f:  # wb是写二进制
                    f.write(r.content)
            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException as e:
            print(e)
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class SearchDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def __init__(self):
        options = Options()  # 实例化Option对象
        options.page_load_strategy = 'none'
        # options.add_argument("--headless")
        # self.driver = webdriver.Ie(options=options,
        #                            executable_path=r'D:\MyDownloads\edgedriver_win64\msedgedriver.exe')
        self.driver = webdriver.Chrome(options=options, executable_path=r'D:/MyDownloads/chromedriver_win32/chromedriver.exe')

    def __del__(self):
        self.driver.close()

    def scroll(self, driver):
        driver.execute_script(""" 
            (function () { 
                var y = document.body.scrollTop; 
                var step = 150; 
                window.scroll(0, y); 
                function f() { 
                    if (y < document.body.scrollHeight) { 
                        y += step; 
                        window.scroll(0, y); 
                        setTimeout(f, 70); 
                    }
                    else { 
                        window.scroll(0, y); 
                        document.title += "scroll-done"; 
                    } 
                } 
                setTimeout(f, 1000); 
            })(); 
            """)

    def process_request(self, request, spider):
        """
        用selenium抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        try:
            self.driver.get("https://snort.social/login")
            wait_time = 180
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="root"]/div/div[1]/div[1]/div/div[1]/input')))
            self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[1]/input')[0].send_keys(
                "npub1937vv2nf06360qn9y8el6d8sevnndy7tuh5nzre4gj05xc32tnwqauhaj6")
            self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/button[1]')[0].click()
            sleep(5)
            print("登录成功！")
            with open('D:/Python/workspace_pycharm/network/damus/damus/spiders/word.txt', 'r', encoding='utf-8') as f:
                my_string = f.read()
            my_url = request.url + my_string
            print(my_url)
            self.driver.get(my_url)
            sleep(20)
            wait_time = 180
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="root"]/div/header/div[2]/div/div[2]')))
            self.driver.find_elements_by_xpath('//*[@id="root"]/div/header/div[2]/div/div[2]')[0].click()
            wait_time = 180
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="root"]/div[@class="page"]/div[1]//div[@class="body"]//div[@class="text"]')))
            self.scroll(self.driver)
            sleep(50)
            time_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div/div[1]//div[@class="header flex"]/div/time')
            like_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div/div[1]//div[@class="footer"]/div/div[2]/div')
            post_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div[@class="page"]/div[1]//div[@class="body"]//div[@class="text"]')
            # for time in time_list:
            #     print("这是时间：" + time.get_attribute('datetime'))

            # for like in like_list:
            #     print("这是点赞：" + like.text)

            # for post in post_list:
            #     print(post.text)
            #     print("----------------------------------------------------------------")
            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException as e:
            print(e)
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

