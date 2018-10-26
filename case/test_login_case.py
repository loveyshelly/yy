#-*- coding: UTF-8 -*-.

from page.loginpage import LoginPage
from selenium import webdriver
import unittest


class LoginCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.loginpage = LoginPage(cls.driver)  #实例化登录页面

	def test_login(self):
		# 登录
		self.loginpage.login("13544772266", "123456")
		#判断是否有弹窗
		# self.loginpage.is_alert_exsit()
		# 获取登录结果
		re = self.loginpage.get_login_result()
		self.assertEqual(re, "13544772266")

	def tearDown(self):
		self.driver.delete_all_cookies()  #清空cookies
		self.driver.refresh()

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == "__main__":
	unittest.main()
