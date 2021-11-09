import pytest

@pytest.mark.usefixtures("test_requirements")
class TestMain1:

    def test_add1(self):
        a=5
        b=5
        print(a+b)


    def test_sub2(self):
        a = 5
        b = 5
        print(a - b)

    def test_prod3(self):
        a = 5
        b = 5
        print(a * b)





