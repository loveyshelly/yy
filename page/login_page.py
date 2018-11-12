#-*- coding: UTF-8 -*-.
from common.base import Base
from common.logger import logger as log

loginurl = "https://pc.test-chexiu.cn/login/login"

class LoginPage(Base):
    '''登录页面'''
    user_loc=("xpath","//input[@placeholder='账号']")#输入账号
    psw_loc=("xpath","//input[@type='password']")#输入密码
    sub_loc=("xpath","//span[contains(text(),'登录')]")#点击登录
    zhanghao_loc=("xpath","//*[@id='app']/div/div/layout/div/headbar/header/div/div[2]/div/div[3]/dropdown/div/span/div/span")

    def open_login_page(self):
        self.driver.get(loginurl)

    def logout(self):
        '''登出'''
        # driver = webdriver.Firefox()
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()


    def login(self, username="cheshangtongscrm", psw="16888cst"):
        '''登录流程:'''
        log.info("begin login page")
        self.open_login_page()
        self.sendKeys(LoginPage.user_loc,username)#输入账号
        self.sendKeys(LoginPage.psw_loc,psw)#输入密码
        self.click(LoginPage.sub_loc)#点击登录按钮
        log.info("end login page")


