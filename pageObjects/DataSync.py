from selenium.webdriver.common.by import By


class DataSync:

    def __init__(self, driver):
        self.driver = driver

    tab_run_history = (By.XPATH, "//a[@href='/soar/data-sync/list/logs']")

    def click_run_history(self):
        return self.driver.find_element(*DataSync.tab_run_history)

    tab_job_details = (By.XPATH, "//a[@href='/soar/data-sync/list/jobs']")

    def click_job_details(self):
        return self.driver.find_element(*DataSync.tab_job_details)
