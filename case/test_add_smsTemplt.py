#coding=utf-8
#-*- coding: UTF-8 -*-.

import unittest
from page.loginpage import LoginPage
from page.SMS_template import SMStemplate
from selenium import webdriver
import time

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
        self.smstemplate.click_new_btn()
        #在标签中选择“活动”
        self.smstemplate.click_sele_tag()
        #输入模板名称
        self.driver.switch_to_window  # 将焦点定位于弹出框
        self.smstemplate.input_tem_title(tem_title)
        #输入模板内容
        self.smstemplate.input_tem_detail(tem_detail)
        #点击【确定】
        self.smstemplate.click_confirm()
        time.sleep(2)
        #点击每页显示数量下拉框
        self.smstemplate.click_page_index()
        #选中每页显示50条选项
        self.smstemplate.click_page_number()
        #获取模板标题
        re=self.smstemplate.get_tem_title()
        return re

    def test_add_smsTemplate(self):
        tem_title="双11活动"
        tem_detail="活动当天消费双倍积分"
        #获取实际结果
        re=self.add_smsTemplate(tem_title,tem_detail)
        #期望结果
        ex=tem_title
        #断言
        self.assertEqual(re,ex)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

