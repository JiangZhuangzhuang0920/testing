from selenium import webdriver

class BasePage:
    def __init__(self,driver:webdriver=None):

        #放在分支里面，python编译器无法确定是否声明变量，因此入参driver指定类型为webdriver并实例为None
        if driver is None:
            #登陆后的页面，需要复用浏览器
            opts = webdriver.ChromeOptions()
            opts.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=opts)
        else:
            self.driver=driver