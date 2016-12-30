#!bin/evn python
# -*-coding:utf8-*-
'''
#[《斗鱼弹幕服务器第三方接入协议v1.4.1》发布信息](http://dev-bbs.douyutv.com/forum.php?mod=viewthread&tid=115&extra=page%3D1)
[python](https://github.com/yingnansong/pydouyu)
[nodejs](https://github.com/yingnansong/douyujs)
window下cmd乱码解决：chcp 65001
[windows cmd命令显示UTF8设置](http://www.liangcuntu.com/windows_cmd_utf8)
'''
from douyu.chat.room import ChatRoom
import redis
r = redis.Redis(host='localhost', port=6379, db=0,password='db2016')

def on_chat_message(msg):
	#o = '[%s]:%s' % (msg.attr('nn'), msg.attr('txt'))
	s = "{0} :{1}".format(msg.attr('nn'),msg.attr('txt'))
	print s
    # 保存入redis
	#r.publish('douyu', s)
	r.set('douyu',s)


def run():
	#彡彡九
    room = ChatRoom('485503')
    #fffy2366
    room = ChatRoom('593076')

    room.on('chatmsg', on_chat_message)
    room.knock()

if __name__ == '__main__':
     run()