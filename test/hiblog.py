# -*- coding: utf-8 -*-
#http://selenium-python.readthedocs.io/installation.html
#http://www.cnblogs.com/LanTianYou/p/5578621.html
#[centos7服务器无GUI情况下安装使用Xvfb、selenium、chrome和selenium-server](http://blog.csdn.net/xds2ml/article/details/52982748)
#[Python with selenium: unable to locate element which really exist](http://stackoverflow.com/questions/24369249/python-with-selenium-unable-to-locate-element-which-really-exist)
#[Python爬虫利器五之Selenium的用法](http://www.cnblogs.com/BigFishFly/p/6380024.html)
#[selenium +phantomjs 登录126邮箱 iframe定位问题](http://blog.csdn.net/fastwxf/article/details/51547612)
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

def hiBlog(blog_url,username,pwd):
    # driver = webdriver.PhantomJS(service_args=["--web-security=false","--ignore-ssl-errors=true",'--ssl-protocol=any'])
    driver = webdriver.PhantomJS()
    # driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get("http://mail.163.com/")
    print "浏览器最大化"
    driver.maximize_window()  #将浏览器最大化显示
    driver.set_window_size(1000, 800)  #参数数字为像素点
    wait = ui.WebDriverWait(driver, 60)
    # wait.until(lambda dr: dr.find_element_by_name('email').is_displayed())
    wait.until(lambda dr: dr.find_element_by_xpath('//iframe[@id="x-URS-iframe"]').is_displayed())
    print driver.current_url
    # driver.save_screenshot('login.png')

    # time.sleep(3)
    #selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"name","selector":"email"}
    # 因为登录窗口变成了iframe
    frame = driver.find_element_by_xpath('//iframe[@id="x-URS-iframe"]')
    # print frame.get_attribute('innerHTML')
    print frame.get_attribute('outerHTML')
    # driver.switch_to.frame(frame)
    driver.switch_to.frame(frame)
    # driver.switch_to.frame(2)
    driver.switch_to.default_content()
    driver.switch_to.frame(2)

    # driver.switch_to.frame('frame_name')
    # 获取网页源代码
    content = driver.page_source.encode('utf-8')
    print content


    time.sleep(1)
    print driver.current_url
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_id("dologin").click()
    # wait.until(lambda dr: dr.find_element_by_id('login_area').is_displayed())
    # driver.get(blog_url)
    # wait.until(lambda dr: dr.find_element_by_id('么么哒').is_displayed())
    #返回(后退)
    # driver.back()
    #前进
    # driver.forward()
    # 截屏
    time.sleep(3)
    driver.save_screenshot('screen.png')
    driver.quit()
  
#执行该文件的主过程
if __name__ == '__main__':
    hiBlog("你的博客地址","fffy2366","xxxxxx")
