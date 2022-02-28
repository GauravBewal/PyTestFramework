from selenium.webdriver.common.by import By
from utilities.Actions import Action

class ConsoleStatus(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    left_panel_elastic_search = "//div[contains(text(),'Elasticsearch')]"

    def click_elastic_search(self):
        return Action.waitandclick(self, By.XPATH, ConsoleStatus.left_panel_elastic_search)

    left_panel_my_sql = "//div[contains(text(),'MySQL')]"

    def click_my_sql(self):
        return Action.waitandclick(self, By.XPATH, ConsoleStatus.left_panel_my_sql)

    left_panel_redis = "//div[contains(text(),'Redis')]"

    def click_redis(self):
        return Action.waitandclick(self, By.XPATH, ConsoleStatus.left_panel_redis)

    left_panel_celery = "//div[contains(text(),'Celery')]"

    def click_celery(self):
        return Action.waitandclick(self, By.XPATH, ConsoleStatus.left_panel_celery)

    text_server_page_heading = "//h1[contains(text(),'Console Status')]/following-sibling::span"

    def get_server_page_heading(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.text_server_page_heading)

    left_panel_gunicorn = "//div[contains(text(),'Gunicorn')]"

    def click_gunicorn(self):
        return Action.waitandclick(self, By.XPATH, ConsoleStatus.left_panel_gunicorn)

    left_panel_ngnix = "//div[contains(text(),'Nginx')]"

    def click_ngnix(self):
        return Action.waitandclick(self, By.XPATH, ConsoleStatus.left_panel_ngnix)

    get_status_text_server = "//*[contains(@id,'el-collapse-head')]/div/div[3]"

    def get_server_status(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.get_status_text_server)

    list_overview_elastic_search = "//*[@id='admin-right__panel']/div/div[2]/div/div/div[1]/h3"

    def get_overview_elastic_search_text(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.list_overview_elastic_search)

    list_overview_my_sql = "//*[@id='admin-right__panel']/div/div[2]/div/div/div[2]/h3"

    def get_overview_my_sql_text(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.list_overview_my_sql)

    list_overview_redis = "//*[@id='admin-right__panel']/div/div[2]/div/div/div[3]/h3"

    def get_overview_redis_text(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.list_overview_redis)

    list_overview_celery = "//*[@id='admin-right__panel']/div/div[2]/div/div/div[4]/h3"

    def get_overview_celery_text(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.list_overview_celery)

    list_overview_gunicorn = "//*[@id='admin-right__panel']/div/div[2]/div/div/div[5]/h3"

    def get_overview_gunicorn_text(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.list_overview_gunicorn)

    list_overview_ngnix = "//*[@id='admin-right__panel']/div/div[2]/div/div/div[6]/h3"

    def get_overview_ngnix_text(self):
        return Action.getText(self, By.XPATH, ConsoleStatus.list_overview_ngnix)
