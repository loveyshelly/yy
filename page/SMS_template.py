#-*- coding: UTF-8 -*-.
from common.base import Base

class SMStemplate(Base):
    #页面元素定位
    qfzs_tab_loc=("xpath","//*[@id='step1']/div[2]/a/span")#“群发助手”
    sms_tab_loc=("xpath","//*[@id='app']/div/div/market/layout/div/div/layout-body/main/aside/subnav/section/div[1]/div[3]/a/span")#“短信模板”
    new_btn_loc=("xpath","//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/message-template/sms-template/div/div[2]/div/datatable/div/div[1]/div/div[1]/datatable-tools/buttoncell[1]/div/a")#【新增】
    sele_tag_loc=("xpath","/html/body/div[1]/div/div/edit-message-template/div/div[1]/tags/div/div[2]/div[5]/span")#“活动”标签
    tem_title_loc=("xpath","/html/body/div[1]/div/div/edit-message-template/div/div[3]/inputcell/div/div/div[2]/input")#“模板名称”输入框
    tem_detail=("xpath","//*[@id='msgArea']/div/div/div[2]/textarea")#“模板内容”输入框
    confirm_loc=("xpath","/html/body/div[1]/div/div/edit-message-template/div/div[4]/buttoncell[1]/div/a")#确定
    page_index=("xpath","//*[@id='app']/div/div/market/layout/div/div/layout-body/main/section/div/message-template/sms-template/div/div[2]/div/datatable/div/div[1]/div/div[2]/span/selectcell/div/div/div/div/a/span[3]/b")#每页显示数量下拉框
    page_number=("xpath","//*[@id='ui-select-choices-row-0-1']/div/div")#每页显示50条
    tem_title=("xpath","//*[@id='1540432644100-30-uiGrid-0007-cell']/div")#列表中标题

    def click_qfzs_tab(self):
        self.click(self.qfzs_tab_loc)#点击“群发助手”

    def click_sms_tab(self):
        self.click(self.sms_tab_loc)#点击“短信模板”

    def click_new_btn(self):
        self.click(self.new_btn_loc)#点击“新增”

    def click_sele_tag(self):
        self.driver.switch_to_window
        self.click(self.sele_tag_loc)#选中“活动”标签

    def input_tem_title(self,text):

        self.sendKeys(self.tem_title_loc,text)#输入模板名称

    def input_tem_detail(self,text):
        self.driver.switch_to_window#将焦点定位于弹出框
        self.sendKeys(self.tem_detail,text)#输入模板内容

    def click_confirm(self):
        self.driver.switch_to_window#将焦点定位于弹出框
        self.click(self.confirm_loc)#点击【确定】

    def click_page_index(self):
        self.click(self.page_index)#点击每页显示条数下拉框

    def click_page_number(self):
        self.click(self.page_number)#选择"50",每页显示50条

    def get_tem_title(self):
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
        '''获取标题'''
        try:
            t=self.findElement(self.tem_title).text
            return t
        except:
            return "获取失败，返回空"





