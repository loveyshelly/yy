# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Base():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30
        self.poll=0.5
    def findElement(self,loctor):
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElements(self,loctor):
        elements=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(loctor))
        return elements

    def findElementNew(self,loctor):
        try:
            element=WebDriverWait(self.driver,self.timeout,self.poll).until( lambda x:x.find_element(*loctor))
            return element
        except:
            return "没有找到该元素"

    def findElementsNew(self,loctor):
        try:
            elements=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*loctor))
            return elements
        except:
            return "没有找到这些元素"

    def sendKeys(self,loctor,text):#输入框输入内容
        ele=self.findElement(loctor)
        ele.send_keys()

    def click(self,loctor):
        ele=self.findElement(loctor)
        ele.click()


    def clear(self,loctor):#清除
        ele=self.findElement(loctor)
        ele.clear()

    def moveToElement(self,loctor,driver):
        mos=self.findElement(loctor)#element是元素对象
        ActionChains().move_to_element(mos).perform()#这里传的driver也可以写到方法的参数里,这样： moveToElement(self,loctor,driver)

    def is_text_in_element(self,loctor,text):
        '''判断给定的text在这个元素的文本上
               要么返回true，要么返回false，不要让它抛异常
               三种情况为假：0，“”，None。python里没有null'''
        try:
            element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element)
            return element
        except:
            return False

    def is_value_in_element(self,loctor,text):
        '''判断给定的text在这个元素的文本上
        要么返回true，要么返回false，不要让它抛异常
        三种情况为假：0，“”，None。python里没有null
        1.找不到元素返回False
        2.value为空返回False
        3.text不在元素的value值里返回False
        '''
        try:
            element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element)
            return element
        except:
            return False

    def is_element_exsits(self,loctor):
        #查找元素的时候判断是否存在，存在就返回element，不存在就返回false
        try:
            element=self.findElement(loctor)
            return element
        except:
            return False

    def is_alert_exsit(self,timeout=5):
        alert=WebDriverWait(self.driver,timeout,self.poll).until(EC.alert_is_present)
        return alert

if __name__=="__main__":
    driver=webdriver.Firefox()#实例化driver
    base=Base(driver)#实例化driver这个类

















