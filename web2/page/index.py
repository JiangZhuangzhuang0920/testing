from time import sleep

from selenium.webdriver.common.by import By
from web2.page.base_page import BasePage
from web2.page.add_menber import AddMember


class Index(BasePage):
    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        self.driver.find_element(By.XPATH,'//span[@class="ww_indexImg ww_indexImg_AddMember"]').click()
        return AddMember(self.driver)

    def goto_impot_member(self):
        pass
    def goto_member_jion(self):
        pass