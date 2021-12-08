import configparser
import os

os.environ["PYTHONPATH"] = os.path.join(os.getcwd().split("CSOL_Automation_Test")[0], "CSOL_Automation_Test")
ini_path = os.path.join(os.environ["PYTHONPATH"], "configuration", "config.ini")
config = configparser.ConfigParser()
config.read(ini_path)


class ReadConfig:

    @staticmethod
    def getAppURL():
        url = config.get('Environment_Details', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        userName = config.get('App_Credentials', 'userName')
        return userName

    @staticmethod
    def getPassword():
        Password = config.get('App_Credentials', 'Password')
        return Password

    @staticmethod
    def defaultWait():
        Wait = config.get('Waits', 'defaultWait')
        return Wait
