import pytest

from pageObjects.Navigation import Navigation
from pageObjects.UserGroupManagement import UserGroupManagement
from pageObjects.CommonElements import Tooltip
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestUserGroupManagement(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.usergroupmanagement
    def test_01_Verify_User_Group_Management_redirection(self):
        """
            Verify redirection to user group management from admin menu
            Validation 1: On the basis of window's title
            TC_ID : 001
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
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        global active_count
        log.info("Get the active Usergroup Count")
        active_count = usergroup.get_usergroup_count()
        assert action.get_title() == 'User Groups Management | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.usergroupmanagement
    def test_02_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
            TC_ID :003
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on inactive tab")
        usergroup.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = usergroup.get_inactive_tab_color()
        log.info("Check visibility of first inative usergroup")
        usergroup.visibility_of_first_inactive_usergroup()
        global inactive_count
        inactive_count = usergroup.get_usergroup_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.usergroupmanagement
    def test_03_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
            TC_ID : 004
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on All tab")
        usergroup.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = usergroup.get_all_tab_color()
        log.info("Check visibility of first active usergroup")
        usergroup.visibility_of_first_active_usergroup()
        global all_tab_count
        all_tab_count = usergroup.get_usergroup_count()
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count + active_count

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.usergroupmanagement
    def test_04_Click_New_User_Group_btn(self):
        """
            Verify creation of new user group
            Validation - 1. On the basis of slider title
            TC_ID : 002
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        log.info("Switch to active tab")
        usergroup.click_on_active_tab()
        log.info("Check visibility of first active usergroup")
        usergroup.visibility_of_first_active_usergroup()
        log.info("Click on add new user button")
        usergroup.click_add_user_group()
        log.info("Read the slider title")
        slider_title = usergroup.get_slider_title()
        log.info("Click on close slider button")
        usergroup.click_slider_close()
        assert slider_title == 'New User Group'

    @pytest.mark.regression
    @pytest.mark.usergroupmanagement
    def test_05_Create_New_User_Group(self):
        """
            Verify creation of new user group
            Validation - 1. On the basis of Created Name
            TC_ID : 005
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        global usergroupname
        usergroupname = "Ui_Automation" + action.get_current_time()
        log.info("Click on add new user button")
        usergroup.click_add_user_group()
        log.info("Add the User Group Name")
        usergroup.put_usergroup_name(usergroupname)
        log.info("Add the User Group Description")
        usergroup.put_usergroup_description("New Test User Group")
        log.info("Click on the activate toggle button")
        usergroup.click_activate_toggle()
        log.info("Enable all permession")
        usergroup.click_on_enable_all_permissions_btn()
        log.info("Click on Create button")
        usergroup.click_create_button()
        log.info("Get the toast message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        usergroup.visibility_of_first_active_usergroup()
        log.info("Validate the creation based on the Count and toast message")
        assert active_count + 1 == usergroup.get_usergroup_count()

    @pytest.mark.regression
    @pytest.mark.usergroupmanagement
    def test_06_search_usergroup(self):
        """
            Verify the Search functionality of the user group
            Validation -1 : On the basis name of the creation
            TC_ID : 006
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        action = Action(self.driver)
        log.info("Input the searching string/ Name of the User Group")
        usergroup.search_button(usergroupname)
        log.info("To get the results click Enter")
        action.click_enter()
        log.info("Validating based on the showed name")
        assert usergroupname == usergroup.get_User_Group_Name()

    @pytest.mark.regression
    @pytest.mark.usergroupmanagement
    def test_07_update_usergroup(self):
        """
            Verify the Update functionality of the User Group
            Validation -1 : Based on the Name comparison of the updated name and input name.
            TC_ID : 007
        """
        log = self.getlogger()
        usergroup = UserGroupManagement(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on the More Option")
        usergroup.click_more_option()
        log.info("Click on the Edit Option")
        usergroup.click_edit_option()
        log.info("Clear the Old User Group Name")
        usergroup.clear_usergroup_name()
        updated_user_group = "Ui_Automation" + action.get_current_time()
        log.info("Updating the New Name of the user Group")
        usergroup.put_usergroup_name(updated_user_group)
        log.info("Clearing the Old Description")
        usergroup.clear_usergroup_description()
        log.info("Adding New Description")
        usergroup.put_usergroup_description("Updated description")
        log.info("Click on the deactivate User Group Button")
        usergroup.click_deactivate_usergroup()
        log.info("Verifying based on the Button Status")
        assert usergroup.check_permission_status() == "ON"
        log.info("Click on the Update Button")
        usergroup.click_update_button()
        log.info("Get the toast message")
        toast_msg = tooltip.get_tooltip_msg()
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        log.info("Click on search button")
        usergroup.click_on_search_clear_btn()
        usergroup.page_refresh()
        log.info("Check for visibility of first active usergroup")
        usergroup.visibility_of_first_active_usergroup()
        log.info("Switch to inactive tab")
        usergroup.click_inactive_tab()
        log.info("Entering the New updated User Group Name for searching ")
        usergroup.search_button(updated_user_group)
        action.click_enter()
        log.info("Check visibility of first inactive group")
        usergroup.visibility_of_first_inactive_usergroup()
        assert updated_user_group == usergroup.get_User_Group_Name() and 'Success' in toast_msg

    @pytest.mark.regression
    @pytest.mark.usergroupmanagement
    def test_08_clone_existing_usergroup(self):
        """
            Verify the clone Functionality based on the Button in more options
            Validation-1: Verify the Button functionality and also able get the same features of the Cloned User Group
            TC_ID : 008
        """
        usergroup = UserGroupManagement(self.driver)
        action = Action(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Click on the more Option")
        usergroup.click_more_option()
        log.info("Click on the clone Button in dropdown")
        usergroup.click_clone_usergroup()
        log.info("Clearing the Default name")
        usergroup.clear_usergroup_name()
        cloned_usergroup = "Ui_Automation_Clone" + action.get_current_time()
        log.info("Update the New Created Name")
        usergroup.put_usergroup_name(cloned_usergroup)
        log.info("Clear the Description")
        usergroup.clear_usergroup_description()
        log.info("Update the New description")
        usergroup.put_usergroup_description("Cloned")
        log.info("Click on the create button")
        usergroup.click_create_button()
        log.info("Get the toast message")
        toast_msg = tooltip.get_tooltip_msg()
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        log.info("Click on search button")
        usergroup.click_on_search_clear_btn()
        log.info("Searching based on changed name")
        usergroup.search_button(cloned_usergroup)
        action.click_enter()
        usergroup.visibility_of_first_inactive_usergroup()
        assert cloned_usergroup == usergroup.get_User_Group_Name() \
               and 'Success' in toast_msg
