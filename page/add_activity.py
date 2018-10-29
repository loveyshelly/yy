#coding=utf-8

from common.base import Base
from selenium import webdriver

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
    act_stime_loc=("xpath","//button[@type='button' and @class='btn btn-default' and @ng-click='$ctrl.openStart()']")#定位活动时间开始时间输入框
    act_etime_loc = ("xpath", "//button[@type='button' and @class='btn btn-default' and @ng-click='$ctrl.openEnd()']")#定位活动时间结束时间输入框
    enroll_etime_loc=("xpath","//button[@type='button' and @class='btn btn-default txt-right' and @ng-click='$ctrl.openStart()']")#定位活动时间结束时间输入框
    pay_money_loc=("xpath","//input[@class='ng-pristine ng-valid ng-empty ng-valid-maxlength ng-touched']")#定位支付金额输入框
    pay_reason_loc=("xpath","//input[@placeholder='如：支付预定金1000,购车可抵现金3000']")#定位输入支付理由输入框
    act_dot_loc=("xpath","//div[@class='inline-block pointer']")#定位添加活动亮点按钮
    add_act_dot=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/gather-activity-detail/div/div/div/form/div/div[6]/div[1]/div[2]/editcell[1]/div/inputcell/div/div/div[2]/input")#定位亮点输入框
    share_abstract_loc=("xpath","//input[@placeholder='微信分享时图文消息的摘要']")#定位分享摘要输入框
    save_loc=("xpath","//buttoncell[@class='inline-block ng-scope ng-isolate-scope']")#定位保存按钮