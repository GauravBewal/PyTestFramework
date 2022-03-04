from selenium.webdriver.common.by import By
from utilities.Actions import Action


class Webhooks(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_webhooks = "//p[contains(text(),'Webhook')]/parent::div/parent::div"

    def click_webhooks(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_webhooks)

    btn_new_webhook = "//header//button"

    def click_new_webhook(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.btn_new_webhook)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, Webhooks.text_slider_heading)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.btn_slider_close)

    tab_inactive = "//li[3]/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_All)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_All, 'color')
