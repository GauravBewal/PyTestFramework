import pytest

from pageObjects.Navigation import Navigation
from pageObjects.ProfileSettings import ProfileSettings
from pageObjects.CommonElements import Tooltip
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestProfileSettings(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Profile_Settings_redirection(self):
        """
            Verify user is able to access profile setting page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        profile = ProfileSettings(self.driver)
        log.info("Click on Profile Settings icon")
        nav.navigate_profile_icon()
        log.info("Click on Profile Settings dropdown")
        profile.click_profile_settings()
        log.info("Check after click page redirects")
        assert action.get_title() in 'Profile Settings | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Verify_Change_Password_redirection(self):
        """
            Verify user is able to click on Change Password on Profile Settings page
            Validation 1. - On the basis of slider title
        """
        log = self.getlogger()
        profile = ProfileSettings(self.driver)
        log.info("Click on the password change button")
        profile.click_change_password()
        log.info("Read the slider button")
        slider_text = profile.get_change_password_slider_title()
        log.info("Click on the close button")
        profile.click_close_change_password_slider()
        assert slider_text in 'Change Password'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Click_on_Edit_Profile_btn(self):
        """
            Verify user is able to click on edit profile button
            Validation: Based on the save button visibility
        """
        log = self.getlogger()
        profile = ProfileSettings(self.driver)
        log.info("Clicking on edit button")
        profile.click_on_edit_button()
        log.info("Check for the save button visibility")
        visibility = profile.check_save_btn_visibility()
        assert visibility is True
        profile.click_cancel_btn()



    @pytest.mark.regression
    def test_04_Edit_Name_of_user(self):
        """
            Verify user is able to edit profile's first name and last name
            Validation: Based on the Toast message and comparison based on changes made in fields
        """
        log = self.getlogger()
        profile = ProfileSettings(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        prev_first_name = profile.get_first_name()
        prev_last_name = profile.get_last_name()
        log.info("Clicking on edit button")
        profile.click_on_edit_button()
        global first_name
        global last_name
        first_name = "ui-automation"
        last_name = action.get_current_time()
        profile.clear_first_name()
        log.info("Enter fist name of the user")
        profile.enter_first_name(first_name)
        profile.clear_last_name()
        log.info("Enter last name of the user")
        profile.enter_last_name(last_name)
        log.info("Click for the save button")
        profile.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close tool tip")
        tooltip.click_close_tooltip()
        updated_first_name = profile.get_first_name()
        updated_last_name = profile.get_last_name()
        assert updated_first_name == first_name and updated_last_name == last_name
        profile.click_on_edit_button()
        profile.clear_first_name()
        profile.enter_first_name(prev_first_name)
        profile.clear_last_name()
        profile.enter_last_name(prev_last_name)
        profile.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close tool tip")
        tooltip.click_close_tooltip()

    @pytest.mark.regression
    def test_05_Edit_Title_of_user(self):
        """
            Verify user is able to edit profile's title name
            Validation: Based on the Toast message and comparison based on changes made in fields
        """
        log = self.getlogger()
        profile = ProfileSettings(self.driver)
        tooltip = Tooltip(self.driver)
        prev_title_name = profile.get_title_name()
        log.info("Clicking on edit button")
        profile.click_on_edit_button()
        global title_name
        title_name = "ui-automation"
        profile.clear_title_name()
        log.info("Enter title name of the user")
        profile.enter_title_name(title_name)
        log.info("Click for the save button")
        profile.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close tool tip")
        tooltip.click_close_tooltip()
        updated_title_name = profile.get_title_name()
        assert updated_title_name == title_name
        profile.click_on_edit_button()
        profile.clear_title_name()
        if prev_title_name != "—":
            profile.enter_title_name(prev_title_name)
        profile.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close tool tip")
        tooltip.click_close_tooltip()

    @pytest.mark.regression
    def test_06_Edit_contact_number_of_user(self):
        """
            Verify user is able to edit profile's contact number
            Validation: Based on the Toast message and comparison based on changes made in fields
        """
        log = self.getlogger()
        profile = ProfileSettings(self.driver)
        tooltip = Tooltip(self.driver)
        action = Action(self.driver)
        prev_mobile_number = profile.get_contact_number()
        log.info("Clicking on edit button")
        profile.click_on_edit_button()
        global mobile_number
        mobile_number = action.get_random_digit() + action.get_random_digit()
        profile.clear_contact_number()
        log.info("Enter contact number of the user")
        profile.enter_contact_number(mobile_number)
        log.info("Click for the save button")
        profile.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close tool tip")
        tooltip.click_close_tooltip()
        updated_mobile_number = profile.get_contact_number()
        assert updated_mobile_number == mobile_number
        profile.click_on_edit_button()
        profile.clear_contact_number()
        if prev_mobile_number != "—":
            profile.enter_contact_number(prev_mobile_number)
        profile.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close tool tip")
        tooltip.click_close_tooltip()




