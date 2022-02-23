from selenium.webdriver.common.by import By


class ProfileSettings:

    def __init__(self, driver):
        self.driver = driver

    dd_profile_settings = (By.XPATH, "//i[contains(@class,'icon-profile')]/parent::div")

    def click_Profile_Settings(self):
        return self.driver.find_element(*ProfileSettings.dd_profile_settings)

    btn_change_password = (By.XPATH, "//header//div[contains(text(),'Change Password')]")

    def click_Change_Password(self):
        return self.driver.find_element(*ProfileSettings.btn_change_password)

    btn_edit_profile = (By.XPATH, "//header//span[contains(text(),'Edit')]//ancestor::button")

    def click_on_edit_button(self):
        return self.driver.find_element(*ProfileSettings.btn_edit_profile)

    btn_save_profile = (By.XPATH, "//button//span[contains(text(),'Save')]")

    def check_save_btn_visibility(self):
        return self.driver.find_element(*ProfileSettings.btn_save_profile)

    slider_title_change_password = (By.CSS_SELECTOR, ".cy-right-modal-header__label.flex-grow-1")

    def get_ChangePassword_SliderTitle(self):
        return self.driver.find_element(*ProfileSettings.slider_title_change_password)

    slider_close_tool_tip = (By.CSS_SELECTOR, ".cy-right-modal-header__icons")

    def click_Close_ToolTip_ChangePassword(self):
        return self.driver.find_element(*ProfileSettings.slider_close_tool_tip)
