#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log


class PublishArticlePage(Base):

    qfzs_tab_loc = ("xpath", "//*[contains(@ui-sref,'market') and contains(@ui-sref-active, 'active')][1]")  # 定位“群发助手”
    pub_list_loc=("xpath","//a[@class='subnav-hotspot'and @href='/market/promotion']")#定位发布文章菜单
    pub_btn_loc=("xpath","//span[contains(text(),'发布文章')and @class='ng-scope']")#定位发布文章按钮
    title_loc = ("xpath", "//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/promotion-add/div/div[1]/form/promotion-article/div/div[1]/inputcell/div/div/div[2]/input")  # 定位文章标题输入框
    #title_loc=("xpath","//inputcell[@class='col-lg-10 ng-isolate-scope']")#定位文章标题输入框
    cover_loc=("xpath","//input[@name='imageUpload']")#定位封面图片上传按钮
    #content_loc=("xpath","//textarea[@id='ueditor_textarea_editorValue']")
    content_loc=("xpath","//iframe[@id='ueditor_1']")#定位文章内容文本框
    save_loc=("xpath","//span[contains(text(),'保存')]")

    def main(self,title,coverpath,acontent):
        log.info("begin article page")
        self.click(PublishArticlePage.qfzs_tab_loc)#点击群发助手
        time.sleep(5)
        self.click(PublishArticlePage.pub_list_loc)#点击发布文章菜单
        time.sleep(2)
        self.click(PublishArticlePage.pub_btn_loc)#点击发布文章按钮
        time.sleep(5)
        self.sendKeys(PublishArticlePage.title_loc,title)#输入文章标题
        time.sleep(2)
        self.sendKeys(PublishArticlePage.cover_loc,coverpath)#上传封面图片
        time.sleep(10)
        #js1 = "document.documentElement.scrollTop=10000"
        #self.driver.execute_script(js1)
        #self.driver.switch_to_frame(PublishArticlePage.content_loc)
        self.inputTextArea(None, acontent)
        #self.sendKeys(PublishArticlePage.content_loc,acontent)#输入文章内容
        time.sleep(2)
        self.click(PublishArticlePage.save_loc)#点击保存
        log.info("end article page")



