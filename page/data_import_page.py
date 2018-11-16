#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log



class DataImportPage(Base):
    data_import_loc = ("xpath", "//*[@id='step1']/div[7]/a/span")  # 定位“数据导入”
    upload_user_loc=("xpath","//div[contains(text(),'上传数据表')]")#定位车主数据——上传数据表
    start_importu_loc=("xpath","//span[text()='开始导入']")#定位开始导入-车主数据
    car_data_loc=("xpath","//a[@ui-sref='sync.carData']")#定位车辆数据页面
    upload_car_loc = ("xpath", "//div[contains(text(),'上传数据表')]")  # 定位车辆数据——上传数据表
    start_importc_loc = ("xpath", "//span[text()='开始导入']")#定位开始导入-车辆
    maintenance_data_loc = ("xpath", "//a[@ui-sref='sync.maintenanceData']")  # 定位维保数据页面
    upload_maintenance_loc = ("xpath", "//div[contains(text(),'上传数据表')]")  # 定位维保数据——上传数据表
    start_importm_loc = ("xpath", "//span[text()='开始导入']")  # 定位开始导入-维保
    renewal_data_loc = ("xpath", "//a[@ui-sref='sync.renewalData']")  # 定位续保数据页面
    upload_renewal_loc = ("xpath", "//div[contains(text(),'上传数据表')]")  # 定位续保数据——上传数据表
    start_importr_loc = ("xpath", "//span[text()='开始导入']")  # 定位开始导入-续保


    def main(self,userdata,cardata,maintenancedata,renewaldata):
        log.info("begin data_import page")
        self.click(DataImportPage.data_import_loc)#点击“数据导入”
        time.sleep(2)
        self.upload(DataImportPage.upload_user_loc,userdata)#上传车主数据
        time.sleep(5)
        self.click(DataImportPage.start_importu_loc)#点击【开始导入】
        time.sleep(5)
        self.click(DataImportPage.car_data_loc)#点击“车辆数据”
        self.upload(DataImportPage.upload_car_loc,cardata)#上传车辆数据
        time.sleep(5)
        self.click(DataImportPage.start_importc_loc)#点击【开始导入】
        time.sleep(5)
        self.click(DataImportPage.maintenance_data_loc)#点击“维保数据”
        self.upload(DataImportPage.upload_maintenance_loc,maintenancedata)#上传维保数据
        time.sleep(5)
        self.click(DataImportPage.start_importm_loc)#点击【开始导入】
        time.sleep(5)
        self.click(DataImportPage.renewal_data_loc)#点击“续保数据”
        self.upload(DataImportPage.upload_renewal_loc,renewaldata)#上传续保数据
        time.sleep(5)
        self.click(DataImportPage.start_importm_loc)  # 点击【开始导入】
        log.info("end data_import page")




