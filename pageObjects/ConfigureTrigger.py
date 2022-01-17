from selenium.webdriver.common.by import By


class ConfigureTrigger:

    def __init__(self, driver):
        self.driver = driver

    button_configure_trigger = (By.XPATH, "//button[contains(@class,'el-tooltip create-playbook')]")

    def click_configure_trigger(self):
        return self.driver.find_element(*ConfigureTrigger.button_configure_trigger)

    text_slider_heading = (By.XPATH, "//span[@class='cursor-pointer font-size-20 font-weight-500']")

    def get_slider_heading(self):
        return self.driver.find_element(*ConfigureTrigger.text_slider_heading)

    button_close_slider = (By.XPATH, "//i[@class='el-icon-close text-size-2 cursor-pointer']")

    def click_close_slider(self):
        return self.driver.find_element(*ConfigureTrigger.button_close_slider)
