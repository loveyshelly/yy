#coding=utf-8

import unittest
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

        title="测试文章标题"
        coverpath="E:\\a8.jpg"
        content="测试文章标题"
        #登录
        self.loginpage.login()
        #获取实际结果
        re=PublishArticlePage.main(title,coverpath,content)
        # 期望结果
        log.info('re')

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()






