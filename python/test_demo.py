import pytest
from python import demo

class Test_yunsuan:
    """
        一个正一个负
        两个正数
        两个负数
        两个0
        一个0和正数
        一个0和负数
        一个整数一个小数
        两个小数
    """

    @pytest.mark.parametrize("a,b,result",[
        (10,-10,0),
        (10,10,20),
        (-1,-1,-2),
        (0,0,0),
        (0,1,1),
        (0,-1,-1),
        (1,1.1,2.1),
        (1.5,1.5,3)
    ])
    def test_add(self,a,b,result):
        assert a+b==result

    """
        两个正数
        两个负数
        正数除以负数
        负数除以正数
        小数除以小数
        整数除以小数
        小数除以整数
    """
    @pytest.mark.parametrize("c,d,result1",[
        (1,1,1),
        (-2,-1,2),
        (2,-1,-2),
        (-1,2,-0.5),
        (1.5,0.5,3),
        (1,0.3,3.3333333333333333),
        (0.3,3,0.1)
    ])
    def test_chufa(self,c,d,result1):
        assert c/d == result1





