'''
父亲类，放一些共用方法
'''

from selenium import webdriver

class BasePage:

    _base_url=""

    def __init__(self,driver:webdriver=None):


        if driver is None:
            #是None，说明是第一次调用，需要第一次实例化子类
            self.driver= webdriver.Chrome()
        else:
            #不为None说明不是第一次实例化，
            self.driver=driver
        if self._base_url !="":
            self.driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)
