from selenium.webdriver.common.by import By
from utilities.Actions import Action

class Webhooks(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_Webhooks = "//p[contains(text(),'Webhook')]/parent::div/parent::div"

    def click_Webhooks(self):
        return Action.waitandclick(self, By.XPATH, Webhooks.tab_Webhooks)

    btn_new_webhook = "//header//button"

    def click_new_webhook(self):
        return Action.waitandclick(self, By.XPATH, Webhooks.btn_new_webhook)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.getText(self, By.XPATH, Webhooks.text_slider_heading)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.waitandclick(self, By.XPATH, Webhooks.btn_slider_close)

    tab_inactive = "//li[3]/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, Webhooks.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, Webhooks.tab_inactive)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, Webhooks.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, Webhooks.tab_All)
