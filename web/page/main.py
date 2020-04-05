'''
主页面两个功能： 企业登录/注册入口
'''
from selenium.webdriver.common.by import By
from web.page.base_page import BasePage
from web.page.login import Login
from web.page.register import Register


class Main(BasePage):

    def goto_register(self):
        base_url = "https://work.weixin.qq.com/"
        #点击立即注册按钮进入到注册页
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)


    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        #return Login(self,_driver)
        pass