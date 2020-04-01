import pytest
import yaml
import selenium

class Test_yamll:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_y(self,a,b):
        print(a+b)