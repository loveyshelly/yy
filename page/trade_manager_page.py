#coding=utf-8

from common.base import Base
from common.logger import logger as log
import time

class TradeManagerPage(Base):
    collector_tools_loc = ("xpath","//*[@id='step1']/div[3]/a/span")# 定位“集客工具”
    collector_enroll_loc=("xpath","//span[contains(text(),'集客报名')]")#定位至集客报名
    trade_manager_loc=("xpath","//span[contains(text(),'交易管理')]")#定位至交易管理
    export_loc=("xpath","//span[contains(text(),'导出')]")#定位至导出
    download_loc=("xpath","//i[@class='glyphicon glyphicon-cloud-download']")#定位至下载导出文件

    def main(self):
        log.info("begin trade manager page")
        time.sleep(5)
        self.click(TradeManagerPage.collector_tools_loc)#点击集客工具
        self.click(TradeManagerPage.collector_enroll_loc)#点击集客报名
        self.click(TradeManagerPage.trade_manager_loc)#点击交易管理
        time.sleep(2)
        self.click(TradeManagerPage.export_loc)#点击导出
        time.sleep(10)
        self.click(TradeManagerPage.download_loc)#点击下载导出文件
        log.info("end trade manager page")
