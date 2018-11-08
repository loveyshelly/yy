#coding=utf-8

import time
import unittest
from selenium import webdriver
from page.login_page import LoginPage
from page.convert_records_page import ConvertRecordspage

class TestConvertRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage.login(cls.driver)
        cls.convert_records_page=ConvertRecordspage(cls.driver)

    def main(self):
        #登录
        self.loginpage.login()
        #获取实际结果
        re=self.covert_records_page.main()

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

