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
cids = r.zrevrange("douyugiftset:"+rid,start,end)

for cid in cids:
    # 从hash表取出弹幕
    msg = r.hget("douyugifthash:"+rid,cid)
    # msg = json.loads(msg)
    msg = eval(msg)
    keys =  msg.keys()

    created_at = "["+msg['created_at']+"]" if 'created_at' in keys else ""
    giftlist = {}
    giftlist['191'] = "鱼丸"
    giftlist['192'] = "192"
    giftlist['507'] = "507"
    giftlist['508'] = "508"
    giftlist['512'] = "圆蛋"
    giftlist['513'] = "小红包"
    giftlist['514'] = "鸡小萌"
    giftlist['515'] = "三周年蛋糕"
    giftlist['516'] = "庆典飞艇"
    giftlist['517'] = "跨年火箭"
    keys = giftlist.keys()
    gift = giftlist[msg['gfid']] if msg['gfid'] in keys else msg['gfid']
    print "感谢{0}赠送的{1}------{2}".format(msg['nn'],gift,created_at)