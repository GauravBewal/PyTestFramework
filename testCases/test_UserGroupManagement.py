import pytest

from pageObjects.Navigation import Navigation
from pageObjects.UserGroupManagement import UserGroupManagement
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestUserGroupManagement(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_User_Group_Management_redirection(self):
        """
        Verify redirection to user group management from admin menu
        Validation 1: On the basis of window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on Admin menu")
        action.click(nav.click_Admin_Menu())
        log.info("Click on User group Management tab from Admin Page")
        action.click(usergroup.click_User_Group_Management())
        assert action.getTitle() in 'User Groups Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_add_user_group(self):
        """
            Verify creation of new user group
            Validation - 1. On the basis of slider title
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on add new user button")
        action.click(usergroup.click_add_user_group())
        log.info("Read the slider title")
        slider_title = action.getText(usergroup.get_slider_title())
        log.info("Click on close slider button")
        action.click(usergroup.click_slider_close())
        assert slider_title == 'New User Group'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on inactive tab")
        action.click(usergroup.click_inactive_tenant_tab())
        tab_color = action.getElementColor(usergroup.click_inactive_tenant_tab())
        assert tab_color == '#1a3ee8'
