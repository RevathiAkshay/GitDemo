import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_sectst():
    a=6
    b=7
    assert(a>b)

def testSecondgreetings():
    a=4
    b=5
    sum = a+b
    print(sum)



