from selenium.webdriver.common.by import By
from utilities.Actions import Action

class ProfileSettings(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    dd_profile_settings = "//i[contains(@class,'icon-profile')]/parent::div"

    def click_Profile_Settings(self):
        return Action.waitandclick(self, By.XPATH, ProfileSettings.dd_profile_settings)

    btn_change_password = "//header//div[contains(text(),'Change Password')]"

    def click_Change_Password(self):
        return Action.waitandclick(self, By.XPATH, ProfileSettings.btn_change_password)

    btn_edit_profile = "//header//span[contains(text(),'Edit')]//ancestor::button"

    def click_on_edit_button(self):
        return Action.waitandclick(self, By.XPATH, ProfileSettings.btn_edit_profile)

    btn_save_profile = "//button//span[contains(text(),'Save')]"

    def check_save_btn_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, ProfileSettings.btn_save_profile)

    slider_title_change_password = ".cy-right-modal-header__label.flex-grow-1"

    def get_ChangePassword_SliderTitle(self):
        return Action.getText(self, By.CSS_SELECTOR, ProfileSettings.slider_title_change_password)

    slider_close_tool_tip = ".cy-right-modal-header__icons"

    def click_Close_ChangePassword_slider(self):
        return Action.waitandclick(self, By.CSS_SELECTOR, ProfileSettings.slider_close_tool_tip)
