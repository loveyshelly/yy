#-*- coding: UTF-8 -*-.
from selenium.webdriver.common.keys import Keys

from common.base import Base
from common.logger import logger as log
import time
from selenium import webdriver



class MaterialPage(Base):
    #页面元素定位
    profileDir = r'E:\work\qd_testing\test_data\pictures'
    profile = webdriver.FirefoxProfile(profileDir)
    driver = webdriver.Firefox(profile)
    article_tab_loc=("xpath","//*[contains(@ui-sref,'market') and contains(@ui-sref-active, 'active')][1]")#群发助手
    article_button_loc=("xpath","//*[contains(@ui-sref,'market.material')]/span[1]")#素材管理
    article_button_new_loc=("xpath","//a[contains(@class, 'btn-primary')]/span[1]")#新建图文消息
    article_title_loc=("xpath","//div[contains(@class,'material-title')]/input[1]")#标题
    article_author_loc=("xpath","//div[contains(@class,'material-author')]/input[1]")#作者名称
    article_abstract_loc=("xpath","//div[contains(@class,'material-abstract')]/div/textarea[1]")#摘要
    article_picture_loc = ("xpath", "//*[text()='上传图片']")
    #article_picture_loc=("xpath","//div[contains(@class, 'image-upload-button')]/input[1]")#图片
    article_content_loc=("xpath","//textarea[@id='ueditor_textarea_editorValue']")#内容
    article_save_loc=("xpath","//a/span[text()='保存素材'][1]")#save
    #/html/body/app/div/div/market/layout/div/div/layout-body/main/section/div/material-edit/div/div[2]/buttoncell[1]/div/a
    path="E://work/qd_testing/test_data/pictures/audi.jpg"


    def main(self, title, author, abstract, content, picture_path='olof.jpeg'):
        log.info('begin material page')
        self.click(MaterialPage.article_tab_loc)
        time.sleep(2)
        self.click(MaterialPage.article_button_loc)
        time.sleep(2)
        self.click(MaterialPage.article_button_new_loc)
        time.sleep(2)
        self.sendKeys(MaterialPage.article_title_loc, title)
        time.sleep(2)
        self.sendKeys(MaterialPage.article_author_loc, author)
        time.sleep(2)
        self.inputTextArea(MaterialPage.article_abstract_loc, abstract)
        time.sleep(2)
        self.upload(MaterialPage.article_picture_loc, MaterialPage.path)
        time.sleep(2)
        self.inputTextArea(None, content)
        #保存素材
        self.click(MaterialPage.article_save_loc)
        log.info('end material page')
        pass






