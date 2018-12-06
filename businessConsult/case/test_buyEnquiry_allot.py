#coding=utf-8

import unittest
import time
from selenium import webdriver
from common.logger import logger as log
from page.login_page import LoginPage
from businessConsult.page.buyEnquiry_allot_page import BuyEnquiryAllotPage

class TestBuyEnquiryExport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.buyEnquiry_allot_page=BuyEnquiryAllotPage(cls.driver)

    def test_buyEnquiry_allot(self):
        customer_key="胡萝卜土"
        #登录
        self.login_page.login()
        time.sleep(5)
        #获取实际结果
        re=self.buyEnquiry_allot_page.main(customer_key)
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
