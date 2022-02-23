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
        action.click(nav.Navigate_Profile_icon())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Click on Profile Settings dropdown")
        action.click(profile.click_Profile_Settings())
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
        action = Action(self.driver)
        profile = ProfileSettings(self.driver)
        action.click(profile.click_Change_Password())
        slider_text = action.getText(profile.get_ChangePassword_SliderTitle())
        time.sleep(ReadConfig.Wait_3_Sec())
        action.click(profile.click_Close_ToolTip_ChangePassword())
        assert slider_text in 'Change Password'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Click_on_Edit_Profile_btn(self):
        """
            Verify user is able to click on edit profile button
            Validation: Based on the save button visibility
        """
        log = self.getlogger()
        action = Action(self.driver)
        profile = ProfileSettings(self.driver)
        log.info("Clicking on edit button")
        action.click(profile.click_on_edit_button())
        log.info("Check for the save button visibility")
        val = action.check_visibility_of_element(profile.check_save_btn_visibility())
        assert val is True
