import time

import pytest

from pageObjects.Navigation import Navigation
from pageObjects.UserManagement import UserManagement
from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestUserManagement(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_User_Management_redirection(self):
        """
        Verify redirection to user management from admin menu
        Validation 1: On the basis of window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        user = UserManagement(self.driver)
        log.info("Click on Admin menu")
        action.click(nav.click_Admin_Menu())
        log.info("Click on User Management tab from Admin Page")
        action.click(user.click_User_Management())
        assert action.getTitle() in 'User Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_add_user(self):
        """
            Verify creation of new user
            Validation - 1. On the basis of slider title
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on add new user button")
        action.click(user.click_add_user())
        log.info("Read the slider title")
        slider_title = action.getText(user.get_slider_title())
        log.info("Click on close slider button")
        action.click(user.click_slider_close())
        assert slider_title == 'User'


    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_export_user(self):
        """
            Verify export functionality of user management
            Validation - 1. On the basis of export options visibility
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on export button")
        action.click(user.click_export())
        time.sleep(ReadConfig.sleepWait())
        log.info("Read export option available")
        t = action.check_visibility_of_element(user.export_option_visibility())
        assert t is True



    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_switch_inactive_tab(self):

        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on inactive tab")
        action.click(user.click_inactive_tenant_tab())
        tab_color = action.getElementColor(user.click_inactive_tenant_tab())
        assert tab_color == '#1a3ee8'

