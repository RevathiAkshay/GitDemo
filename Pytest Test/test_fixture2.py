from logging import Logger
from Loggerclass import getlogobject
import pytest


@pytest.mark.usefixtures("test_dataload")
class Testgetdata(getlogobject):

    def test_getdata(self,test_dataload):
        log = self.getloggerobject()
        log.info(test_dataload[0])
        log.info(test_dataload[1])

