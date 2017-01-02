#!bin/evn python
# -*-coding:utf8-*-
'''
#[《斗鱼弹幕服务器第三方接入协议v1.4.1》发布信息](http://dev-bbs.douyutv.com/forum.php?mod=viewthread&tid=115&extra=page%3D1)
[python](https://github.com/yingnansong/pydouyu)
[nodejs](https://github.com/yingnansong/douyujs)
window下cmd乱码解决：chcp 65001
[windows cmd命令显示UTF8设置](http://www.liangcuntu.com/windows_cmd_utf8)
https://www.github.com/fffy2366/pydouyu

[Redis 命令参考](http://redisdoc.com/)

ZRANGE douyuchatset 0 -1 WITHSCORES
#递减
ZREVRANGE douyuchatset 0 -1 WITHSCORES
hget douyuchathash b8116d914b5b48ce7700010000000000
'''
from douyu.chat.room import ChatRoom
import redis
from os import system
import datetime
import time

r = redis.Redis(host='localhost', port=6379, db=0, password='db2016')


def on_chat_message(msg):
    # print msg.to_text()
    #el@=/uid@=98050310/nn@=liangcuntu/cid@=b8116d914b5b48ce8cec000000000000/level@=1/gid@=-9999/rg@=4/rid@=593076/txt@=测试/type@=chatmsg/ic@=avanew@Sface@S201612@S28@S08@Sed9e85a68b5fa100dc5ece9902ca9c93/ct@=2/
    # o = '[%s]:%s' % (msg.attr('nn'), msg.attr('txt'))
    s = "{0} :{1}".format(msg.attr('nn'), msg.attr('txt'))

    system('say '+msg.attr('txt'))
    print s

    # 按日期保存入redis
    # r.publish('douyu', s)
    # r.set('douyu',s)
    cid = msg.attr('cid')
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now = int(time.time())

    r.zadd("douyuchatset",cid,now)

    v = {"nn":msg.attr('nn'),"txt":msg.attr('txt'),"created_at":created_at}
    r.hset("douyuchathash",cid,v)

def run():
    # 彡彡九
    room = ChatRoom('485503')
    # fffy2366
    room = ChatRoom('593076')

    room.on('chatmsg', on_chat_message)
    room.knock()


if __name__ == '__main__':
    run()
