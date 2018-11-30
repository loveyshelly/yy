#coding=utf-8

import time
import unittest
from selenium import webdriver
from page.login_page import LoginPage
from page.data_analysis_page import DataAnalysisPage
from common.logger import logger as log

class TestDataAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login_page=LoginPage(cls.driver)
        cls.data_analysis=DataAnalysisPage(cls.driver)

    def test_data_analysis(self):
        #登录
        self.login_page.login()
        #获取实际结果
        re=self.data_analysis.main()
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
