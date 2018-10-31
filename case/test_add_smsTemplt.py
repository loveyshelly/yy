#coding=utf-8
#-*- coding: UTF-8 -*-.

import unittest
from page.login_page import LoginPage
from page.SMS_template import SMStemplate
from selenium import webdriver
import time
from common.logger import logger as log


class TestAddSMStemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.smstemplate=SMStemplate(cls.driver)

    def add_smsTemplate(self,tem_title,tem_detail):
        #登录
        self.loginpage.login()
        time.sleep(10)
        #点击【群发助手】，【短信模板】，【新增】
        self.smstemplate.click_qfzs_tab()
        self.smstemplate.click_sms_tab()
        time.sleep(1)
        self.smstemplate.click_new_btn()
        #在标签中选择“活动”
        #这里要等待一下，因为页面是ajax的，活动按钮一开始的时候是点击无效的
        time.sleep(1)
        self.smstemplate.click_sele_tag()
        log.info('Done select..')
        #输入模板名称
        self.smstemplate.input_tem_title(tem_title)
        #输入模板内容
        self.smstemplate.input_tem_detail(tem_detail)
        #点击【确定】
        return self.smstemplate.click_confirm()
        # #点击每页显示数量下拉框
        # self.smstemplate.click_page_index()
        # #选中每页显示50条选项
        # self.smstemplate.click_page_number()
        # #获取模板标题
        # re=self.smstemplate.get_tem_title()

    def test_add_smsTemplate(self):
        tem_title=u"双11活动"
        tem_detail=u"活动当天消费双倍积分"
        #获取实际结果
        res = self.add_smsTemplate(tem_title, tem_detail)
        #期望结果
        log.info(res)
        #断言
        #self.assertEqual(re,ex)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

