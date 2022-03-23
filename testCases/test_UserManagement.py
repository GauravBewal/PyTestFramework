import pytest

from pageObjects.Navigation import Navigation
from pageObjects.UserManagement import UserManagement
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestUserManagement(Base):

    @pytest.mark.regression
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
        nav.click_admin_menu()
        log.info("Click on User Management tab from Admin Page")
        user.click_user_management()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        global active_count
        active_count = user.get_user_count()
        assert action.get_title() in 'User Management | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Verify_Switch_Inactive_tab(self):
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
        log.info("Check visibility of inactive user")
        user.visibility_of_first_inactive_user()
        global inactive_count
        inactive_count = user.get_user_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        log.info("Click on All tab")
        user.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = user.get_all_tab_color()
        log.info("check visibility of active user")
        user.visibility_of_first_active_user()
        global all_tab_count
        all_tab_count = user.get_user_count()
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count+active_count

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Click_Add_User_btn(self):
        """
            Verify create button functionality of new user
            Validation - 1. On the basis of slider title
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        log.info("Switch to active tab")
        user.click_active_tab()
        log.info("Visibility og first active user")
        user.visibility_of_first_active_user()
        log.info("Click on add new user button")
        user.click_add_user()
        log.info("Read the slider title")
        slider_title = user.get_slider_title()
        log.info("Click on close slider button")
        user.click_slider_close()
        assert slider_title == 'User'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_05_Click_Export_User_btn(self):
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

