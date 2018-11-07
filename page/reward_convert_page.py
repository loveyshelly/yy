#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class RewardConvertPage(Base):
    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    reward_convert_loc=("xpath", "//span[contains(text(),'奖励兑换') and @class='ng-binding ng-scope']")#定位奖励兑换菜单
    active_convert_loc=("xpath","//span[contains(text(),'活动奖励兑换')]")#定位活动奖励兑换
    input_convert_num=("xpath","//input[@placeholder='请输入兑换码']")#定位兑换码输入框
    convert_loc=("xpath","//span[contains(text(),'兑换') and @class='ng-scope']")#定位兑换按钮

    def main(self,convertnum):
        log.info("begin reward convert page")
        self.click(RewardConvertPage.qfzs_tab_loc)#点击群发助手
        time.sleep(2)
        self.click(RewardConvertPage.reward_convert_loc)#点击奖励兑换
        self.sendKeys(RewardConvertPage.input_convert_num,convertnum)#输入兑换码
        self.click(RewardConvertPage.convert_loc)#点击兑换
        log.info("end reward convert page")
        

