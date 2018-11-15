#coding=utf-8

import unittest
import time
from selenium import webdriver
from common.logger import logger as log
from page.login_page import LoginPage
from page.consume_covert_page import CovertConsumePage

class TestConsumeCovert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.consume_covert_page=CovertConsumePage(cls.driver)

    def test_consume_covert(self):
        code="573935501845"
        #登录
        self.login_page.login()
        #获取实际结果
        re=self.consume_covert_page.main(code)
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



