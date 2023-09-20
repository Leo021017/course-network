# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itemadapter import ItemAdapter
import pymysql
from .settings import MYSQL_DBNAME
from .settings import MYSQL_HOST
from .settings import MYSQL_PASSWD
from .settings import MYSQL_USER
from .items import DamusItem
from .items import SearchItem


class DamusPipeline(object):
    def __init__(self):
    # 连接数据库
        self.connect1 = pymysql.connect(
        host='localhost',
        db='damus',
        user='root',
        passwd='HYC20021017.2.2',
        port=3306,
        charset='utf8mb4',
        use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor1 = self.connect1.cursor();
    
        self.connect2 = pymysql.connect(
        host='localhost',
        db='damus',
        user='root',
        passwd='HYC20021017.2.2',
        port=3306,
        charset='utf8mb4',
        use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor2 = self.connect2.cursor();

    # def close_spider(self, spider):
    #     if len(self.data) > 0:
    #         self._write_to_db()
    #     self.conn.close

    def process_item(self, item, spider):
        # try:
        if isinstance(item, DamusItem):
            print("id数目是{}\n".format(len(item['id'])))
            for i in range(0, len(item['post_list'])):
                if i >= len(item['like_list']):
                    like = '1'
                else:
                    like = item['like_list'][i]
                if i >= len(item['time_list']):
                    time = '23年5月25日'
                else:
                    time = item['time_list'][i]
                self.cursor1.execute(
                    """insert into posts(`post_list`, `like_list`, `time_list`)
                    value (%s, %s, %s)""",
                    (str(item['post_list'][i]),
                        like,
                        time))

            # fp = open('./damus.txt', 'a', encoding='utf-8')
            # post = item['post_list']
            # for po in post:
            #     if po is not None:
            #         fp.write(str(po))
            fp = open('./damus_user.txt', 'a', encoding='utf-8')
            for j in range(0, len(item['id'])):
                print("j={}".format(j))
                # id = item['id'][j]
                print("len(resume)={}".format(len(item['resume'])))
                
                if j >=len(item['resume']):
                    resume = 'resume does not exist'
                else:
                    resume = item['resume'][j]
                if j >=len(item['background']):
                    background = 'background does not exist'
                else:
                    b = 'D:/Python/workspace_pycharm/network/damus/damus/background/' + 'bkg-{}.png'.format(id)
                    background = b
                if j >=len(item['profile']):
                    profile = 'profile does not exist'
                else:
                    p = 'D:/Python/workspace_pycharm/network/damus/damus/profile/' + 'profile-{}.png'.format(id)
                    profile = p
                if j >=len(item['name']):
                    name = 'name does not exist'
                else:
                    name = item['name'][j]
                self.cursor2.execute(
                    """insert into user(`id`, `resume`, `background`, `name`, `profile`)
                    value (%s, %s, %s, %s, %s)""",
                    (str(item['id'][j]),
                        resume,
                        background,
                        name,
                        profile))
                fp.write("确实进入for循环了！")
        
                
            post = item['resume']
            for po in post:
                fp.write(str(po) + "\n")
            # fp.write(str(item['id']))
            


            # 提交sql语句
            self.connect1.commit()
            self.connect2.commit()
            

            # except Exception as error:
            #     # 出现错误时打印错误日志
            #     print("error")
            return item

class SearchPipeline(object):
    def __init__(self):
    # 连接数据库
        self.connect = pymysql.connect(
        host='localhost',
        db='damus',
        user='root',
        passwd='HYC20021017.2.2',
        port=3306,
        charset='utf8mb4',
        use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    # def close_spider(self, spider):
    #     if len(self.data) > 0:
    #         self._write_to_db()
    #     self.conn.close

    def process_item(self, item, spider):
        # try:
        if isinstance(item, SearchItem):
            print("keyword={}".format(item['keyword']))
            for i in range(0, len(item['post_list'])):
                if str(item['post_list'][i]) == " ":
                    post = "Announcing version 0.3 of Bitcoin, the P2P cryptocurrency! Bitcoin is a digital currency using cryptography and a distributed network to replace the need for a trusted central server"
                else:
                    post = str(item['post_list'][i])
                if i >= len(item['like_list']):
                    like = '1'
                else:
                    like = item['like_list'][i]
                if i >= len(item['time_list']):
                    time = '23年5月25日'
                else:
                    time = item['time_list'][i]
                self.cursor.execute(
                    """insert into search(`post_list`, `like_list`, `time_list`, `keyword`)
                    value (%s, %s, %s, %s)""",
                    (post,
                        like,
                        time,
                        str(item['keyword'][0])))
            
            # 提交sql语句
            self.connect.commit()
            

            # except Exception as error:
            #     # 出现错误时打印错误日志
            #     print("error")
            return item


