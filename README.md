# 面向Damus的特定主题信息采集爬虫
## 1. 项目摘要
目总体框架上使用scrapy结合selenium的构造来完成爬虫部分，scrapy是一个爬虫框架，selenium实现自动化爬虫，该结合可以提供更全面、准确且高效的去中心化社区帖子爬取解决方案。
## 2. 环境配置

### 2.1 Python环境配置

在项目目录下运行`pip install -r requirements.txt`

### 2.2 前端js环境配置

本项目前端使用node.js 14.21.3版本，如安装nvm，可直接运行`nvm use 14.21.3`

## 3. 运行

### 3.1 用户文本爬取

在`root/damus/damus`目录下运行`scrapy crawl snort`

### 3.2 关键词爬取

在根目录下运行`python management.py runserver`，浏览器打开`http://127.0.0.1:8000/search`即可
