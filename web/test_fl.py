from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testfl():
    def setup(self):
        self.driver = webdriver.Chrome()
        #全局的隐式等待（默认0.5s轮循环，找不到抛出异常）
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_one(self):
        self.driver.get(url="http://caixian.mypicc.com.cn/")
        #直接等待
        sleep(3)
        ele_bx=self.driver.find_element_by_xpath('//*[@id="navList"]//li[2]')
        ele_bx.click()

        #创建一个方法，判断是否找到想等待的元素 wait(x)中x必写，即使不用，因为until调用需要参数
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@id="mainFormMall"]//div[5]'))>0
        #显性等待,传参不用写wait(),wait()是调用，不是传参
        WebDriverWait(self.driver,10).until(wait)
        ele_lc = self.driver.find_element_by_xpath('//*[@id="navList"]//li[3]')
        ele_lc.click()
        #显性等待用自带的方法
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="navList"]//li[3]')))