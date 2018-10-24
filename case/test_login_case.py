
from page.loginpage import LoginPage
from selenium import webdriver
import unittest
import ddt


#参数和代码分离
testdata=[
      {"username": "13544772266", "psw": "123456", "result": "13544772266"},
      ]

@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver) #实例化登录页面

    def login_case(self,username,psw):
        # 登录
        self.loginpage.login(username,psw)
        #判断是否有弹窗
        # self.loginpage.is_alert_exsit()
        # 获取登录结果
        res=self.loginpage.get_login_result()
        return res

    @ddt.data(*testdata)
    def test_login_01(self,canshu):
        re=self.login_case(canshu["username"],canshu["psw"])
        self.assertTrue(canshu["result"]==re)

    def tearDown(self):
        self.driver.delete_all_cookies()#清空cookies
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()







