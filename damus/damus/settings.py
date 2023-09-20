# Scrapy settings for damus project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "damus"

SPIDER_MODULES = ["damus.spiders"]
NEWSPIDER_MODULE = "damus.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "damus (+http://www.yourdomain.com)"

DEFAULT_REQUEST_HEADERS = {
    # 'cookie': '__cflb=02DiuGWuKaNx9C8JTR1MoTVnLZG8N6FSLjpuVbNMhDj5T',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
}

# 开启爬虫中间件
SPIDER_MIDDLEWARES = {
    "damus.middlewares.DamusSpiderMiddleware": 543,
}
# 开启下载器中间件
DOWNLOADER_MIDDLEWARES = {
    "damus.middlewares.DamusDownloaderMiddleware": 543,
}

# 项目管道，300为优先级，越低越爬取的优先度越高
ITEM_PIPELINES = {
    "damus.pipelines.DamusPipeline": 300,
}

ROBOTSTXT_OBEY = False
# LOG_LEVEL = "WARNING"
LOG_LEVEL = 'CRITICAL'

# 下载延迟时间，单位是秒，控制爬虫爬取的频率，根据你的项目调整，不要太快也不要太慢，默认是3秒，即爬一个停3秒，设置为1秒性价比较高
# 如果要爬取的文件较多，写零点几秒也行
DOWNLOAD_DELAY = 1  # 默认是3
RANDOMIZE_DOWNLOAD_DELAY = True  # 随机时延（自己加）

# 是否保存COOKIES，默认关闭，开机可以记录爬取过程中的COOKIE，非常好用的一个参数
COOKIES_ENABLED = False  # 关闭COOKIES，防止服务器追踪爬虫轨迹

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'damus'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'HYC20021017.2.2'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 最大并发数
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
