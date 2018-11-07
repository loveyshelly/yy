#coding=utf-8

import unittest
from selenium import webdriver
from page.login_page import LoginPage
from page.reward_convert_page import RewardConvertPage
from common.logger import logger as log

class TestRewardConvert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.reward_convert_page=RewardConvertPage(cls.driver)

    def test_reward_convert(self):
        convertnum="123456789000"
        #登录
        self.loginpage.login()
        #获取实际结果
        self.reward_convert_page.main(convertnum)
        #期望结果
        log.info("re")

    def tearDown(self):
        pass

if __name__=="__main__":
    if __name__ == '__main__':
        unittest.main()


