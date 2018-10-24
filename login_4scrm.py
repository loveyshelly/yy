#coding=utf-8

from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://pc.test-chexiu.cn/login/login")

ele=driver.find_element_by_xpath("//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/div[1]/input").send_keys("13544772266")
