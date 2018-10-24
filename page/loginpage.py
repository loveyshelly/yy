from common.base import Base

loginurl='https://pc.test-chexiu.cn/login/login'

class LoginPage(Base):
    '''登录页面'''
    user_loc=("xpath","//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/div[1]/input")#输入账号
    psw_loc=("xpath","//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/div[2]/input")#输入密码
    sub_loc=("xpath","//*[@id='app']/div/div/login/div/div/div/div[2]/div/form/div[2]/button")#点击登录
    zhanghao_loc=("xpath","//*[@id='app']/div/div/layout/div/headbar/header/div/div[2]/div/div[3]/dropdown/div/span/div/span")

    def open_login_page(self):
        self.driver.get(loginurl)

    def logout(self):
        '''登出'''
        # driver = webdriver.Firefox()
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()

    def input_username(self,usrname):
        '''输入账号'''
        self.sendKeys(self.user_loc, usrname)

    def input_psw(self, psw):
        '''输入密码'''
        self.sendKeys(self.psw_loc, psw)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click(self.sub_loc)

    def login(self, username="13544772266", psw="123456"):
        '''登录流程:'''
        self.open_login_page()
        self.input_username(username)
        self.input_psw(psw)
        self.click_login_button()

    def get_login_result(self):
        '''获取登录的结果'''
        try:
            t = self.findElement(self.zhanghao_loc).text
            return t
        except:
               print("登录失败！！！，返回空字符")
               return ""

    def is_alert(self):
        '''判断是否有弹窗，有的话点确定，没有的话就pass
        有缺陷：如果页面卡，出现alert慢就判断不到了
        '''
        try:
            alert = self.driver.switch_to_alert()  # 这一步不会报错
            print(alert.text)     # 这一步，没有获取到alert文本就报错了
            alert.accept()  # 点确定按钮
        except:
            pass

    def is_alert_exsits_base(self):
        try:
            alert = self.is_alert_exsit()
            alert.accept()
        except:
            pass
