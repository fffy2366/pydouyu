#!bin/evn python
# -*-coding:utf8-*-
# doc:http://selenium-python.readthedocs.io/installation.html
__author__ = 'Frank'
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

if __name__ == '__main__':
    url="https://www.sbobet.com/zh-cn/euro"
    driver = webdriver.PhantomJS()
    driver.get(url)
    wait = ui.WebDriverWait(driver, 60)
    driver.find_element_by_id("username").send_keys("_efpa2ha012")
    driver.find_element_by_id("password").send_keys("_pppp1111")
    driver.execute_script("$M('tb').onSignIn();")
    wait.until(lambda dr: dr.find_element_by_id('login-name').is_displayed())
    print driver.current_url
    time.sleep(3)
    driver.save_screenshot('screen.png')
    driver.quit()