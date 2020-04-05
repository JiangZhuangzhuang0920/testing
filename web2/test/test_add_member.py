from time import sleep

from web2.page.index import Index


class TestAddMember:

    def setup(self):
        self.index = Index()

    def test_add_member(self):
        #能拆开是因为 goto_add_member是实例化AddMember类
        addmember=self.index.goto_add_member()
        addmember.add_member()
        a=addmember.get_first()
        assert a=="abc"
        addmember.delet_member()



