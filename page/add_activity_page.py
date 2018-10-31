#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class AddActivity(Base):

    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    act_tab_loc=("xpath","//*[contains(@ui-sref,'market.mobileTemplate')]")#定位“活动模板”
    add_template=("xpath","//*[contains(@class,'text-gray')]")#定位“添加模板”
    #confirm_btn=("xpath","//*[contains(@class,'btn-primary')]:nth-child(1)")
    confirm_btn=("xpath","/html/body/div[1]/div/div/div/div/buttoncell[2]/div/a/span")#定位弹出框中的确认按钮
    act_name=("xpath","//input[@type='text'and @placeholder='请输入活动名称']")#定位活动名称输入框
    trigger_keys=("xpath","//input[@type='text'and @placeholder='关键字']")#定位触发关键字输入框
    cover_pic_loc=("xpath","//input[@type='file' and @name='weChatCoverUrl']")#定位封面图片上传按钮
    theme_pic_loc=("xpath","//input[@type='file' and @name='activeCoverUrl']")#定位主题配图上传按钮
    act_stime_loc=("xpath","//input[@placeholder='开始时间']")#定位活动时间开始时间输入框
    act_etime_loc=("xpath","//input[@placeholder='结束时间']")#定位活动时间结束时间输入框
    enroll_etime_loc=("xpath","//input[@placeholder='请选择日期']")#定位活动时间结束时间输入框
    pay_money_loc=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/gather-activity-detail/div/div/div/form/div/div[5]/div/inputcell[1]/div/div/div[2]/input")#定位支付金额输入框
    pay_reason_loc=("xpath","//input[@placeholder='如：支付预定金1000,购车可抵现金3000']")#定位输入支付理由输入框
    act_dot_loc=("xpath","//div[@class='inline-block pointer']")#定位添加活动亮点按钮
    add_act_dot=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/gather-activity-detail/div/div/div/form/div/div[6]/div[1]/div[2]/editcell[1]/div/inputcell/div/div/div[2]/input")#定位亮点输入框
    share_abstract_loc=("xpath","//input[@placeholder='微信分享时图文消息的摘要']")#定位分享摘要输入框
    save_loc=("xpath","//buttoncell[@class='inline-block ng-scope ng-isolate-scope']")#定位保存按钮
    sure_loc=("xpath","//a[contains(@class, 'btn-danger')]")#定位弹出框中的确定按钮
    next_loc = ("xpath", "//span[contains(text(),'下一步')]")#定位下一步按钮
    #next_loc=("xpath","//div[@class='inline-block pointer']")#定位下一步按钮
    input_phone_loc=("xpath","//textarea[@placeholder='手动输入号码请用英文逗号或换行分隔。']")#定位号码输入框
    send_loc=("xpath","//buttoncell[@class='ml-20 inline-block ng-scope ng-isolate-scope' and @ng-click='$ctrl.goSend()']")#定位发送按钮


    def main(self,name,keys,cover_path,theme_path,stime,etime,eetime,money,reason,dot,s_abstract,tphone):

        log.info('begin add activity')
        self.click(AddActivity.qfzs_tab_loc)#点击群发助手
        time.sleep(2)
        self.click(AddActivity.act_tab_loc)#点击活动模板
        time.sleep(2)
        self.click(AddActivity.add_template)#点击添加模板
        time.sleep(5)
        self.click(AddActivity.confirm_btn)#点击活动类型弹出框的【确认】
        time.sleep(2)
        self.sendKeys(AddActivity.act_name,name)#输入活动名称
        time.sleep(2)
        self.sendKeys(AddActivity.trigger_keys,keys)#输入触发关键字
        time.sleep(2)
        self.sendKeys(AddActivity.cover_pic_loc,cover_path)#上传封面图片
        time.sleep(2)
        self.sendKeys(AddActivity.theme_pic_loc,theme_path)#上传主题配图
        time.sleep(2)
        self.sendKeys(AddActivity.act_stime_loc,stime)#填写活动开始时间
        time.sleep(2)
        self.sendKeys(AddActivity.act_etime_loc,etime)#填写活动结束时间
        time.sleep(2)
        self.sendKeys(AddActivity.enroll_etime_loc,eetime)#填写报名截止时间
        time.sleep(5)
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
        time.sleep(2)
        self.sendKeys(AddActivity.pay_money_loc,money)#输入支付金额
        time.sleep(2)
        self.sendKeys(AddActivity.pay_reason_loc,reason)#输入支付理由
        time.sleep(2)
        self.click(AddActivity.act_dot_loc)#点击添加活动亮点
        time.sleep(2)
        self.sendKeys(AddActivity.add_act_dot,dot)#输入活动亮点
        time.sleep(2)
        self.sendKeys(AddActivity.share_abstract_loc,s_abstract)#输入分享摘要
        time.sleep(2)
        self.click(AddActivity.save_loc)#点击保存
        time.sleep(5)
        self.click(AddActivity.sure_loc)#点击确定
        time.sleep(5)
        self.click(AddActivity.next_loc)#点击下一步
        time.sleep(2)
        self.click(AddActivity.input_phone_loc,tphone)#输入号码
        time.sleep(2)
        self.click(AddActivity.send_loc)#点击发送按钮

        log.info('end activity page')



