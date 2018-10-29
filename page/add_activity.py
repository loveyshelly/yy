#coding=utf-8

from common.base import Base
from selenium import webdriver

class AddActivity(Base):

    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    act_tab_loc=("xpath","//*[@id='app']/div/div/market/layout/div/div/layout-body/main/aside/subnav/section/div[1]/div[3]/a/span")#定位“活动模板”
    add_template=("xpath","//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/mobile-template/div/h5-template/div/div[2]/div[2]/div[1]/mobile-template-view[2]/div/div")#定位“添加模板”
    confirm_btn=("xpath","/html/body/div[1]/div/div/div/div/buttoncell[2]/div/a/span")
    act_name=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/gather-activity-detail/div/div/div/form/div/editcell[2]/div/inputcell/div/div/div[2]/input")#定位活动名称输入框
    trigger_keys=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/gather-activity-detail/div/div/div/form/div/editcell[4]/div/inputcell/div/div/div[2]/input")#定位触发关键字输入框
    cover_pic_loc=("xpath","//*[@id='app']/div/div/jike/layout/div/div/layout-body/main/section/div/gather-activity-detail/div/div/div/form/div/image-upload[1]/div/div/div[2]/div[1]/input")#定位封面图片上传按钮