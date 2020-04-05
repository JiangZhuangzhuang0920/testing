from web.page.main import Main


class TestRigister:
    def setup(self):
        #进入到首页
        self.main=Main()

    def test_register(self):
        assert self.main.goto_register().register()