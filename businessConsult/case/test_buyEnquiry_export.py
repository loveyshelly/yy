#coding=utf-8

import unittest
import time
from selenium import webdriver
from common.logger import logger as log
from page.login_page import LoginPage
from businessConsult.page.buyEnquiry_export_page import BuyEnquiryExportPage

class TestBuyEnquiryExport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.buyEnquiry_exportpage=BuyEnquiryExportPage(cls.driver)

    def test_buyEnquiry_export(self):
        #登录
        self.login_page.login()
        time.sleep(5)
        #获取实际结果
        re=self.buyEnquiry_exportpage.main()
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
