#coding=utf-8

from common.base import Base
from common.logger import logger as log
import time

class CovertCouponPage(Base):
    collector_tools_loc = ("xpath", "//span[contains(text(),'集客工具')]")  # 定位“集客工具”
    coupon_loc=("xpath","//span[contains(text(),'优惠券')]")#定位至优惠券菜单
    covert_loc = ("xpath", "//a[@ui-sref='jike.couponExchange']")# 定位至兑换
    covert_records_loc=("xpath","//uib-tab-heading[contains(text(),'兑换记录')]")#定位兑换记录
    export_loc=("xpath","//a[@class='btn btn-default']")#定位至导出
    download_loc=("xpath","//i[@class='glyphicon glyphicon-cloud-download text-primary']")#定位下载文件

    def main(self):
        log.info("begin covert coupon page")
        self.click(CovertCouponPage.collector_tools_loc)#点击“集客工具”
        self.click(CovertCouponPage.coupon_loc)#点击优惠券菜单
        self.click(CovertCouponPage.covert_loc)#点击兑换
        self.click(CovertCouponPage.covert_records_loc)#点击兑换记录
        time.sleep(20)
        self.click(CovertCouponPage.export_loc)#点击导出
        self.click(CovertCouponPage.download_loc)#点击下载文件
        log.info("end covert coupon page")



