#coding=utf-8

import time
from common.logger import logger as log
from common.base import Base

class AuditingCouponPage(Base):
    collector_tools_loc = ("xpath", "//a[@ui-sref='jike']")  # 定位“集客工具”
    coupon_loc=("xpath","//span[contains(text(),'优惠券')]")#定位至优惠券菜单
    audit_coupon_loc=("xpath","//span[contains(text(),'单券审核')]")#定位单券审核
    audit_loc=("xpath","//a[contains(text(),'快速审核')]")#定位快速审核
    sure_loc=("xpath","//span[contains(text(),'确定')]")#定位确定按钮

    def main(self):
        log.info("begin auditing coupon page")
        self.click(AuditingCouponPage.collector_tools_loc)#点击“集客工具”
        time.sleep(2)
        self.click(AuditingCouponPage.coupon_loc)#点击优惠券
        time.sleep(2)
        self.click(AuditingCouponPage.audit_coupon_loc)#点击单券审核
        time.sleep(2)
        self.click(AuditingCouponPage.audit_loc)#点击快速审核
        time.sleep(2)
        self.click(AuditingCouponPage.sure_loc)#点击确定按钮
        log.info("end auditing coupon page")
