#coding=utf-8

import time
import unittest
from selenium import webdriver
from common.logger import logger as log
from page.login_page import LoginPage
from page.data_import_page import DataImportPage


class TestDataImpot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.data_import=DataImportPage(cls.driver)

    def test_data_import(self):
        userdata = "E:\\车主导入.xlsx"
        cardata="E:\\车辆导入.xlsx"
        maintenancedata="E:\\维保导入.xlsx"
        renewaldata="E:\\续保导入.xlsx"

        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        re=self.data_import.main(userdata,cardata,maintenancedata,renewaldata)
        #期望结果
        log.info("re")

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
