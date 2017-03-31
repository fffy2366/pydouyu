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
cids = r.zrevrange("douyuchatset:"+rid,start,end)
count=1
for cid in cids:
    # print cid
    # 从hash表取出弹幕
    msg = r.hget("douyuchathash:"+rid,cid)
    if not msg:
        continue
    # msg = json.loads(msg)
    msg = eval(msg)
    keys =  msg.keys()
    # if(count==1):
    #     r.hdel("douyuchathash:"+rid,cid)
    created_at = "["+msg['created_at']+"]" if 'created_at' in keys else ""

    print "{0} : {1}------{2}".format(msg['nn'],msg['txt'],created_at)
    count = count+1