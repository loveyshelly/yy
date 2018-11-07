#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class SmsMsendPage(Base):
    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    sms_msend_loc=("xpath","//a[@ui-sref='market.messageGroupsend']")#定位短信群发菜单
    input_sms_content=("xpath","//textarea[@placeholder='请输入文字......']")#定位短信内容文本框
    input_sms_sendee=("xpath","//textarea[@placeholder='手动输入号码请用英文逗号或换行分隔。']")#定位短信接收人文本框
    send_loc=("xpath","//buttoncell[@class='inline-block ng-isolate-scope']")#发送

    def main(self,scontent,sphone):
        log.info("begin sms send page")
        self.click(SmsMsendPage.qfzs_tab_loc)#点击“群发助手”
        time.sleep(2)
        self.click(SmsMsendPage.sms_msend_loc)#点击“短信群发”
        self.sendKeys(SmsMsendPage.input_sms_content,scontent)#输入短信内容
        self.sendKeys(SmsMsendPage.input_sms_sendee,sphone)#输入接收人手机号
        self.click(SmsMsendPage.send_loc)#点击发送
        log.info("end sms send page")





