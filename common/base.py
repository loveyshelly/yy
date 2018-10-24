#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Base():
    def __init__(self,driver):
        self.driver = driver
        self.timeout=30
        self.poll=1

    def findElement(self,loctor):#loctor是元祖类型
        '''
        args:
        loctor 传元祖，如("id","xx")
        '''
        element = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElements(self,loctor):
        elements=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_elements(*loctor))
        return elements

    def findElementNew(self,loctor):
        try:
           element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(loctor))
           return element
        except:
            return "没有找到该元素"

    def findElementsNew(self,loctor):
        try:
           elements=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(loctor))
           return elements
        except:
            return "没有找到这些元素"

    def sendKeys(self,loctor,text):
        ele=self.findElement(loctor)
        ele.send_keys(text)

    def click(self,loctor):
        ele=self.findElement(loctor)
        ele.click()

    def clear(self,loctor):
        ele=self.findElement(loctor)
        ele.clear()

    def moveToElement(self,loctor):
        '''鼠标悬停事件'''
        mos=self.findElement(loctor)#element是元素对象
        ActionChains(driver).move_to_element(mos).perform() #这里传的driver也可以写到方法的参数里,这样： moveToElement(self,loctor,driver)

    def is_text_in_element(self,loctor,text):
        '''判断给定的text在这个元素的文本上
        要么返回true，要么返回false，不要让它抛异常
        三种情况为假：0，“”，None。python里没有null'''
        try:
           element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element)
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
           element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element)
           return element
        except:
            return False

    def is_element_exsits(self, locator):
        '''查找元素的时候，存在返回element，不存在的时候Timeout异常了'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_alert_exsit(self, timeout=5):
        '''语文老师教的：直到，，，，才，，，
       如有alert,返回的是alert对象，
       没有就返回False'''
        alert = WebDriverWait(self.driver, timeout, self.poll).until(EC.alert_is_present())
        return alert



if __name__=="__main__":
    driver = webdriver.Firefox()#实例化driver
    base=Base(driver)#实例化driver这个类

    driver.get("https://www.baidu.com")#打开百度
    news_loc=("xpath",".//*[@id='u1']/a[1]")  #新闻
    res=base.is_text_in_element(news_loc,"新闻")
    print(res)
    btn_loc=("id","su")
    res1=base.is_value_in_element(btn_loc,"一下")

    loc1=("id","kw")#定位百度搜索框
    '''
    ele1=base.findElement(loc1)
    ele1.sendkeys("haode")
    '''
    base.sendKeys(loc1,"haode")

    loc2=("css selector","#su")#定位点击搜索按钮
    '''
    ele2=base.findElement(loc2)#*号后面的参数是一个list或者是一个元祖
    ele2.click()
    '''
    base.click(loc2)