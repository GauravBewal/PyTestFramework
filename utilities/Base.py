import inspect
import logging
import os
import pytest


@pytest.mark.usefixtures("setup")
class Base:

        def getlogger(self):
            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)
            current_folder = os.path.dirname(os.path.abspath(__file__))
            log_path = os.path.join(current_folder, "../", 'logs', 'automation.log')
            filehandler = logging.FileHandler(log_path)
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
            logger.setLevel(logging.INFO)
            return logger
