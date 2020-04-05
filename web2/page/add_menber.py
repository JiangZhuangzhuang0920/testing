from time import sleep

from selenium.webdriver.common.by import By
from web2.page.base_page import BasePage


class AddMember(BasePage):
    #添加成员页面输入内容并保存
    def add_member(self):
        sleep(3)
        self.driver.find_element_by_id("username").send_keys("abc")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("abc")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13333333333")
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        sleep(3)
    def get_first(self):
        xxx = self.driver.find_element(By.XPATH,'//*[@id="member_list"]/tr[1]/td[2]').get_attribute("title")
        return  xxx
    def delet_member(self):
        self.driver.find_element(By.XPATH,'//*[@id="member_list"]/tr[1]/td[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_delete").click()
        self.driver.find_element(By.XPATH, '//a[@d_ck="submit"]').click()