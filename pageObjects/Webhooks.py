from selenium.webdriver.common.by import By


class Webhooks:

    def __init__(self, driver):
        self.driver = driver

    tab_Webhooks = (By.XPATH, "//div[@class='admin-components__list']//div[9]")

    def click_Webhooks(self):
        return self.driver.find_element(*Webhooks.tab_Webhooks)

    btn_new_webhook = (By.XPATH, "//header//button")

    def click_new_webhook(self):
        return self.driver.find_element(*Webhooks.btn_new_webhook)

    text_slider_heading = (By.XPATH, "//div[@class='modal--header']//span")

    def get_slider_title(self):
        return self.driver.find_element(*Webhooks.text_slider_heading)

    btn_slider_close = (By.XPATH, "//div[@class='modal--header']//i")

    def click_slider_close(self):
        return self.driver.find_element(*Webhooks.btn_slider_close)

    tab_inactive = (By.XPATH, "//li[3]/a[contains(text(),'Inactive')]")

    def click_inactive_tab(self):
        return self.driver.find_element(*Webhooks.tab_inactive)

    tab_All = (By.XPATH, "//li/a[contains(text(),'All')]")

    def click_All_tab(self):
        return self.driver.find_element(*Webhooks.tab_All)
