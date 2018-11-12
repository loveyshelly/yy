#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class ConvertRecordspage(Base):
    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    reward_convert_loc = ("xpath", "//span[contains(text(),'奖励兑换') and @class='ng-binding ng-scope']")  # 定位奖励兑换菜单
    covert_records_loc=("xpath","//span[contains(text(),'兑换记录')]")#定位兑换记录
    export_loc=("xpath","//span[contains(text(),'导出')]")#定位导出
    download_loc=("xpath","//a[@class='inline-block file-export-master text-primary ng-scope']")#定位下载导出文件


    def main(self):
        self.click(ConvertRecordspage.qfzs_tab_loc)#点击“群发助手”
        time.sleep(5)
        self.click(ConvertRecordspage.reward_convert_loc)#点击奖励兑换菜单
        self.click(ConvertRecordspage.covert_records_loc)#点击兑换记录菜单
        self.click(ConvertRecordspage.export_loc)#点击导出按钮
        self.click(ConvertRecordspage.download_loc)#点击下载导出文件