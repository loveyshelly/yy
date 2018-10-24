#coding=utf-8

import unittest
from page.loginpage_shelly import LoginPage
from page.editbug import NewBug
from selenium import webdriver
import time

class TestNewBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.newbug=NewBug(cls.driver)

    def add_bug(self,bugtitle,bugdetail): #创建bug流程

        # 1.登录
        self.loginpage.login()
        # 2.点【测试】，【bug】，【提交bug】
        self.newbug.click_test_tab()
        self.newbug.click_bug()
        self.newbug.click_add_bug()
        # 3.编辑bug
        self.newbug.add_truk()
        self.newbug.input_bug_title(bugtitle)

        #self.newbug.input_bug_detail(bugdetail)
        self.newbug.click_save()
        #获取点完之后的实际结果
        result=self.newbug.get_bug_title()
        print("获取实际结果：%s" % result)
        return result

    def test_add_bug(self):
        nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
        bugtitle="测试用的标题"+nowtime
        bugdetail="bug正文"
        re=self.add_bug(bugtitle,bugdetail)
        # 5.期望结果
        ex ="[未确认] "+bugtitle
        # 断言：实际结果和期望结果对比
        self.assertEqual(re,ex,msg="断言失败")
        #self.assertTrue(re==ex)

    def tearDown(self):
        #每次执行完之后连接数据库执行SQL删除这条
        pass

if __name__=="__main__":
    unittest.main()








