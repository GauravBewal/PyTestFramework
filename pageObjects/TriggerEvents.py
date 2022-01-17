from selenium.webdriver.common.by import By


class TriggerEvents:

    def __init__(self, driver):
        self.driver = driver

    button_create_event = (By.XPATH, "//button[contains(@class,'el-tooltip create-playbook')]")

    def click_create_new_event(self):
        return self.driver.find_element(*TriggerEvents.button_create_event)

    text_get_slider_heading = (By.XPATH, "//span[@class='cursor-pointer font-size-20 font-weight-500']")

    def get_slider_text(self):
        return self.driver.find_element(*TriggerEvents.text_get_slider_heading)

    button_close_slider = (By.XPATH, "//i[@class='el-icon-close text-size-2 cursor-pointer']")

    def click_close_slider(self):
        return self.driver.find_element(*TriggerEvents.button_close_slider)
