#!bin/evn python
# -*-coding:utf8-*-
__author__ = 'Frank'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#模拟登陆163邮箱
# driver = webdriver.Firefox()
driver = webdriver.PhantomJS()

driver.get("http://mail.163.com/")

#用户名 密码
elem_user = driver.find_element_by_name("email")
elem_user.send_keys("")
elem_pwd = driver.find_element_by_name("password")
elem_pwd.send_keys("vjdyps@163")
elem_pwd.send_keys(Keys.RETURN)
time.sleep(5)
assert "baidu" in driver.title
driver.close()
driver.quit()
