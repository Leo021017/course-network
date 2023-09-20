# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itemadapter import ItemAdapter
import pymysql


class DamusPipeline:

    def __init__(self):
        # 数据库连接，根据个人情况修改host等信息
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='HYC20021017.2.2',
                                    database='damus',
                                    charset='utf8mb4')
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        if len(self.data) > 0:
            self._write_to_db()
        self.conn.close

    def process_item(self, item, spider):
        # 从item中获取数据，包括帖子点赞数和评论
        post_list = item.get('post_list', '')
        like_list = item.get('like_list', '')
        time_list = item.get('time_list', '')
        # comment = item.get('comment', '')
        # name = item.get('name', '')
        print(
            "------------------------------------------------------------------------------------------------------------------")
        # resume = item.get('resume', '')
        # background = item.get('background', '')
        # 把数据放到容器中，以便进行批处理
        self.data.append((post_list, like_list, time_list))
        # 每100条存一次
        if len(self.data) == 100:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self, post_list, like_list, time_list):
        self.cursor.executemany(
            # insert into后面跟数据库table的名字，我的是posts，括号内是表中具体每个列的值
            'insert into posts(post,like,time) values (%s,%s,%s)', self.data
            # 'insert into posts(post,like,time) values (1,2,3)'
        )
        self.conn.commit()
