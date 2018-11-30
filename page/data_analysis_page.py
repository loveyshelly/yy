#coding=utf-8

from common.base import Base
from common.logger import logger as log
import time

class DataAnalysisPage(Base):
    collector_tools_loc = ("xpath","//*[@id='step1']/div[3]/a/span")# 定位“集客工具”
    collector_enroll_loc=("xpath","//span[contains(text(),'集客报名')]")#定位至集客报名
    data_analysis_loc=("xpath","//span[contains(text(),'数据分析')]")#定位至数据分析
    export_loc=("xpath","//span[contains(text(),'导出')]")#定位至导出
    download_loc=("xpath","//i[@class='glyphicon glyphicon-cloud-download']")#定位至下载导出文件

    def main(self):
        log.info("begin data analysis page")
        time.sleep(5)
        self.click(DataAnalysisPage.collector_tools_loc)#点击集客工具
        self.click(DataAnalysisPage.collector_enroll_loc)#点击集客报名
        self.click(DataAnalysisPage.data_analysis_loc)#点击数据分析
        time.sleep(2)
        self.click(DataAnalysisPage.export_loc)#点击导出
        time.sleep(10)
        self.click(DataAnalysisPage.download_loc)#点击下载导出文件
        log.info("end data analysis page")
