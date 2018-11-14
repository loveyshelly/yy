#coding=utf-8

from common.base import Base
from common.logger import logger as log
import time

class GrantCouponPage(Base):
    #wechat_grant_loc=("xpath","//*[@id='1542174294709-0-uiGrid-00C3-cell']/div/div/div/span/a")#定位至微信发放
    wechat_grant_loc = ("xpath", "//a[contains(text(),'微信发放')]")# 定位至微信发放
    peculiar_msend_loc=("xpath","//a[contains(text(),'特异群发')]")#定位至特异群发
    msend_loc=("xpath","//span[contains(text(),'群发消息')]")#定位至群发消息


    def main(self):

        log.info("begin grant coupon page")
        self.click(GrantCouponPage.wechat_grant_loc)# 点击微信发放
        self.click(GrantCouponPage.peculiar_msend_loc)#点击特异群发
        self.click(GrantCouponPage.msend_loc)#点击群发消息
        log.info("end grant coupon page")


