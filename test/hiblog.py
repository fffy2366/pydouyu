# -*- coding: utf-8 -*-
#http://www.cnblogs.com/LanTianYou/p/5578621.html
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

import time

def hiBlog(blog_url,username,pwd):
    driver = webdriver.PhantomJS()
    driver.get("http://mail.163.com/")
    # driver.get("http://xinclean.cn/audit/login")
    print "浏览器最大化"
    driver.maximize_window()  #将浏览器最大化显示
    driver.set_window_size(1000, 800)  #参数数字为像素点
    # wait = ui.WebDriverWait(driver, 60)
    # wait.until(lambda dr: dr.find_element_by_name('email').is_displayed())
    driver.find_element_by_id("lbNormal").click()
    r = driver.execute_script("return newsJason")
    print r
    time.sleep(1)
    # driver.find_element_by_name("email").send_keys(username)
    # driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_id("dologin").click()
    # wait.until(lambda dr: dr.find_element_by_id('login_area').is_displayed())
    # driver.get(blog_url)
    # wait.until(lambda dr: dr.find_element_by_id('么么哒').is_displayed())
    #么么哒，ヾ(￣▽￣)Bye~Bye~知道为什么要冷静三秒钟吗？自己想。
    time.sleep(3)
    driver.save_screenshot('screen.png')
    driver.quit()
  
#执行该文件的主过程
if __name__ == '__main__':
    # hiBlog("你的博客地址","fffy2366","jdypsxxx")

    url="https://www.sbobet.com/zh-cn/euro"
    driver = webdriver.PhantomJS()
    driver.get(url)
    wait = ui.WebDriverWait(driver, 60)
    driver.find_element_by_id("username").send_keys("_efpa2ha012")
    driver.find_element_by_id("password").send_keys("_pppp1111")
    driver.execute_script("$M('tb').onSignIn();")
    # driver.execute_script("alert();")
    # driver.execute_script("document.write(11111);")
    wait.until(lambda dr: dr.find_element_by_id('login-name').is_displayed())
    time.sleep(3)
    driver.save_screenshot('screen.png')
    driver.quit()