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
reload(sys)
sys.setdefaultencoding('utf8')
socket.setdefaulttimeout(10)
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
class Urlgets:
	def __init__(self):
		self.defaulturl="https://www.sbobet.com/"
		self.loginurl="https://www.sbobet.com/web/public/process-sign-in.aspx"
		#self.jsonurl="http://isn8213.com/membersite/zh-CN/resource/events/refresh/1/1/3/3/0/4/0/1?_="
		self.cookie=cookielib.LWPCookieJar()
		self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
		urllib2.install_opener(self.opener)
	def pri_ck(self):
		if self.cookie:
			for index, cook in enumerate(self.cookie):
				print "["+str(index)+"]",cook;
			else:
				pass
		print "-"*100
	def m_time(self):
		return int(time.time()*1000)
	def create_log_file(self,data):
		f=open("html/"+str(self.m_time())+".html",'w')
		f.write(data)
		f.close
	def userlogin(self):
		ret=urllib2.Request(self.defaulturl,headers=headers)
		try:
			res=urllib2.urlopen(ret,timeout=20)
			html=zlib.decompress(res.read(), 16+zlib.MAX_WBITS)
			print res.headers
			print res.code
			print res.url
			self.create_log_file(html)
			ck=r'name=\'HidCK\' value=(.*?) />'
			t=r'(\d{4,5}\,(\d\,){6}\'(\d){8}\'\,(\d\,){3}\d)'
			ts=r'id="tag" value="(.*?)" />'
			hidck=re.compile(ck)
			tk=re.compile(t)
			tags=re.compile(ts)
			hidck=re.findall(hidck,html)
			tags=re.findall(tags,html)
			Token=re.search(tk,html).group().replace('\'','')
			res.close
			print "Active Token : %s" % str(Token)
			print "Action Hidck : %s" % str(hidck[0])
			print "Action Tags : %s" % str(tags[0])
			self.pri_ck()
			print "#"*100
		except urllib2.URLError as e:
			print e.reason
		time.sleep(1)
		values={}
		values['tag']=tags[0]
		values['HidCK']=hidck[0]
		values['tk']=Token
		values['password']='pppp1111'
		values['id']='efpa2ha011'
		values['fingerprint']='bad1c989ff6b7081c761eedfa6ba1c34'
		values['lang']='zh_cn'
		values['5']='1'
		values['type']='form'
		values['tzDiff']='0'
		data=urllib.urlencode(values)
		response = urllib2.Request(self.loginurl, data=data, headers=header2)
		try:
			print "-"*100
			result=urllib2.urlopen(response)
			self.pri_ck()
			print dir(result)
			print result.headers
			print result.getcode
			print result.url
		except urllib2.URLError as e:
			print e.code
		#self.pri_ck()
		#print result.read()
		#result.close()
		#return False
	# def get_json(self):
	# 	self.userlogin()
	# 	time.sleep(1)
	# 	#data = urllib.urlencode(logindata)
	# 	print "GET JSON CONTENT"
	# 	jsonurl=self.jsonurl+str(self.m_time())
	# 	url=urllib2.Request(jsonurl,headers=headers)
	# 	print "-"*100+"\n"+jsonurl+"\n"
	# 	while True:
	# 		try:
	# 			print "try down once !"
	# 			result = urllib2.urlopen(url,timeout=3)
	# 			self.pri_ck()
	# 			res=result.read()
	# 			if res:
	# 				html = zlib.decompress(res, 16+zlib.MAX_WBITS)
	# 				print "-"*100
	# 				print html
	# 			else:
	# 				print "error"
	# 			time.sleep(1)
	# 		except urllib2.URLError as e:
	# 			self.get.json()
	# 	else:
	# 		pass
IM=Urlgets()
IM.userlogin()