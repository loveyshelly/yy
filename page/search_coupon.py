#coding=utf-8

from common.logger import logger as log
from common.base import Base
import time


class SearchCoupon(Base):
    collector_tools_loc=("xpath","//a[@ui-sref='jike']")#定位“集客工具”
    coupon_loc=("xpath","//span[contains(text(),'优惠券')]")#定位至优惠券菜单
    grant_loc=("xpath","//a[@ui-sref='jike.couponGrant']")#定位至发放
    input_coupon_name=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/coupon-grant/div/div/form/div[1]/inputcell/div/div/div[2]/input")#定位搜索框
    search_loc=("xpath","//i[@class='iconfont icon-search ng-scope']")#定位查询按钮

    def search(self,name="双12五折券"):
        log.info("begin grant coupon page")
        self.click(SearchCoupon.collector_tools_loc)#点击“集客工具”
        self.click(SearchCoupon.coupon_loc)#点击优惠券
        self.click(SearchCoupon.grant_loc)#点击发放
        time.sleep(2)
        self.sendKeys(SearchCoupon.input_coupon_name,name)#输入关键字
        time.sleep(2)
        self.click(SearchCoupon.search_loc)#点击查询
        log.info("begin grant coupon page")








