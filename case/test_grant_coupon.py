#coding=utf-8

import unittest
import time
from selenium import webdriver
from common.logger import logger as log
from page.login_page import LoginPage
from page.grant_coupon_page import GrantCouponPage

class TestGrantCoupon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.grant_coupon_page=GrantCouponPage(cls.driver)

    def test_grant_coupon(self):
        #登录
        self.login_page.login()
        time.sleep(10)
        #获取实际结果
        re=self.grant_coupon_page.main()
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
