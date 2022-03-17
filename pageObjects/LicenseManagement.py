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

    Number_of_days_left = "//div//div[@class='d-flex align-items-end']//div[1]"

    def get_number_of_days_left(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.Number_of_days_left)

    name_of_tenant = "(//div[@class='d-flex']//div//div//child::div[2])[1]"

    def get_name_of_Tenant(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.name_of_tenant)

    name_of_tenant_code = "(//div[@class='d-flex']//div//div//child::div[2])[2]"

    def get_name_of_Tenant_code(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.name_of_tenant_code)

    name_of_tenant_version = "(//div[@class='d-flex']//div//div//child::div[2])[3]"

    def get_name_of_Tenant_version(self):
        return Action.get_text(self, By.XPATH, LicenseManagement.name_of_tenant_version)

    tick_cross_btn = "//span[@class='el-input__suffix']"

    def check_cross_and_tick_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, LicenseManagement.tick_cross_btn)

    sync_now_btn = "//header//span"

    def visiblity_of_Sync_Now_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, LicenseManagement.sync_now_btn)