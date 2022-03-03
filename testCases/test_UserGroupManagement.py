import pytest

from pageObjects.Navigation import Navigation
from pageObjects.UserGroupManagement import UserGroupManagement
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestUserGroupManagement(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_User_Group_Management_redirection(self):
        """
            Verify redirection to user group management from admin menu
            Validation 1: On the basis of window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on Admin menu")
        nav.click_admin_menu()
        log.info("Click on User group Management tab from Admin Page")
        usergroup.click_user_group_management()
        log.info("Read the page heading")
        assert action.get_title() == 'User Groups Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Click_New_User_Group_btn(self):
        """
            Verify creation of new user group
            Validation - 1. On the basis of slider title
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on add new user button")
        usergroup.click_add_user_group()
        log.info("Read the slider title")
        slider_title = usergroup.get_slider_title()
        log.info("Click on close slider button")
        usergroup.click_slider_close()
        assert slider_title == 'New User Group'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on inactive tab")
        usergroup.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = usergroup.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on All tab")
        usergroup.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = usergroup.get_all_tab_color()
        assert tab_color == '#1a3ee8'
