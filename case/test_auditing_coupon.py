#coding=utf-8

import unittest
import time
from selenium import webdriver
from page.loginf_page import LoginPage
from page.auditing_coupon_page import AuditingCouponPage
from common.logger import logger as log

class TestAuditingCoupon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginf_page=LoginPage(cls.driver)
        cls.auditing_coupon_page=AuditingCouponPage(cls.driver)

    def test_auditing_coupon(self):
        #登录
        self.loginf_page.login()
        time.sleep(10)
        #获取实际结果
        re=self.auditing_coupon_page.main()
        #期望结果
        log.info("re")

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()

