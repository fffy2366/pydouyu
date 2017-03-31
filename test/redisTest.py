#!bin/env python
# -*-coding:utf8-*-
import redis
import datetime
import time

print 'Hello World!'

l = [1,2,5,4,3]

print l

t = (1,2,4)

print t

# 连接redis

r = redis.Redis(host='localhost', port=6379, db=0, password='db2016')

# redis string
r.set('test','2017 hello')
print r.get('test')

r.zadd("listtest","key",90)
# print r.get("listtest")

#redis list
# r.lpush("pushname","pushvalue")
print r.rpop("pushname")

# redis hash map
r.hset("maptest:2017-01-01","key1","value2")
r.hset("maptest:2017-01-02","key1","value3")
print r.hget("maptest:2017-01-02","key1")


# created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
created_at = datetime.datetime

print created_at

[].append()


# 获得当前时间时间戳
now = int(time.time())  #->这是时间戳
print now