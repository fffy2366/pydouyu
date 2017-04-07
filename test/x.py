#coding:utf8
import urllib
import urllib2
import cookielib
import socket
import time
import sys
import zlib
import httplib2
import re
import os
import json
reload(sys)
sys.setdefaultencoding('utf8')
#socket.setdefaulttimeout(20)
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection': 'keep-alive',
'Host':'www.sbobet.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36',
}
header2 = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
#'Cache-Control':'max-age=0',
'Connection': 'keep-alive',
#'Content-Type':'application/x-www-form-urlencoded',
'Host':'www.sbobet.com',
#'Origin':'https://www.sbobet.com',
'Referer':'https://www.sbobet.com/zh-cn/euro',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36',
}
event_hand = {
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.5',
#'Cache-Control':'max-age=0',
'Connection': 'keep-alive',
#'Content-Type':'application/x-www-form-urlencoded',
'Host':'www.sbobet.com',
#'Origin':'https://www.sbobet.com',
'Referer':'https://www.sbobet.com/zh-cn/euro',
#'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}
class Urlgets:
	def __init__(self):
		#socket.close
		self.defaulturl="https://www.sbobet.com/zh-cn/euro"
		self.loginurl="https://www.sbobet.com/web/public/process-sign-in.aspx"
		self.event_url="https://www.sbobet.com/zh-cn/data/event?"
		self.cookie=cookielib.LWPCookieJar()
		self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
		urllib2.install_opener(self.opener)
	def pri_ck(self):
		if self.cookie:
			for index, cookie in enumerate(self.cookie):
				print '[',index, ']',cookie;
			else:
				pass
		print "-"*100
	def m_time(self):
		return int(time.time()*1000)
	def create_log_file(self,data):
		filename="html/"+str(self.m_time())+".html"
		#print filename
		f=open(filename,'w+b')
		f.write(data)
		f.close
	def openurl(self):
		ret=urllib2.Request(self.defaulturl,headers=headers)
		try:
			os.system('clear')
			print "# Access : %s" % self.defaulturl
			print "-"*100
			res=urllib2.urlopen(ret,timeout=20)
			if res.code==200:
				print res.headers
				html=zlib.decompress(res.read(), 16+zlib.MAX_WBITS)
				self.create_log_file(html)
				self.pri_ck()
				##################################################################
				ck=r'name=\'HidCK\' value=(.*?) />'
				hidck=re.compile(ck)
				hidck=re.findall(hidck,html)
				print "# Active Hidck : %s" % str(hidck[0])
				###################################################################
				tag=r'id="tag" value="(.*?)" />'
				tags=re.compile(tag)
				tags=re.findall(tags,html)
				print "# Active Tags : %s" % str(tags[0])
				###################################################################
				fingerprint=r'id="fingerprint" value="(.*?)" />'
				fingerprints=re.compile(fingerprint)
				fingerprints=re.findall(fingerprints,html)
				print "# Active fingerprint : %s" % str(fingerprints[0])
				###################################################################
				ts=r"\'\d{8,13}\'\,\'(.*?)\'\,\'zh\-cn\'\,"
				tss=re.compile(ts)
				tss=re.findall(tss,html)
				print "# Active tkss : %s" % tss[0]
				###################################################################
				#[33353,0,2,0,0,0,0,'20170406',1,3,0,4]
				#[33353,0,2,0,0,0,0,'20170406',1,3,0,4]
				tk=r'\[(\d{3,5}\,\d{1}\,\d{1}\,\d{1}\,\d{1}\,\d{1}\,\d{1}\,\'\d{8}\'\,\d{1}\,\d{1}\,\d{1}\,\d{1})\]'
				tks=re.compile(tk)
				Token=re.findall(tks,html)
				print  "# Active old token %s" % Token[0].replace('\'','')
				###################################################################
				tk_num=r'\[(\d{3,6})\,\d{1}'
				tk_nums=re.compile(tk_num)
				tk_nums=re.findall(tk_nums,html)
				print "# Active old tk %s" % tk_nums[0]
				###################################################################
				rd=r'\[\d{3,5}\,\d{1}\,(\d{1}\,\d{1}\,\d{1}\,\d{1}\,\d{1}\,\'\d{8}\'\,\d{1}\,\d{1}\,\d{1}\,\d{1})\]'
				random=re.compile(rd)
				randomq=re.findall(random,html)
				random=tk_nums[0]+","+tk_nums[0]+","+randomq[0].replace('\'','')
				print "# News token ,look this ! %s " % random
				print "#"*100
				res.close
				event_url=self.event_url+"ts="+tss[0]+"&tk="+random
				print "# Access :%s " % event_url
				print "#"*100
				time.sleep(1)
				req=urllib2.Request(event_url,headers=event_hand)
				event=urllib2.urlopen(req,timeout=20)
				self.pri_ck()
				#print dir(event)
				new_res=zlib.decompress(event.read(), 16+zlib.MAX_WBITS)
				#json_str = json.dumps(new_res)
				#print json_str
				qq=r'onUpdate\(\'od\'\,\[(\d{3,5})\,'
				qq=re.compile(qq)
				qqs=re.findall(qq,new_res)
				if qqs:
					ntk=qqs[0]
				else:
					qq=r'onIdle\(\'od\'\,(\d{3,5})\)'
					qq=re.compile(qq)
					qqs=re.findall(qq,new_res)
					ntk=qqs[0]
				newtk=ntk+","+ntk+","+randomq[0].replace('\'','')
				print "# change tk number : %s" % newtk
				event.close
				return newtk,hidck[0],tags[0]
			else:
				time.sleep(1)
				self.openurl()
		except urllib2.URLError as e:
			print e.reason
	def userlogin(self):
		tk,hi,tag=self.openurl()
		#print tk,hi,tag
		time.sleep(1)
		values={}
		values['5']='1'
		values['HidCK']=hi
		# values['id']='isuntime66'
		values['id']='efpa2ha012'
		#efpa2ha010 efpa2ha011 efpa2ha012
		values['lang']='zh_cn'
		# values['password']='123456aa'
		values['password']='pppp1111'
		values['tag']=tag
		values['fingerprint']='4bb67c1cf7e5546e7267611629e3707c'
		values['tk']=tk
		values['type']='form'
		values['tzDiff']='0'
		#print values
		data=urllib.urlencode(values)
		print "-"*100
		#print data
		print "# Access: %s" % self.loginurl
		response = urllib2.Request(self.loginurl,data,header2)
		hh=urllib2.urlopen(response,timeout=20)
		print hh.geturl()
		self.pri_ck()
		hh.close
		return values
def cont():
	try:
		IM=Urlgets().userlogin()
		return True
	except:
		IM=Urlgets().userlogin()
		return False
