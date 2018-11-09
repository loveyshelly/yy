#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class DrawRecordsPage(Base):
    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    reward_convert_loc = ("xpath", "//span[contains(text(),'奖励兑换') and @class='ng-binding ng-scope']")  # 定位奖励兑换菜单
    draw_records_loc=("xpath","//span[contains(text(),'领取记录')]")#定位兑换记录
    export_loc=("xpath","//span[contains(text(),'导出')]")#定位导出

    def main(self):
        self.click(DrawRecordsPage.qfzs_tab_loc)#点击“群发助手”
        time.sleep(5)
        self.click(DrawRecordsPage.reward_convert_loc)#点击奖励兑换菜单
        self.click(DrawRecordsPage.draw_records_loc)#点击领取记录菜单
        self.click(DrawRecordsPage.export_loc)#点击导出按钮

