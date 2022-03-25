from selenium.webdriver.common.by import By

from utilities.Actions import Action


class ProfileSettings(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    dd_profile_settings = "//i[contains(@class,'icon-profile')]/parent::div"

    def click_profile_settings(self):
        return Action.javascript_click(self, By.XPATH, ProfileSettings.dd_profile_settings)

    btn_change_password = "//header//div[contains(text(),'Change Password')]"

    def click_change_password(self):
        return Action.javascript_click(self, By.XPATH, ProfileSettings.btn_change_password)

    btn_edit_profile = "//header//span[contains(text(),'Edit')]//ancestor::button"

    def click_on_edit_button(self):
        return Action.javascript_click(self, By.XPATH, ProfileSettings.btn_edit_profile)

    btn_save_profile = "//button//span[contains(text(),'Save')]"

    def check_save_btn_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, ProfileSettings.btn_save_profile)

    slider_title_change_password = "(//div[contains(@class,'header__label')]/div)[2]"

    def get_change_password_slider_title(self):
        return Action.get_text(self, By.XPATH, ProfileSettings.slider_title_change_password)

    slider_close_tool_tip = "//div[contains(@class,'header__icons')]//span[@data-testaction='slider-close']"

    def click_close_change_password_slider(self):
        return Action.javascript_click(self, By.XPATH, ProfileSettings.slider_close_tool_tip)
