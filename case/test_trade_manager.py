#coding=utf-8

import unittest
import time
from common.logger import logger as log
from page.login_page import LoginPage
from page.trade_manager_page import TradeManagerPage
from selenium import webdriver

class TestTradeManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.trade_manager_page=TradeManagerPage(cls.driver)

    def test_trade_manager(self):
        #登录
        self.login_page.login()
        #获取实际结果
        re=self.trade_manager_page.main()
        #期望结果
        log.info("re")

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()