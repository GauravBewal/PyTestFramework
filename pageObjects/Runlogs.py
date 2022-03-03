from selenium.webdriver.common.by import By
from utilities.Actions import Action


class Runlogs(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    runlog_filter_btn = "//div[@class='filters-view']//button"

    def click_on_filter_btn(self):
        return Action.wait_and_click(self, By.XPATH, Runlogs.runlog_filter_btn)

    filter_slider_title = "//span[@class='filters__header__label']"

    def get_filter_slider_title(self):
        return Action.get_text(self, By.XPATH, Runlogs.filter_slider_title)
