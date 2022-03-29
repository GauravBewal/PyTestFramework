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

    cancel_btn = "//i[contains(@class,'icon-close')]/parent::div"

    def click_cancel_btn(self):
        return Action.wait_and_click(self, By.XPATH, ProfileSettings.cancel_btn)

    slider_close_tool_tip = "//div[contains(@class,'header__icons')]//span[@data-testaction='slider-close']"

    def click_close_change_password_slider(self):
        return Action.javascript_click(self, By.XPATH, ProfileSettings.slider_close_tool_tip)

    def click_save_btn(self):
        return Action.javascript_click(self, By.XPATH, ProfileSettings.btn_save_profile)

    first_name_tab = "//div//input[@placeholder='Enter First Name']"

    def enter_first_name(self, value):
        return Action.send_keys(self, By.XPATH, ProfileSettings.first_name_tab, value)

    last_name_tab = "//div//input[@placeholder='Enter Last Name']"

    def enter_last_name(self, value):
        return Action.send_keys(self, By.XPATH, ProfileSettings.last_name_tab, value)

    title_name_tab = "//div//input[@placeholder='Enter Title']"

    def enter_title_name(self, value):
        return Action.send_keys(self, By.XPATH, ProfileSettings.title_name_tab, value)

    contact_number_tab = "//div//input[@placeholder='Enter Phone Number']"

    def enter_contact_number(self, value):
        return Action.send_keys(self, By.XPATH, ProfileSettings.contact_number_tab, value)

    first_name_in_view_mode = "//label[@for='first_name']/parent::div//span"

    def get_first_name(self):
        return Action.get_text(self, By.XPATH, ProfileSettings.first_name_in_view_mode)

    last_name_in_view_mode = "//label[@for='last_name']/parent::div//span"

    def get_last_name(self):
        return Action.get_text(self, By.XPATH, ProfileSettings.last_name_in_view_mode)

    title_in_view_mode = "//label[@for='title']/parent::div//span"

    def get_title_name(self):
        return Action.get_text(self, By.XPATH, ProfileSettings.title_in_view_mode)

    contact_number_in_view_mode = "//label[@for='contact_number']/parent::div//span"

    def get_contact_number(self):
        return Action.get_text(self, By.XPATH, ProfileSettings.contact_number_in_view_mode)

    def clear_first_name(self):
        return Action.clear_field(self, By.XPATH, ProfileSettings.first_name_tab)

    def clear_last_name(self):
        return Action.clear_field(self, By.XPATH, ProfileSettings.last_name_tab)

    def clear_title_name(self):
        return Action.clear_field(self, By.XPATH, ProfileSettings.title_name_tab)

    def clear_contact_number(self):
        return Action.clear_field(self, By.XPATH, ProfileSettings.contact_number_tab)
