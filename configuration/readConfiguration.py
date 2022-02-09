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
    def Wait_10_Sec():
        wait_10_Sec = config.get('Waits', 'Wait_10_Seconds')
        return int(wait_10_Sec)

    @staticmethod
    def Wait_3_Sec():
        wait_3_Sec = config.get('Waits', 'Wait_3_Seconds')
        return int(wait_3_Sec)

    @staticmethod
    def Wait_20_Sec():
        wait_20_Sec = config.get('Waits', 'Wait_20_Seconds')
        return int(wait_20_Sec)

    @staticmethod
    def Wait_50_Sec():
        wait_50_Sec = config.get('Waits', 'Wait_50_Seconds')
        return int(wait_50_Sec)

    @staticmethod
    def appname():
        app_name = config.get('MY_APPS DETAILS', 'app_name')
        return app_name
