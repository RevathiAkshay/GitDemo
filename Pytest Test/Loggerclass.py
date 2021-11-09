import inspect
import logging


class getlogobject:
    def getloggerobject(self):
        ###this is to get name of the test which calls the Logger function
        testname = inspect.stack()[1][3]
        logger = logging.getLogger(testname)

        filehandler = logging.FileHandler("file1.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger























