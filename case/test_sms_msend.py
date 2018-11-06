#coding=utf-8

import time
import unittest
from selenium import webdriver
from page.login_page import LoginPage
from page.sms_msend_page import SmsMsendPage
from common.logger import logger as log

class TestSmsMsend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.sms_msend_page=SmsMsendPage(cls.driver)

    def test_sms_msend(self):
        scontent="双11活动开始了！"
        sphone="13424399553"
        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        re=self.sms_msend_page.main(scontent,sphone)
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

