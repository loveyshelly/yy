#coding=utf-8

import unittest
import time
from selenium import webdriver
from page.login_page import LoginPage
from page.search_coupon import SearchCoupon
from common.logger import logger as log

class TestSearchCoupon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.search_coupon=SearchCoupon(cls.driver)

    def test_search_coupon(self):
        #登录
        self.login_page.login()
        time.sleep(5)
        #获取实际结果
        re=self.search_coupon.search()
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

