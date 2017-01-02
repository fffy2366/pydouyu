#!bin/evn python
# -*-coding:utf8-*-

import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, password='db2016')

# 从sortset里按时间降序取出弹幕id
rid = "593076"
# rid = "485503"
page = 1
pageSize = 20
start = (page-1)*pageSize
end = start+pageSize-1
cids = r.zrevrange("douyuenterset:"+rid,start,end)

for cid in cids:
    # 从hash表取出弹幕
    msg = r.hget("douyuenterhash:"+rid,cid)
    # msg = json.loads(msg)
    msg = eval(msg)
    keys =  msg.keys()

    created_at = "["+msg['created_at']+"]" if 'created_at' in keys else ""

    print "欢迎{0}来到直播间------{1}".format(msg['nn'],created_at)