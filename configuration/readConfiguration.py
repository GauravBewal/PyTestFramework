import os
import configparser

config = configparser.ConfigParser()

Current_folder = os.path.dirname(os.path.abspath(__file__))
ini_file = os.path.join(Current_folder, 'config.ini')

config.read(ini_file)


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

    @staticmethod
    def sleepWait():
        sleepWait = config.get('Waits', 'sleepWait')
        return int(sleepWait)

    @staticmethod
    def mediumSleepWait():
        mediumsleepWait = config.get('Waits', 'MediumSleepWait')
        return int(mediumsleepWait)

    @staticmethod
    def largeSleepWait():
        largesleepWait = config.get('Waits', 'LargeSleepWait')
        return int(largesleepWait)

    @staticmethod
    def appname():
        app_name = config.get('MY_APPS DETAILS', 'app_name')
        return app_name
