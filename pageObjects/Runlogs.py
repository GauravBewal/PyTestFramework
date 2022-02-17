from selenium.webdriver.common.by import By


class Runlogs:

    def __init__(self, driver):
        self.driver = driver

    runlog_filter_btn = (By.XPATH, "//div[@class='filters-view']//button")

    def click_on_filter_btn(self):
        return self.driver.find_element(*Runlogs.runlog_filter_btn)

    filter_slider_title = (By.XPATH, "//span[@class='filters__header__label']")

    def get_filter_slider_title(self):
        return self.driver.find_element(*Runlogs.filter_slider_title)