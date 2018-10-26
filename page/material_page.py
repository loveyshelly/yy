#-*- coding: UTF-8 -*-.
from selenium.webdriver.common.keys import Keys

from common.base import Base
from common.logger import logger as log
import time


class MaterialPage(Base):
    #页面元素定位
    article_tab_loc=("xpath","//*[contains(@ui-sref,'market') and contains(@ui-sref-active, 'active')][1]")#群发助手
    article_button_loc=("xpath","//*[contains(@ui-sref,'market.material')]/span[1]")#素材管理
    article_button_new_loc=("xpath","//a[contains(@class, 'btn-primary')]/span[1]")#新建图文消息
    article_title_loc=("xpath","//div[contains(@class,'material-title')]/input[1]")#标题
    article_author_loc=("xpath","//div[contains(@class,'material-author')]/input[1]")#作者名称
    article_abstract_loc=("xpath","//div[contains(@class,'material-abstract')]/div/textarea[1]")#摘要
    article_picture_loc=("xpath","//image-upload[1]")#图片
    article_content_loc=("xpath","//textarea[@id='ueditor_textarea_editorValue']")#内容
    article_save_loc=("xpath","//*[@id='step1']/div[2]/a/span")#save

    def main(self, title, author, abstract, content, picture_path='olof.jpeg'):
        log.info('begin material page')
        self.click(MaterialPage.article_tab_loc)
        time.sleep(1)
        self.click(MaterialPage.article_button_loc)
        time.sleep(1)
        self.click(MaterialPage.article_button_new_loc)
        time.sleep(1)
        self.sendKeys(MaterialPage.article_title_loc, title)
        self.sendKeys(MaterialPage.article_author_loc, author)
        self.inputTextArea(MaterialPage.article_abstract_loc, abstract)

        self.inputTextArea(None, content)


        self.click(MaterialPage.article_save_loc)
        log.info('end material page')
        pass






