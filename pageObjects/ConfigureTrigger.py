from selenium.webdriver.common.by import By


class ConfigureTrigger:

    def __init__(self, driver):
        self.driver = driver

    button_configure_trigger = (By.XPATH, "//header//button")

    def click_configure_trigger(self):
        return self.driver.find_element(*ConfigureTrigger.button_configure_trigger)

    text_slider_heading = (By.XPATH, "//div[@class='modal--header']//span")

    def get_slider_heading(self):
        return self.driver.find_element(*ConfigureTrigger.text_slider_heading)

    button_close_slider = (By.XPATH, "//div[@class='modal--header']//i")

    def click_close_slider(self):
        return self.driver.find_element(*ConfigureTrigger.button_close_slider)

    tab_inactive = (By.XPATH, "//li/a[contains(text(),'Inactive')]")

    def click_inactive_tab(self):
        return self.driver.find_element(*ConfigureTrigger.tab_inactive)

    tab_All = (By.XPATH, "//li/a[contains(text(),'All')]")

    def click_All_tab(self):
        return self.driver.find_element(*ConfigureTrigger.tab_All)
