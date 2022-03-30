import pytest

from pageObjects.Navigation import Navigation
from pageObjects.UserManagement import UserManagement
from pageObjects.UserGroupManagement import UserGroupManagement
from pageObjects.Webhooks import Webhooks
from pageObjects.CommonElements import Tooltip
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
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count + active_count

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

    @pytest.mark.regression
    def test_06_Create_New_User(self):
        """
            Verify the Create a New User
            Validation -1 : On the basis of the Count in the Active Tab
            TC_ID : 006
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Redirect to the Active Tab")
        user.click_active_tab()
        log.info("Click On add new User Button")
        user.click_add_user()
        First_Name = "TestUser"
        Last_Name = action.get_current_time()
        global Full_Name
        Full_Name = First_Name + " " + Last_Name
        User_Name = First_Name + "." + str(all_tab_count)
        log.info("Add the First Name of User")
        user.put_first_name(First_Name)
        log.info("Add the Last Name of User")
        user.put_last_name(Last_Name)
        log.info("Select the First Active User Group")
        user.click_dropdown()
        user.click_top_user_group()
        log.info("Add the User Name for User")
        user.put_user_name(User_Name.lower())
        User_email = "testuser" + "." + str(all_tab_count) + "@cyware.com"
        log.info("Add the User Email Id")
        user.put_user_email(User_email)
        log.info("Adding as the Bot User")
        user.check_bot_user()
        log.info("Click On create Button")
        user.click_create_user_btn()
        log.info("Click on the close tool tip")
        toast_msg = tooltip.get_tooltip_msg()
        assert "Success" in toast_msg
        tooltip.click_close_tooltip()
        log.info("Wait until the Visibility of the User")
        user.visibility_of_first_active_user()
        assert active_count + 1 == user.get_user_count()

    @pytest.mark.regression
    def test_07_Search_User(self):
        """
                Verify the Search Functionality of the User
                Validation -1 : This is the search functionality of the based on Name comparsion
                TC_ID : 007
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        action = Action(self.driver)
        log.info("Enter the Name to be Searched")
        user.search_button(Full_Name)
        log.info("Click Enter to Search the result")
        action.click_enter()
        log.info("Wait until the first User Name Visibility")
        user.visibility_of_first_active_user()
        log.info("Get the First Name of search list and compare the Name")
        assert Full_Name == user.get_first_list_name()

    @pytest.mark.regression
    def test_08_Update_User_Name(self):
        """
                Verify the Update Functionality of the User
                Validation -1 : Check the Updated name in the Listing Page
                Tc_ID : 008
        """
        log = self.getlogger()
        action = Action(self.driver)
        user = UserManagement(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click On First List User")
        user.click_first_list_user()
        log.info("Clear the First Name")
        user.clear_first_name()
        updated_first_name = "TestUser"
        log.info("Add the New Updated First Name")
        user.put_first_name(updated_first_name)
        log.info("Clear the Last Name Field")
        user.clear_last_name()
        updated_last_name = action.get_current_time()
        user.put_last_name(updated_last_name)
        user.click_update_btn()
        log.info("Get the Toast Message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        tooltip.click_close_tooltip()
        log.info("Clear the Search Field")
        user.click_on_search_clear_btn()
        log.info("Wait until the Visibility of the First User")
        user.visibility_of_first_active_user()
        global Updated_Full_Name
        Updated_Full_Name = updated_first_name + " " + updated_last_name
        user.search_button(Updated_Full_Name)
        action.click_enter()
        log.info("Check the Visibility of the User")
        user.visibility_of_first_active_user()
        assert Updated_Full_Name == user.get_first_list_name()

    @pytest.mark.regression
    def test_09_Visibility_User_in_UserGroupManagement(self):
        """
            Verification of the Created user Visible in the User Group Management while creating a User Group.
            Validation -1 : Verify the created new user is visible in the user list
            TC_ID : 009
        """
        log = self.getlogger()
        action = Action(self.driver)
        nav = Navigation(self.driver)
        user = UserManagement(self.driver)
        usergroup = UserGroupManagement(self.driver)
        log.info("Click on the Admin Button")
        nav.click_admin_menu()
        log.info("Click on the User Group Management")
        usergroup.click_user_group_management()
        assert action.get_title() == 'User Groups Management | Cyware Orchestrate'
        log.info("Click on the Add User Group / Create a new User group")
        usergroup.click_add_user_group()
        log.info("Click on User Dropdown")
        usergroup.click_dropdown_users()
        log.info("Click on the Visibility of the User Name in the list or drop down")
        assert user.visibility_of_user_in_usergroup(Updated_Full_Name) is True

    @pytest.mark.regression
    def test_10_Visibility_User_in_Webhooks(self):
        """
            Verification of the Created user Visible in the User Group Management while creating a Webhook.
            Validation -1 : Verify the created new user is visible in the Bot User List in Webhook
            TC_ID : 010
        """
        log = self.getlogger()
        action = Action(self.driver)
        nav = Navigation(self.driver)
        webhook = Webhooks(self.driver)
        user = UserManagement(self.driver)
        log.info("Click on the Admin Menu")
        nav.click_admin_menu()
        log.info("Click on Webhook Module")
        webhook.click_webhooks()
        assert action.get_title() in 'Webhooks | Cyware Orchestrate'
        log.info("Click on new Webhook")
        webhook.click_new_webhook()
        log.info("Click on the List Bot Users")
        webhook.click_on_list_user()
        log.info("Check Visibility of the User in the Webhook user Field")
        visibility = user.visibility_of_user(Updated_Full_Name)
        log.info("Redirect to the User Management")
        nav.click_admin_menu()
        user.click_user_management()
        assert action.get_title() in 'User Management | Cyware Orchestrate'
        assert visibility is True

    @pytest.mark.regression
    def test_11_Deactivate_User(self):
        """
            Verify The user is able to deactivate user easily IN User Group Management
            Validation -1 : Count in inactive tab and toast message
            Tc_ID : 011
        """
        log = self.getlogger()
        user = UserManagement(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Wait until the first User Name Visibility")
        user.visibility_of_first_active_user()
        log.info("Click on the first user listed")
        user.click_first_list_user()
        log.info("Click Deactivate the User button")
        user.click_deactivate_user()
        log.info("Click on Update Button")
        user.click_update_btn()
        log.info("Get the Toast Message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        tooltip.click_close_tooltip()
        log.info("Clear Search Bar Results")
        user.click_on_search_clear_btn()
        user.page_refresh()
        log.info("Switch to inactive tab")
        user.click_inactive_tab()
        user.visibility_of_first_inactive_user()
        assert inactive_count + 1 == user.get_user_count()

    # @pytest.mark.regression
    # def test_09_Export_User_Details(self):
    #     log = self.getlogger()
    #     action = Action(self.driver)
    #     user = UserManagement(self.driver)
    #     log.info("Click on the export button")
    #     user.click_export()
    #     log.info("Click on csv option")
    #     user.click_on_csv_btn()
    #     log.info("Read the tooltip msg")
    #     toast_msg = user.get_tooltip_msg()
    #     assert "Success" in toast_msg
    #     path = action.get_file_downloaded_path(action.check_file_downloaded_and_get_file_name("Cyw", 'csv'))
    #     assert action.delete_downloaded_file(path) is True
