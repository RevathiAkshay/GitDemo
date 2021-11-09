## import logging method
import logging


def test_loggingdemo():


    ##create logger object using logging.getlogger()
    logger = logging.getLogger(__name__)

    ##create logging.Filehandler("file1.log) object
    filehandler = logging.FileHandler("file1.log")

    ## to set the format
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    # pass filehandler object to logger.addhandler

    logger.addHandler(filehandler)

    ##to set the level
    logger.setLevel(logging.INFO)
    # write logger statements for Debug, Errror, Info, warning, critical
    logger.debug("Debug statements ")
    logger.info("information only")
    logger.warning("warning statements")
    logger.error("failure")
    logger.critical("catastrophical failure")
