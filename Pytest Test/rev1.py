

import logging

class log1:
    def logtest(self):
        logger = logging.getLogger(__name__)

        fileh1 = logging.FileHandler("file2.log")
        formater1 = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
        fileh1.setFormatter(formater1)
        logger.addHandler(fileh1)

        logger.setLevel(logging.INFO)
        logger.debug("Degub lines")
        logger.info("info lines")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")