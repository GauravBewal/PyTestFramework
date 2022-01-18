from selenium.webdriver.common.by import By


class TenantManagement:

    def __init__(self, driver):
        self.driver = driver

    tab_Tenant_Management = (By.XPATH, "//div[@class='admin-components__list']//div[4]")

    def click_Tenant_Management(self):
        return self.driver.find_element(*TenantManagement.tab_Tenant_Management)

    tab_inactive = (By.XPATH, "//li/a[contains(text(),'Inactive')]")

    def click_inactive_tab(self):
        return self.driver.find_element(*TenantManagement.tab_inactive)

    tab_All = (By.XPATH, "//li/a[contains(text(),'Inactive')]")

    def click_All_tab(self):
        return self.driver.find_element(*TenantManagement.tab_All)

    btn_new_tenant = (By.XPATH, "//header//button")

    def click_new_tenant(self):
        return self.driver.find_element(*TenantManagement.btn_new_tenant)

    text_slider_title = (By.XPATH, "//div[@class='modal--header']//span")

    def get_slider_title(self):
        return self.driver.find_element(*TenantManagement.text_slider_title)

    btn_slider_close = (By.XPATH, "//div[@class='modal--header']//i")

    def click_slider_close(self):
        return self.driver.find_element(*TenantManagement.btn_slider_close)
