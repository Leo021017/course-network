from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver import ActionChains


class Spider(object):
    def __init__(self):
        edge_options = Options()  # 实例化Option对象
        edge_options.page_load_strategy = 'none'
        self.driver = webdriver.Ie(options=edge_options,
                                   executable_path=r'D:\MyDownloads\edgedriver_win64\msedgedriver.exe')
        # print(edge_options.to_capabilities())
        self.url = 'https://snort.social/p/npub1cmmswlckn82se7f2jeftl6ll4szlc6zzh8hrjyyfm9vm3t2afr7svqlr6f'
        self.post_list = []

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

    def get_post(self, driver):
        self.driver.get(self.url)
        # driver.maximize_window()
        sleep(10)
        print("开始scrolling")
        self.scroll(driver)
        sleep(60)
        print("结束scrolling")
        wait_time = 180
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]/div[@class="note-invoice"]')))
        self.post_list = driver.find_elements_by_xpath('//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]/div[@class="note-invoice"]')
        print(len(self.post_list))
        img_num = len(self.post_list)
        action = ActionChains(self.driver)
        for i in range(0, img_num):
            post = self.post_list[0]
            driver.execute_script("arguments[0].scrollIntoView();", post)
            sleep(5)
            action.click(post)
            action.perform()
            WebDriverWait(driver, 180).until(
                EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]//img'))
            )
            img = driver.find_elements_by_xpath('//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]//img')
            print(img[0].get_attribute('src'))
            driver.refresh()
            sleep(10)
            WebDriverWait(driver, 180).until(
                EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]/div[@class="note-invoice"]'))
            )
            self.post_list = driver.find_elements_by_xpath('//*[@id="root"]/div[@class="page"]/div[3]//div[@class="body"]//div[@class="text"]/div[@class="note-invoice"]')
            print(len(self.post_list))
            # WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH,
            #                                 '//*[@id="root"]/div[@class="page"]/div[3]/div[@class="note card  "]/div['
            #                                 '2]//div[@class="text"]/div[@class="note-invoice"]'))
            # )
            # self.post_list = driver.find_elements_by_xpath(
            #     '//*[@id="root"]/div[@class="page"]/div[3]/div[@class="note card  "]/div[2]//div[@class="text"]/div['
            #     '@class="note-invoice"]')

            # for post in post_list:
        #     driver.execute_script("arguments[0].scrollIntoView();", post)
        #     sleep(5)
        #     action.click(post)
        #     action.perform()
        # img_list = driver.find_elements_by_xpath('//*[@id="root"]/div[@class="page"]/div[3]/div[@class="note card  "]/div[2]//div[@class="text"]//img')
        # for img in img_list:
        #     print(img.get_attribute('src'))

    def run(self):
        self.get_post(self.driver)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
