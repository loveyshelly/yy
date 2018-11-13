#coding=utf-8

from common.base import Base
from common.logger import logger as log
import time

class GrantCouponPage(Base):
    collector_tools_loc=("xpath","//span[contains(text(),'集客工具')]")#定位“集客工具”
    coupon_loc=("xpath","//span[contains(text(),'优惠券')]")#定位至优惠券菜单
    grant_loc=("xpath","//a[@ui-sref='jike.couponGrant']")#定位至发放
    wechat_grant_loc=("xpath","(//span[contains(text(),'微信发放')])[0]")#定位至微信发放
    peculiar_msend_loc=("xpath","//a[contains(text(),'特异群发')]")#定位至特异群发
    msend_loc=("xpath","//span[contains(text(),'群发消息')]")#定位至群发消息

    def main(self):
        log.info("begin grant coupon page")
        self.click(GrantCouponPage.collector_tools_loc)#点击“集客工具”
        self.click(GrantCouponPage.coupon_loc)#点击优惠券
        self.click(GrantCouponPage.grant_loc)#点击发放
        self.click(GrantCouponPage.wechat_grant_loc)#点击微信发放
        self.click(GrantCouponPage.peculiar_msend_loc)#点击特异群发
        self.click(GrantCouponPage.msend_loc)#点击群发消息
        log.info("end grant coupon page")


