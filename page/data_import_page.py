#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log



class DataImportPage(Base):
    data_import_loc = ("xpath", "//*[@id='step1']/div[7]/a/span")  # 定位“数据导入”
    upload_user_loc=("xpath","//input[@id='txt_upload']")#定位车主数据——上传数据表
    start_import_loc=("xpath","//span[text()='开始导入']")
    #car_data_loc=("xpath","//*[@id='app']/div/div/sync/layout/div/div/layout-body/main/aside/subnav/section/div[1]/div[3]/a/span")#定位车辆数据页面
    #upload_car_loc = ("xpath", "//input[@id='txt_upload']")  # 定位车辆数据——上传数据表


    def main(self,userdata):
        log.info("begin data_import page")
        self.click(DataImportPage.data_import_loc)#点击“数据导入”
        time.sleep(2)
        self.upload(DataImportPage.upload_user_loc,DataImportPage.userdata)#上传车主数据
        time.sleep(10)
        self.click(DataImportPage.start_import_loc)#点击开始导入
        time.sleep(10)
        log.info("end data_import page")




