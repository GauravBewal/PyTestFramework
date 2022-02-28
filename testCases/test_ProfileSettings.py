import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.ProfileSettings import ProfileSettings
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestProfileSettings(Base):

    @pytest.mark.smoke
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
        nav.Navigate_Profile_icon()
        log.info("Click on Profile Settings dropdown")
        profile.click_Profile_Settings()
        log.info("Check after click page redirects")
        assert action.getTitle() in 'Profile Settings | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Verify_Change_Password_redirection(self):
        """
            Verify user is able to click on Change Password on Profile Settings page
            Validation 1. - On the basis of slider title
        """
        log = self.getlogger()
        profile = ProfileSettings(self.driver)
        log.info("Click on the password change button")
        profile.click_Change_Password()
        log.info("Read the slider button")
        slider_text = profile.get_ChangePassword_SliderTitle()
        log.info("Click on the close button")
        profile.click_Close_ChangePassword_slider()
        assert slider_text in 'Change Password'

    @pytest.mark.smoke
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
