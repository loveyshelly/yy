#coding=utf-8

from common.logger import logger
from common.base import Base
import time

class BuyEnquiryExportPage(Base):
    businessConsult_loc=("xpath", "//span[contains(text(),'业务咨询')]")# 定位“业务咨询”
    businessclue_loc=("xpath", "//span[contains(text(),'业务线索')]")# 定位“业务线索”
    buyEnquiry_loc=("xpath", "//span[contains(text(),'购车询价')]")#定位“购车询价”
    export_loc = ("xpath", "//span[contains(text(),'导出')]")  # 定位至导出

    def main(self):
        self.click(BuyEnquiryExportPage.businessConsult_loc)#点击业务咨询
        self.click(BuyEnquiryExportPage.businessclue_loc)#点击业务线索
        self.click(BuyEnquiryExportPage.buyEnquiry_loc)#点击购车询价
        time.sleep(5)
        self.click(BuyEnquiryExportPage.export_loc)#点击导出




