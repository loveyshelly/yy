#coding=utf-8

from common.logger import logger as log
from common.base import Base
import time

class BuyEnquiryAllotPage(Base):
    businessConsult_loc=("xpath","//span[contains(text(),'业务咨询')]")#定位“业务咨询”
    businessclue_loc=("xpath", "//span[contains(text(),'业务线索')]")#定位“业务线索”
    buyEnquiry_loc=("xpath", "//span[contains(text(),'购车询价')]")#定位“购车询价”
    input_key_loc = ("xpath", "//input[@placeholder='姓名、电话']")#定位至关键字查询搜索框
    query_loc=("xpath", "//a[@class='btn-primary']")#定位查询按钮
    select_loc=("xpath","//div[@class='ui-grid-selection-row-header-buttons ui-grid-icon-ok ng-scope ui-grid-row-selected']")#定位勾选框
    allot_loc=("xpath","//span[contains(text(),'分配')]")#定位分配按钮
    select_sales=("xpath","//div[contains(text(),'xiaoli')]")#定位至销售顾问选择下拉列表
    save_loc=("xpath","//span[contains(text(),'保存')]")#定位保存按钮

    def main(self,customer_key):
        log.info("begin buyEnquiry allot page")
        self.click(BuyEnquiryAllotPage.businessConsult_loc)#点击业务咨询
        self.click(BuyEnquiryAllotPage.businessclue_loc)#点击业务线索
        self.click(BuyEnquiryAllotPage.buyEnquiry_loc)#点击购车询价
        self.sendKeys(BuyEnquiryAllotPage.input_key_loc,customer_key)#输入关键字
        self.click(BuyEnquiryAllotPage.query_loc)#点击查询按钮
        self.click(BuyEnquiryAllotPage.select_loc)
        self.click(BuyEnquiryAllotPage.allot_loc)#点击分配按钮
        self.click(BuyEnquiryAllotPage.select_sales)#选择销售顾问
        self.click(BuyEnquiryAllotPage.save_loc)#点击保存按钮
        log.info("end buyEnquiry allot page")




