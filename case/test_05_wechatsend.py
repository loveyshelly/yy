#coding=utf-8

import time
import unittest
from page.login_page import LoginPage
from page.wechat_msend_page import WechatMsendPage
from selenium import webdriver
from common.logger import logger as log

class TestWechatSend(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.wechat_msend=WechatMsendPage(cls.driver)

    def test_wechat_msend(self):
        wecontent="双11活动报名开始了！"
        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        re=self.wechat_msend.main(wecontent)
        #期望结果
        log.info('re')

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
