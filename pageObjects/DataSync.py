from selenium.webdriver.common.by import By


class DataSync:

    def __init__(self, driver):
        self.driver = driver

    tab_run_history = (By.XPATH, "//a[@href='/soar/data-sync/list/logs']")

    def click_run_history(self):
        return self.driver.find_element(*DataSync.tab_run_history)

    button_create_data_sync = (By.XPATH, "//button[contains(@class,'el-tooltip d-flex align-items-center')]")

    def click_create_data_sync(self):
        return self.driver.find_element(*DataSync.button_create_data_sync)

    tab_job_details = (By.XPATH, "//a[@href='/soar/data-sync/list/jobs']")

    def click_job_details(self):
        return self.driver.find_element(*DataSync.tab_job_details)

    button_back_to_home = (By.XPATH, "//div[contains(@class,'back-button-container')]")

    def click_back_button(self):
        return self.driver.find_element(*DataSync.button_back_to_home)

    button_confirm_close = (By.XPATH, "//button[contains(text(),'Close without Saving')]")

    def click_confirm_close(self):
        return self.driver.find_element(*DataSync.button_confirm_close)
