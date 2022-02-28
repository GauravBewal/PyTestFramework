from selenium.webdriver.common.by import By
from utilities.Actions import Action

class TriggerEvents(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_create_event = "//header//button"

    def click_create_new_event(self):
        return Action.waitandclick(self, By.XPATH, TriggerEvents.button_create_event)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        return Action.getText(self, By.XPATH, TriggerEvents.text_page_heading)

    text_get_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_text(self):
        return Action.getText(self, By.XPATH, TriggerEvents.text_get_slider_heading)

    button_close_slider = "//div[@class='modal--header']//i"

    def click_close_slider(self):
        return Action.waitandclick(self, By.XPATH, TriggerEvents.button_close_slider)
