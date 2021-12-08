import inspect
import logging
import os

import pytest


@pytest.mark.usefixtures("setup")
class Base:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        os.environ["PYTHONPATH"] = os.path.join(os.getcwd().split("CSOL_Automation_Test")[0], "CSOL_Automation_Test")
        log_path = os.path.join(os.environ["PYTHONPATH"], "logs", "automation.log")
        filehandler = logging.FileHandler(log_path)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
