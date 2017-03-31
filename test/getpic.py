#coding:utf8
import urllib
import urllib2
import cookielib
import pytesseract as pyim
import time
from PIL import Image
import sys
import zlib
reload(sys)
sys.setdefaultencoding('utf8')
headers = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection': 'keep-alive',
'Host':'isn8213.com',
'Origin':'http://isn8213.com',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Referer':'http://isn8213.com/membersite/login.jsp',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}
class Urlgets:
	def __init__(self):
		self.defaulturl="http://isn8213.com/membersite/login.jsp"
		self.loginurl="http://isn8213.com/membersite/resource/member/login"
		self.captrueurl="http://isn8213.com/membersite/ui/captcha?w=50&h=20&fs=18&"
		self.cookie=cookielib.LWPCookieJar()
		self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
		# self.jsonurl="http://isn8213.com/membersite/zh-CN/ui/tpl/news_ticker.jsp?_="
		self.jsonurl="http://isn8213.com/membersite/zh-CN/resource/events/refresh/1/1/3/3/0/4/0/1?_="
		urllib2.install_opener(self.opener)
	def pri_ck(self):
		if self.cookie:
			for index, cookie in enumerate(self.cookie):
				print '[',index, ']',cookie;
			else:
				pass
	def m_time(self):
		return int(time.time()*1000)
	def creaturlopen(self):
		imgurl=self.captrueurl+str(self.m_time())
		request=urllib2.Request(imgurl,headers=headers)
		try:
			result=urllib2.urlopen(request,timeout=20)
			self.pri_ck()
			return result.read(),imgurl
		except urllib2.URLError as e:
			print e.reason
	def get_picture(self):
		res,imgurl=self.creaturlopen()
		print "url=%s" %imgurl
		atime=int(time.time()*1000)
		local=open('face/image.jpg', 'wb')
		local.write(res)
		local.close()
		im=Image.open('face/image.jpg')
		imgry=im.convert('L')
		time.sleep(0.3)
		num=pyim.image_to_string(imgry)
		print "Verification code:%s" % num
		btime=int(time.time()*1000)
		print "start timestamp is: %s end timestamp is: %s" % (atime,btime)
		ctime=btime-atime
		print "Total consumption of %s milliseconds" % ctime
		return num,ctime
	def userlogin(self):
		#try access once
		once=urllib2.Request(self.defaulturl)
		try:
			once=urllib2.urlopen(once,timeout=20)
			datas=once.read()
			#once=zlib.decompress(datas, 16+zlib.MAX_WBITS)
			print "*"*100
			self.pri_ck()
			print "*"*100
		except urllib2.URLError as e:
			print e.reason
		time.sleep(1)
		num,ctime=self.get_picture()
		logindata={'buId':1,'code':num,'language':'zh_CN','password':'qqqq1111','username':'xch570bx3'}
		data=urllib.urlencode(logindata)
		print logindata
		request=urllib2.Request(self.loginurl,data,headers)
		try:
			result=urllib2.urlopen(request,timeout=20)
			res=result.read()
			html=zlib.decompress(res, 16+zlib.MAX_WBITS)
			print "USER LOGIN"
			print "-"*100
			print html
			self.pri_ck()
			print "-"*100
		except urllib2.URLError as e:
			print e.reason
	def get_json(self):
		self.userlogin()
		time.sleep(1)
		#data = urllib.urlencode(logindata)
		print "GET JSON CONTENT"
		jsonurl=self.jsonurl+str(self.m_time())
		url=urllib2.Request(jsonurl,headers=headers)
		print "-"*100+"\n"+jsonurl+"\n"
		try:
			result = urllib2.urlopen(url,timeout=20)
			self.pri_ck()
			html = zlib.decompress(result.read(), 16+zlib.MAX_WBITS)
			print html
		except urllib2.URLError as e:
			print e.reason
IM=Urlgets().get_json()