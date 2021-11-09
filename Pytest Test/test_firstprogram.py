##start with test_ or ends with _test
##always used functions for scritping
import pytest


@pytest.mark.smoke
def testFirstPgm():
    print("hello")

def testgreetings():
    print("How are u?")


def test_envieonments(test_dataload1):
    print(test_dataload1)
