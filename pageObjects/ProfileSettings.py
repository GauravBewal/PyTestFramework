from selenium.webdriver.common.by import By

from utilities.Actions import Action


class ProfileSettings(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    dd_profile_settings = "//i[contains(@class,'icon-profile')]/parent::div"

    def click_profile_settings(self):
        """
            Click profile settings
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ProfileSettings.dd_profile_settings)

    btn_change_password = "//header//div[contains(text(),'Change Password')]"

    def click_change_password(self):
        """
            Click on change password
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ProfileSettings.btn_change_password)

    btn_edit_profile = "//header//span[contains(text(),'Edit')]//ancestor::button"

    def click_on_edit_button(self):
        """
            Click on edit button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ProfileSettings.btn_edit_profile)

    btn_save_profile = "//button//span[contains(text(),'Save')]"

    def check_save_btn_visibility(self):
        """
            Click on save button visibility
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, ProfileSettings.btn_save_profile)

    slider_title_change_password = "(//div[contains(@class,'header__label')]/div)[2]"

    def get_change_password_slider_title(self):
        """
            Get change password slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, ProfileSettings.slider_title_change_password)

    cancel_btn = "//i[contains(@class,'icon-close')]/parent::div"

    def click_cancel_btn(self):
        """
            Click on cancel button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ProfileSettings.cancel_btn)

    slider_close_tool_tip = "//div[contains(@class,'header__icons')]//span[@data-testaction='slider-close']"

    def click_close_change_password_slider(self):
        """
            Click on close change password slider
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ProfileSettings.slider_close_tool_tip)

    def click_save_btn(self):
        """
            Click on Save button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ProfileSettings.btn_save_profile)

    first_name_tab = "//div//input[@placeholder='Enter First Name']"

    def enter_first_name(self, value):
        """
            Enter first name in text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ProfileSettings.first_name_tab, value)

    last_name_tab = "//div//input[@placeholder='Enter Last Name']"

    def enter_last_name(self, value):
        """
            Enter last name in text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ProfileSettings.last_name_tab, value)

    title_name_tab = "//div//input[@placeholder='Enter Title']"

    def enter_title_name(self, value):
        """
            Enter Title Name in text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ProfileSettings.title_name_tab, value)

    contact_number_tab = "//div//input[@placeholder='Enter Phone Number']"

    def enter_contact_number(self, value):
        """
            Enter contact number in text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ProfileSettings.contact_number_tab, value)

    first_name_in_view_mode = "//label[@for='first_name']/parent::div//span"

    def get_first_name(self):
        """
            Get first name in text field
            :return:
        """
        return Action.get_text(self, By.XPATH, ProfileSettings.first_name_in_view_mode)

    last_name_in_view_mode = "//label[@for='last_name']/parent::div//span"

    def get_last_name(self):
        """
            Get last name in text field
            :return:
        """
        return Action.get_text(self, By.XPATH, ProfileSettings.last_name_in_view_mode)

    title_in_view_mode = "//label[@for='title']/parent::div//span"

    def get_title_name(self):
        """
            Get title name
            :return:
        """
        return Action.get_text(self, By.XPATH, ProfileSettings.title_in_view_mode)

    contact_number_in_view_mode = "//label[@for='contact_number']/parent::div//span"

    def get_contact_number(self):
        """
            Get contact number
            :return:
        """
        return Action.get_text(self, By.XPATH, ProfileSettings.contact_number_in_view_mode)

    def clear_first_name(self):
        """
            Clear first name field
            :return:
        """
        return Action.clear_field(self, By.XPATH, ProfileSettings.first_name_tab)

    def clear_last_name(self):
        """
            Clear last name
            :return:
        """
        return Action.clear_field(self, By.XPATH, ProfileSettings.last_name_tab)

    def clear_title_name(self):
        """
            Clear title name
            :return:
        """
        return Action.clear_field(self, By.XPATH, ProfileSettings.title_name_tab)

    def clear_contact_number(self):
        """
            Clear contact number
            :return:
        """
        return Action.clear_field(self, By.XPATH, ProfileSettings.contact_number_tab)
