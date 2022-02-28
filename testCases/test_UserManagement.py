import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.UserManagement import UserManagement
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestUserManagement(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_User_Management_redirection(self):
        """
        Verify redirection to user management from admin menu
        Validation 1: On the basis of window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        user = UserManagement(self.driver)
        log.info("Click on Admin menu")
        nav.click_Admin_Menu()
        log.info("Click on User Management tab from Admin Page")
        user.click_User_Management()
        assert action.getTitle() in 'User Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Click_Add_User_btn(self):
        """
            Verify create button functionality of new user
            Validation - 1. On the basis of slider title
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        log.info("Click on add new user button")
        user.click_add_user()
        log.info("Read the slider title")
        slider_title = user.get_slider_title()
        log.info("Click on close slider button")
        user.click_slider_close()
        assert slider_title == 'User'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Click_Export_User_btn(self):
        """
            Verify export functionality of user management
            Validation - 1. On the basis of export options visibility
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        log.info("Click on export button")
        user.click_export()
        log.info("Read export option available")
        visibility = user.export_option_visibility()
        assert visibility is True

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        log.info("Click on inactive tab")
        user.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = user.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        log.info("Click on All tab")
        user.click_All_tab()
        log.info("Read the tab color after switching")
        tab_color = user.get_all_tab_color()
        assert tab_color == '#1a3ee8'
