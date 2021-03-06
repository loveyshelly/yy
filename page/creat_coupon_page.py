#coding=utf-8

from common.logger import logger as log
from common.base import Base
import time

class CreatCouponPage(Base):
    collector_tools_loc=("xpath","//a[@ui-sref='jike']")#定位“集客工具”
    coupon_loc=("xpath","//span[contains(text(),'优惠券')]")#定位至优惠券菜单
    creat_loc=("xpath","//a[@class='subnav-hotspot' and @ui-sref='jike.coupon']")#定位至创建
    new_coupon_loc=("xpath","//span[contains(text(),'新增优惠券')]")#定位至新增优惠券按钮
    input_coupon_name=("xpath","//input[contains(@placeholder,'名称长度')]")#定位优惠券名称输入框
    input_money=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/coupon-detail/div/div[2]/div/form/div/editcell[5]/div/inputcell/div/div/div[2]/input")#定位金额输入框
    live_time=("xpath","//input[@placeholder='请选择日期']")#定位使用期限输入框
    coupon_introduction=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/coupon-detail/div/div[2]/div/form/div/editcell[6]/div/inputcell/div/div/div[2]/input")#定位至优惠说明输入框
    use_notice = ("xpath", "//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/coupon-detail/div/div[2]/div/form/div/editcell[7]/div/textarea-cell/div/div/div[2]/textarea")  # 定位使用须知文本框
    #use_notice=("xpath","(//textarea[@ng-model='$ctrl.value'])[0]")#定位使用须知文本框
    input_num=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/coupon-detail/div/div[2]/div/form/div/editcell[8]/div/inputcell/div/div/div[2]/input")#定位数量输入框
    apply_instruction=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/coupon-detail/div/div[2]/div/form/div/editcell[12]/div/textarea-cell/div/div/div[2]/textarea")#定位申请说明输入框
    save_loc=("xpath","//span[contains(text(),'保存并提交审核')]")#定位保存并提交审核
    sure_loc=("xpath","//span[contains(text(),'确定')]")#定位确定

    def main(self,coupon_name,money,liveTime,introductions,notices,number,instructions):
        log.info("begin creat coupon page")
        self.click(CreatCouponPage.collector_tools_loc)#点击“集客工具”
        self.click(CreatCouponPage.coupon_loc)#点击优惠券菜单
        time.sleep(5)
        self.click(CreatCouponPage.creat_loc)#点击创建
        time.sleep(5)
        self.click(CreatCouponPage.new_coupon_loc)#点击新增优惠券按钮
        time.sleep(5)
        self.sendKeys(CreatCouponPage.input_coupon_name,coupon_name)#输入优惠券名称
        time.sleep(2)
        self.sendKeys(CreatCouponPage.input_money,money)#输入金额
        time.sleep(2)
        self.sendKeys(CreatCouponPage.live_time,liveTime)#输入到期日
        time.sleep(2)
        js1 = "document.documentElement.scrollTop=5000"
        self.driver.execute_script(js1)
        self.sendKeys(CreatCouponPage.coupon_introduction,introductions)#输入优惠说明
        time.sleep(2)
        self.sendKeys(CreatCouponPage.use_notice,notices)#输入使用须知
        time.sleep(2)
        self.sendKeys(CreatCouponPage.input_num,number)#输入数量
        self.sendKeys(CreatCouponPage.apply_instruction,instructions)#输入申请说明
        self.click(CreatCouponPage.save_loc)#保存并提交审核
        time.sleep(2)
        self.click(CreatCouponPage.sure_loc)#确定
        log.info("end creat coupon page")

