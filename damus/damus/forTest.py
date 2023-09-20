from time import sleep
import os.path

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


class Spider(object):
    def __init__(self):
        edge_options = Options()  # 实例化Option对象
        edge_options.page_load_strategy = 'normal'
        self.driver = webdriver.Ie(options=edge_options,
                                   executable_path=r'D:\MyDownloads\edgedriver_win64\msedgedriver.exe')
        # print(edge_options.to_capabilities())
        self.url = 'https://snort.social/p/npub1s277u5rww60te98w9umz6p7pjcxuus96cegdsf4y978qcqvu8jtq88dsym'
        self.a_list = []
        self.user_url_list = []

    def scroll(self, driver):
        driver.execute_script(""" 
            (function () { 
                var y = document.body.scrollTop; 
                var step = 140; 
                window.scroll(0, y); 
                function f() { 
                    if (y < 4000000) { 
                        y += step; 
                        window.scroll(0, y); 
                        setTimeout(f, 50); 
                    }
                    else { 
                        window.scroll(0, y); 
                        document.title += "scroll-done"; 
                    } 
                } 
                setTimeout(f, 1000); 
            })(); 
            """)

    def get_user(self):
        try:
            self.driver.get(self.url)
            height = 1
            while height < 4000000:
                height = self.driver.execute_script(
                    "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
                print(height)
            # sleep(90)
            self.scroll(self.driver)
            print("scrolling 开始")
            sleep(2000)
            print("scrolling 结束")
            wait_time = 30
            print("开始等待元素加载")
            # wait = WebDriverWait(self.driver, wait_time)
            # wait.until(
            #     EC.presence_of_element_located(
            #         (By.XPATH,
            #          '//*[@id="root"]/div[@class="page"]/div[2]/div[@class="note card  "]/div[1]/a/@href')))
            self.a_list = self.driver.find_elements_by_xpath(
                '//*[@id="root"]/div[@class="page"]/div[2]/div[@class="note card  "]/div[1]/a')
            # user_url_list = self.user_list.__getattribute__('href')
            # action = ActionChains(self.driver)

        except TimeoutException as e:
            print(e)

        print("开始爬取用户url：")
        url_num = 0
        fp = open("./user_url.txt", 'w', encoding='utf-8')
        for a in self.a_list:
            # action.click(user)
            # action.perform()

            # all_handlers = self.driver.window_handles
            # self.driver.switch_to.window(all_handlers[0])
            user_url = a.get_attribute('href')
            print(user_url)
            fp.write(user_url + "\n")
            url_num = url_num + 1
            # self.get_post(self.driver)
        print(url_num)

    def get_post(self, driver):
        # sleep(30)
        self.scroll(driver)
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        sleep(60)

        wait_time = 180
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="root"]/div[@class="page"]/div[3]/div[@class="note card  "]/div[2]//div[@class="text"]')))
        post_list = driver.find_elements_by_xpath(
            '//*[@id="root"]/div[@class="page"]/div[3]/div[@class="note card  "]/div[2]//div[@class="text"]')
        for post in post_list:
            print(post.text)
            print("----------------------------------------------------------------")
        # driver.execute_script("window.scrollTo(0,1000)")
        # print(driver.page_source)
        driver.back()

    def test(self):
        try:
            self.driver.get("https://snort.social/login")
            self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[1]/input')[0].send_keys(
                "npub12ftld459xqw7s7fqnxstzu7r74l5yagxztwcwmaqj4d24jgpj2csee3mx0")
            self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/button[1]')[0].click()
            sleep(5)
            self.driver.get(self.url)
            sleep(20)
            self.scroll(self.driver)
            sleep(60)
            print("开始爬取！")
            wait_time = 180
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]')))
            name = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/h2')
            resume = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[3]/div/div/p')
            background = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/img')
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

            userid = self.url.split("/p/")[1]
            src = background[0].get_attribute('src')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
            }
            r = requests.get(url=src, headers=headers)
            if not os.path.exists('./background'):
                os.mkdir('./background')
            with open("background/{}.png".format(userid), "wb") as f:  # wb是写二进制
                f.write(r.content)
        except TimeoutException as e:
            print(e)

    def run(self):
        self.test()
        self.driver.quit()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
    # spider.test()
