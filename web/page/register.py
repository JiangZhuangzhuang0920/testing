'''
对注册页面进行建模
'''
from selenium.webdriver.common.by import By

from web.page.base_page import BasePage


class Register(BasePage):
    #填写表单
    def register(self):
        #定位元素并操作元素的操作细节
        self.find(By.ID,"corp_name").send_keys("hello")
        self.find(By.ID, "manager_name").send_keys("hello2")