# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest
mobile_emulation = {"deviceName":"iPhone 6"}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)


class Withdraw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("http://2020m90g52.51mypc.cn:35139/mercDemo/WebWithdraw_input.jsp")
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='form1']/center/table/tbody/tr[9]/td[2]/input").clear()
        self.driver.find_element_by_xpath("//*[@id='form1']/center/table/tbody/tr[9]/td[2]/input").send_keys("")  #输入存管会员编号
        self.driver.find_element_by_xpath("//*[@id='form1']/center/table/tbody/tr[20]/td[2]/input").click()  #提交
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/form/input[5]").click()  #提交
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/jspfile/section/section/div[2]/div[2]/div[2]/div").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='CHK_NO']").send_keys("")
        self.driver.find_element_by_xpath("//*[@id='PAY_PASS']").send_keys("")
        self.driver.find_element_by_xpath("//*[@id='confirm_tixian']").click()
        time.sleep(3)

    def Withdraw(self, mbrcode, CHK_NO, password):
        '''这里写了一个提现的方法，存管会员客户号、验证码、密码、参数化'''
        # driver.find_element_by_xpath("//*[@id='form1']/center/table/tbody/tr[9]/td[2]/input").clear()
        self.driver.find_element_by_xpath("//*[@id='form1']/center/table/tbody/tr[9]/td[2]/input").send_keys(mbrcode)
        # driver.find_element_by_xpath("//*[@id='CHK_NO']").clear()
        self.driver.find_element_by_xpath("//*[@id='CHK_NO']").send_keys(CHK_NO)
        # driver.find_element_by_xpath("//*[@id='PAY_PASS]").clear()
        self.driver.find_element_by_xpath("//*[@id='PAY_PASS]").send_keys(password)

    def test_001(self):
        self.Withdraw(mbrcode="0001100000143343",CHK_NO="123456",password="1234qwer")
        result = self.driver.find_element_by_xpath("/html/body/jspfile/div[2]/div[1]").text
        print(result)
        self.assertEqual(result,"提现成功")
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()