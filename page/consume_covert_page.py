#coding=utf-8

from common.base import Base
from common.logger import logger as log
import time

class CovertConsumePage(Base):
    collector_tools_loc = ("xpath", "//span[contains(text(),'集客工具')]")  # 定位“集客工具”
    coupon_loc=("xpath","//span[contains(text(),'优惠券')]")#定位至优惠券菜单
    covert_tab = ("xpath", "//a[@ui-sref='jike.couponExchange']")# 定位至兑换菜单
    input_code=("xpath","//input[@placeholder='请输入优惠券兑换码']")#定位至兑换码输入框
    covert_loc=("xpath","//a[@class='btn-primary']")#定位兑换按钮

    def main(self,code):
        log.info("begin covert coupon page")
        self.click(CovertConsumePage.collector_tools_loc)#点击“集客工具”
        self.click(CovertConsumePage.coupon_loc)#点击优惠券
        self.click(CovertConsumePage.covert_tab)#点击兑换菜单
        self.sendKeys(CovertConsumePage.input_code,code)#输入兑换码
        self.click(CovertConsumePage.covert_loc)#点击兑换
        log.info("end covert coupon page")



