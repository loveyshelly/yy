#coding=utf-8

import unittest
import time
import datetime
from common.logger import logger as log
from page.login_page import LoginPage
from page.add_activity_page import AddActivity
from selenium import webdriver

class TestAddActivity(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.add_activity_page=AddActivity(cls.driver)

    def test_add_activity(self):
        name="双11大促"
        keys="11"
        cover_path = "E:\\a8.jpg"
        theme_path = "E:\\a3.jpg"
        stime=(datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        etime=(datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        eetime=(datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
        money="100"
        reason="活动经费"
        dot="多重优惠"
        s_abstract="省更多"
        tphone="13424399553"

        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        re=self.add_activity_page.main(name,keys,cover_path,theme_path,stime,etime,eetime,money,reason,dot,s_abstract,tphone)
        #期望结果
        log.info('re')

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



