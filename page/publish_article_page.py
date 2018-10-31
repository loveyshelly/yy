#coding=utf-8

import time
from common.base import Base
from common.logger import logger as log

class PublishArticlePage(Base):
    qfzs_tab_loc = ("xpath", "//*[@id='step1']/div[2]/a/span")  # 定位“群发助手”
    pub_list_loc=("xpath","//a[@class='subnav-hotspot'and @href='/market/promotion']")#定位发布文章菜单
    pub_btn_loc=("xpath","//a[@ng-href='/market/promotion/add']")#定位发布文章按钮
    title_loc=("xpath","//inputcell[@class='col-lg-10 ng-isolate-scope']")#定位文章标题输入框
    cover_loc=("xpath","//input[@name='imageUpload']")#定位封面图片上传按钮
    content_loc=("xpath","//body[@class='view']")#定位文章内容文本框
    save_loc=("xpath","//span[contains(text(),'保存')]")

    def main(self,title,coverpath,content):
        log.info("begin article page")
        self.click(PublishArticlePage.qfzs_tab_loc)#点击群发助手
        time.sleep(5)
        self.click(PublishArticlePage.pub_list_loc)#点击发布文章菜单
        self.click(PublishArticlePage.pub_btn_loc)#点击发布文章按钮
        self.sendKeys(PublishArticlePage.title_loc,title)#输入文章标题
        self.sendKeys(PublishArticlePage.cover_loc,coverpath)#上传封面图片
        self.sendKeys(PublishArticlePage.content_loc,content)#输入文章内容
        self.click(PublishArticlePage.save_loc)#点击保存
        log.info("end article page")



