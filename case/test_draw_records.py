#coding=utf-8

import unittest
import time
from page.login_page import LoginPage
from page.draw_records_page import DrawRecordsPage
from selenium import webdriver
from common.logger import logger as log

class TestDrawRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.draw_records_page=DrawRecordsPage(cls.driver)

    def test_draw_records(self):
        #登录
        self.loginpage.login()
        #获取实际结果
        re=self.draw_records_page.main()
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



