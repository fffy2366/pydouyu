#/!bin/evn python
# -*-coding:utf8-*-
import redis
import uuid

'''
#投票
一个主题四个单选项
通过弹幕关键字累计票数
限制：每个用户只能投一票


SET page_view 20
INCR page_view
GET page_view
'''


class Toupiao:
    topic = None
    option = None
    r = None

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0, password='db2016')

    def topic(self, topic):
        self.topic = topic
        _uuid = uuid.uuid1()
        self.r.hset("topic", _uuid, self.topic)
        return _uuid

    def options(self, toppic_id, ops):
        for o in ops:
            _uuid = uuid.uuid1()
            self.option = ops
            self.r.hset("options:" + toppic_id, _uuid, o)

    def tou(self, msg):
        # 弹幕有投1,投2，投3，投4关键字
        if '投1' in msg:
            self.r.incr('')
        pass


t = Toupiao

tid = t.topic("")
