from selenium.webdriver.common.by import By

from utilities.Actions import Action


class LicenseManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    btn_licence_update_button = "//button/span[contains(text(),'Update')]"

    def click_licence_update_button(self):
        return Action.javascript_click(self, By.XPATH, LicenseManagement.btn_licence_update_button)

    text_licence_field = "//div[@class='cs-lincese bg-n10']//input"

    def licence_key_field(self, value):
        return Action.get_attribute(self, By.XPATH, LicenseManagement.text_licence_field, value)

    user_accounts_card_text = "//div[@id='chart-users']/preceding-sibling::div"

    def get_text_from_user_accounts_card(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.user_accounts_card_text)

    Open_APIs_card_text = "//div[@id='chart-openapi']/preceding-sibling::div"

    def get_text_from_Open_APIs_card(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.Open_APIs_card_text)

    Webhooks_card_text = "//div[@id='chart-webhooks']/preceding-sibling::div"

    def get_text_from_Webhooks_card(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.Webhooks_card_text)
