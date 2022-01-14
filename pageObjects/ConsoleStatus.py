from selenium.webdriver.common.by import By


class ConsoleStatus:

    def __init__(self, driver):
        self.driver = driver

    left_panel_elastic_search = (By.XPATH, "//*[@id='admin-left__panel']/ul/li[11]/div[3]")

    def click_elastic_search(self):
        return self.driver.find_element(*ConsoleStatus.left_panel_elastic_search)

    left_panel_my_sql = (By.XPATH, "//*[@id='admin-left__panel']/ul/li[11]/div[4]")

    def click_my_sql(self):
        return self.driver.find_element(*ConsoleStatus.left_panel_my_sql)

    left_panel_redis = (By.XPATH, "//*[@id='admin-left__panel']/ul/li[11]/div[5]")

    def click_redis(self):
        return self.driver.find_element(*ConsoleStatus.left_panel_redis)

    left_panel_celery = (By.XPATH, "//*[@id='admin-left__panel']/ul/li[11]/div[6]")

    def click_celery(self):
        return self.driver.find_element(*ConsoleStatus.left_panel_celery)

    left_panel_gunicorn = (By.XPATH, "//*[@id='admin-left__panel']/ul/li[11]/div[7]")

    def click_gunicorn(self):
        return self.driver.find_element(*ConsoleStatus.left_panel_gunicorn)

    left_panel_ngnix = (By.XPATH, "//*[@id='admin-left__panel']/ul/li[11]/div[8]")

    def click_ngnix(self):
        return self.driver.find_element(*ConsoleStatus.left_panel_ngnix)

    get_status_text_server = (By.XPATH, "//*[contains(@id,'el-collapse-head')]/div/div[3]")

    def get_server_status(self):
        return self.driver.find_element(*ConsoleStatus.get_status_text_server)

    list_overview_elastic_search = (By.XPATH, "//*[@id='admin-right__panel']/div/div[2]/div/div/div[1]/h3")

    def get_overview_elastic_search_text(self):
        return self.driver.find_element(*ConsoleStatus.list_overview_elastic_search)

    list_overview_my_sql = (By.XPATH, "//*[@id='admin-right__panel']/div/div[2]/div/div/div[2]/h3")

    def get_overview_my_sql_text(self):
        return self.driver.find_element(*ConsoleStatus.list_overview_my_sql)

    list_overview_redis = (By.XPATH, "//*[@id='admin-right__panel']/div/div[2]/div/div/div[3]/h3")

    def get_overview_redis_text(self):
        return self.driver.find_element(*ConsoleStatus.list_overview_redis)

    list_overview_celery = (By.XPATH, "//*[@id='admin-right__panel']/div/div[2]/div/div/div[4]/h3")

    def get_overview_celery_text(self):
        return self.driver.find_element(*ConsoleStatus.list_overview_celery)

    list_overview_gunicorn = (By.XPATH, "//*[@id='admin-right__panel']/div/div[2]/div/div/div[5]/h3")

    def get_overview_gunicorn_text(self):
        return self.driver.find_element(*ConsoleStatus.list_overview_gunicorn)

    list_overview_ngnix = (By.XPATH, "//*[@id='admin-right__panel']/div/div[2]/div/div/div[6]/h3")

    def get_overview_ngnix_text(self):
        return self.driver.find_element(*ConsoleStatus.list_overview_ngnix)

