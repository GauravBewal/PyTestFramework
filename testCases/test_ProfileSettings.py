import time
import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.ProfileSettings import ProfileSettings
from utilities.Base import Base
from utilities.Actions import Action


@pytest.mark.usefixtures("setup")
class TestProfileSettings(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_profile_settings_redirection(self):
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
        log.info("Click on Profile Settings dropdown")
        action.click(profile.click_Profile_Settings())
        time.sleep(ReadConfig.sleepWait())
        log.info("Check after click page redirects")
        assert action.getTitle() in 'Profile Settings | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Change_Password_redirection(self):
        """
            Verify user is able to click on Change Password on Profile Settings page
            Validation 1. - On the basis of slider title
        """
        log = self.getlogger()
        action = Action(self.driver)
        profile = ProfileSettings(self.driver)
        action.click(profile.click_Change_Password())
        slider_text = action.getText(profile.get_ChangePassword_SliderTitle())
        time.sleep(ReadConfig.sleepWait())
        action.click(profile.click_Close_ToolTip_ChangePassword())
        assert slider_text in 'Change Password'
