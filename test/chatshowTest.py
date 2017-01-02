#!bin/evn python
# -*-coding:utf8-*-

import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, password='db2016')

# 从sortset里按时间降序取出弹幕
page = 1
pageSize = 20
start = (page-1)*pageSize
end = start+pageSize-1
cids = r.zrevrange("douyuchatset",start,end)

for cid in cids:
    # print cid
    msg = r.hget("douyuchathash",cid)
    # msg = json.loads(msg)
    msg = eval(msg)
    keys =  msg.keys()
    # print keys
    # if 'created_at' in keys:
    #     print msg['created_at']
    created_at = "["+msg['created_at']+"]" if 'created_at' in keys else ""

    print "{0}:{1} {2}".format(msg['nn'],msg['txt'],created_at)