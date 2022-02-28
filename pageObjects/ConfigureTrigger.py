from selenium.webdriver.common.by import By
from utilities.Actions import Action

class ConfigureTrigger(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_configure_trigger = "//header//button"

    def click_configure_trigger(self):
        return Action.waitandclick(self, By.XPATH, ConfigureTrigger.button_configure_trigger)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        return Action.getText(self, By.XPATH, ConfigureTrigger.text_page_heading)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_heading(self):
        return Action.getText(self, By.XPATH, ConfigureTrigger.text_slider_heading)

    button_close_slider = "//div[@class='modal--header']//i"

    def click_close_slider(self):
        return Action.waitandclick(self, By.XPATH, ConfigureTrigger.button_close_slider)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, ConfigureTrigger.tab_inactive)

    def read_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, ConfigureTrigger.tab_inactive)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, ConfigureTrigger.tab_All)

    def read_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, ConfigureTrigger.tab_All)
