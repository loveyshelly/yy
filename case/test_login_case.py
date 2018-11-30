#coding=utf-8

from page.login_page import LoginPage
from selenium import webdriver
import unittest
from common.logger import logger as log

class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver) #实例化登录页面

    def test_login(self,username,psw):

        # 获取实际结果
        re=self.loginpage.login(username,psw)
        #期望结果
        log.info("re")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main()








