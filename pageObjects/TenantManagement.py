from selenium.webdriver.common.by import By
from utilities.Actions import Action

class TenantManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_Tenant_Management = "//p[contains(text(),'Tenant Management')]/parent::div/parent::div"

    def click_Tenant_Management(self):
        return Action.waitandclick(self, By.XPATH, TenantManagement.tab_Tenant_Management)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, TenantManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, TenantManagement.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'Inactive')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, TenantManagement.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, TenantManagement.tab_All, 'color')

    btn_new_tenant = "//header//button"

    def click_new_tenant(self):
        return Action.waitandclick(self, By.XPATH, TenantManagement.btn_new_tenant)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.getText(self, By.XPATH, TenantManagement.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.waitandclick(self, By.XPATH, TenantManagement.btn_slider_close)
