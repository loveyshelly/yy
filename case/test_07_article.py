#coding=utf-8

import unittest
import time
from common.logger import logger as log
from page.login_page import LoginPage
from page.publish_article_page import PublishArticlePage
from selenium import webdriver

class TestPublisArticle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.publis_article_page=PublishArticlePage(cls.driver)

    def test_publish_article(self):

        title="shelly test title"
        coverpath="E:\\a8.jpg"
        acontent="shelly test content"
        #登录
        self.loginpage.login()
        time.sleep(10)
        #获取实际结果
        re=self.publis_article_page.main(title,coverpath,acontent)
        # 期望结果
        log.info('re')

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()






