# -*- coding: UTF-8 -*-
'''
@Project ：damus 
@File    ：get_user.py
@Author  ：Leo
@Date    ：2023/5/16 20:10 
'''

from lxml import etree

# 打开本地HTML文件并读取内容
with open('crl.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 使用etree库将HTML解析为Element对象
html_tree = etree.HTML(html_content)

# 可以通过XPath表达式查找元素
title_element = html_tree.xpath('//*[@id="root"]/div[@class="page"]/div[2]/div[@class="note card  "]/div[1]/a[@class="pfp"]/@href')

# 打印标题文本
print(title_element)

fp = open("./a.txt", 'w', encoding='utf-8')
for a in title_element:
    # action.click(user)
    # action.perform()

    # all_handlers = self.driver.window_handles
    # self.driver.switch_to.window(all_handlers[0])
    fp.write(a + "\n")
    # self.get_post(self.driver)
