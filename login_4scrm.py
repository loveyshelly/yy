#coding=utf-8

from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://pc.test-chexiu.cn/login/login")

ele=driver.find_element_by_xpath("//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/div[1]/input").send_keys("13544772266")
ele1=driver.find_element_by_xpath("//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/div[2]/input").send_keys("123456")
ele2=driver.find_element_by_xpath("//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/button").click()
time.sleep(10)
ele3=driver.find_element_by_xpath("//*[@id='step1']/div[2]/a/span").click()#点击“群发助手”
time.sleep(2)
add_tem=driver.find_element_by_class_name("templateAdd pointer ng-scope").click()
'''
ele4=driver.find_element_by_xpath("//*[@id='app']/div/div/market/layout/div/div/layout-body/main/aside/subnav/section/div[1]/div[3]/a/span").click()#点击“短信模板”
time.sleep(2)
ele5=driver.find_element_by_xpath("//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/message-template/sms-template/div/div[2]/div/datatable/div/div[1]/div/div[1]/datatable-tools/buttoncell[1]/div/a/span").click()#点击“新增”
time.sleep(2)
driver.switch_to_window
ele6=driver.find_element_by_xpath("/html/body/div[1]/div/div/edit-message-template/div/div[1]/tags/div/div[2]/div[5]/span").click()#点击“活动”标签
time.sleep(2)
driver.switch_to_window
tem_title=driver.find_element_by_xpath("/html/body/div[1]/div/div/edit-message-template/div/div[3]/inputcell/div/div/div[2]/input").send_keys("biaoti")#输入名称
time.sleep(2)
driver.switch_to_window
tem_detail=driver.find_element_by_xpath("//*[@id='msgArea']/div/div/div[2]/textarea").send_keys("neirong")#输入内容
time.sleep(2)
confirm=driver.find_element_by_xpath("/html/body/div[1]/div/div/edit-message-template/div/div[4]/buttoncell[1]/div/a").click()#点击【确定】
time.sleep(2)
s=driver.find_element_by_xpath("//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/message-template/sms-template/div/div[2]/div/datatable/div/div[1]/div/div[2]/span/selectcell/div/div/div/div/a/span[3]/b").click()
time.sleep(2)
fanye=driver.find_element_by_xpath("//*[@id='ui-select-choices-row-0-1']/div/div").click()
time.sleep(2)
js1 = "document.documentElement.scrollTop=10000"
driver.execute_script(js1)
'''