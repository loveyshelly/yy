#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class WechatMsendPage(Base):
    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    #qfzs_tab_loc = ("xpath", "//*[contains(@ui-sref,'market') and contains(@ui-sref-active, 'active')][1]")  # 定位“群发助手”
    wesend_list_loc = ("xpath", "//span[contains(text(),'微信群发')]")
    wecontent_loc=("xpath","//textarea[@placeholder='请输入文字......']")#定位微信内容文本框
    atten_time_loc=("xpath","//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/wechatgroupsend/div/div/tabwechat/div/div[2]/div[3]/div/div[2]/div/div[2]/form-all/div/div/div/div[2]/radio/div/div/div/div/div[2]")
    #atten_time_loc=("xpath","//label/input[@name='subscibeObject' and @class='ng-valid ng-not-empty ng-dirty ng-touched ng-valid-parse']")#定位关注时间-最近一周
    send_loc = ("xpath", "//span[contains(text(),'群发消息')]")

    def main(self,wecontent):
        log.info("begin wechat msend page")
        self.click(WechatMsendPage.qfzs_tab_loc)#点击群发助手
        time.sleep(2)
        self.click(WechatMsendPage.wesend_list_loc)#点击微信群发菜单
        time.sleep(2)
        self.sendKeys(WechatMsendPage.wecontent_loc,wecontent)#输入微信内容
        #self.inputTextArea(None, wecontent)
        time.sleep(5)
        self.click(WechatMsendPage.atten_time_loc)#选中“最近一周”
        time.sleep(2)
        self.click(WechatMsendPage.send_loc)#点击群发消息
        log.info("end wechat msend page")




