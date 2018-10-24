#coding=utf-8
from common.base import Base
import time
from selenium import webdriver

loginurl="http://zentao.maotukeji.com/index.php?m=user&f=login"
#继承过来的方法不用实例化，可self.直接调用
class LoginPage(Base):
    '''登录页面'''
    zhanghao_loc = ("css selector", "#userMenu>a")
    def __init__(self,driver):
        self.driver=driver #形参
    def logout(self):
        '''登出'''
        self.driver.delete_all_cookies() #删除所有的cookies
        self.driver.refresh()

    def login(self, username="xiaoli", psw="Mt123456"):  # 这里的driver是形参
        '''登录函数'''
        # 保证函数里面的每个参数都要定义
        self.driver.get(loginurl)
        time.sleep(2)

        # 登录
        self.driver.find_element_by_name("account").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)

    def get_login_result(self):
        # 获取登录结果（用户名）
        try:
            t = self.find_element_by_css_selector(self.zhanghao_loc).text
            # 通过用户名判断是否登录成功
            return t

        except:
            print("登录失败！！！")
            return ""
    def is_alert_exsit(self):
        try:
            from selenium import webdriver
            driver=webdriver.Firefox()
            alert=driver.switch_to_alert()
            print(alert.text)
            alert.accept()
        except:
            pass


