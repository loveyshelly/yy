#coding=utf-8

import time
import datetime
import unittest
from selenium import webdriver
from common.logger import logger as log
from page.login_page import LoginPage
from page.creat_coupon_page import CreatCouponPage

class TestCreatCoupon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.creat_coupon_page=CreatCouponPage(cls.driver)

    def test_creat_coupon(self):
        coupon_name="双12五折券"
        money="0.01"
        liveTime=(datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        introductions="多买优惠越多"
        notices="仅限本人使用"
        number="100"
        instructions="双12活动在即"
        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        re=self.creat_coupon_page.main(coupon_name,money,liveTime,introductions,notices,number,instructions)
        #期望结果
        log.info("re")

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()






