import configparser
import os

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
    def ctix_baseurl():
        ctix_base_url = config.get('CTIX_CREDS', 'base_url')
        return ctix_base_url

    @staticmethod
    def ctix_access_key():
        ctix_access_id = config.get('CTIX_CREDS', 'access_key')
        return ctix_access_id

    @staticmethod
    def ctix_secret_key():
        ctix_secret_id = config.get('CTIX_CREDS', 'secret_key')
        return ctix_secret_id

    @staticmethod
    def cftr_baseurl():
        cftr_base_url = config.get('CFTR_CREDS', 'base_url')
        return cftr_base_url

    @staticmethod
    def cftr_access_key():
        cftr_access_id = config.get('CFTR_CREDS', 'access_key')
        return cftr_access_id

    @staticmethod
    def cftr_secret_key():
        cftr_secret_id = config.get('CFTR_CREDS', 'secret_key')
        return cftr_secret_id



    @staticmethod
    def Wait_10_Sec():
        wait_10_Sec = config.get('Waits', 'Wait_10_Seconds')
        return int(wait_10_Sec)

    @staticmethod
    def Wait_3_Sec():
        wait_3_Sec = config.get('Waits', 'Wait_3_Seconds')
        return int(wait_3_Sec)

    @staticmethod
    def Wait_15_Sec():
        wait_15_Sec = config.get('Waits', 'Wait_15_Seconds')
        return int(wait_15_Sec)

    @staticmethod
    def Wait_6_Sec():
        wait_6_Sec = config.get('Waits', 'Wait_6_Seconds')
        return int(wait_6_Sec)

    @staticmethod
    def appname():
        app_name = config.get('MY_APPS DETAILS', 'app_name')
        return app_name
