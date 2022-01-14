from selenium.webdriver.common.by import By


class ProfileSettings:

    def __init__(self, driver):
        self.driver = driver

    dd_profile_settings = (By.XPATH, "//ul[@class='el-dropdown-menu el-popper']/li[1]/div/div")

    def click_Profile_Settings(self):
        return self.driver.find_element(*ProfileSettings.dd_profile_settings)

    btn_change_password = (By.CSS_SELECTOR, ".cs-profile-icon.d-flex.align-items-center.justify-content-center")

    def click_Change_Password(self):
        return self.driver.find_element(*ProfileSettings.btn_change_password)

    btn_edit_Profile = (By.CSS_SELECTOR, "button[class='ml-3 px-4 d-flex align-items-center "
                                         "justify-content-center cy-button cy-button--primary cy-button--md']")

    def click_Edit(self):
        return self.driver.find_element(*ProfileSettings.btn_edit_Profile)

    slider_title_change_password = (By.CSS_SELECTOR, ".cy-right-modal-header__label.flex-grow-1")

    def get_ChangePassword_SliderTitle(self):
        return self.driver.find_element(*ProfileSettings.slider_title_change_password)

    slider_close_tool_tip = (By.CSS_SELECTOR, ".cy-right-modal-header__icons")

    def click_Close_ToolTip_ChangePassword(self):
        return self.driver.find_element(*ProfileSettings.slider_close_tool_tip)
