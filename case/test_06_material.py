#coding=utf-8
#-*- coding: UTF-8 -*-.

import unittest

import time
from page.login_page import LoginPage
from page.material_page import MaterialPage
from selenium import webdriver
from common.logger import logger as log

class TestAddMaterial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.material_page = MaterialPage(cls.driver)

    def test_add_material(self):
        title=u"关于双11活动"
        abstract=u"活动细则说明"
        content=u"活动细则说明内容"
        author=u"shelly"
        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        res = self.material_page.main(title, author, abstract, content)
        #期望结果
        log.info(res)
        #断言
        #self.assertEqual(re,ex)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()

