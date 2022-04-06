import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.MyApps import MyApps
from pageObjects.Navigation import Navigation
from pageObjects.CommonElements import Tooltip
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestApps(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.apps
    def test_01_Verify_Apps_redirection(self):
        """
            Verify Apps redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on Main Menu")
        nav.click_main_menu()
        log.info("Click on Apps from Menu")
        nav.navigate_apps()
        log.info("Read page heading")
        page_heading = my_apps.get_page_heading()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'My Apps | Cyware Orchestrate' and page_heading == 'Apps' \
               and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.apps
    def test_02_Create_new_custom_app(self):
        """
            Verify user is able to create a new app manually
            Validation - 1. By check count increase under My apps
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Check if walk through is initiated")
        my_apps.click_on_close_walkthrough()
        log.info("Click on App create button")
        my_apps.Create_App_button()
        log.info("Enter app name")
        global new_app_name
        new_app_name = "newapp" + action.get_random_digit(5)
        my_apps.enter_app_name(new_app_name)
        log.info("Enter app supported api version")
        my_apps.enter_supported_api_version("1.0.0")
        log.info("Click on refresh button")
        my_apps.click_app_refresh_button()
        log.info("Read the tooltip msg")
        toast_msg_1 = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("Click on active app")
        my_apps.click_active_app()
        log.info("Click on app save button")
        my_apps.click_save_app_button()
        log.info("Read the tooltip msg")
        toast_msg_2 = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("Check visibility of 1st app")
        my_apps.visibility_of_first_app()
        assert 'Success' == toast_msg_1 and 'Success' == toast_msg_2

    @pytest.mark.regression
    @pytest.mark.apps
    def test_03_Search_for_App(self):
        """
            Verify user is able to search new manually created app.
            Validation - 1. search the app which is created new manually.
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        my_apps.search_for_app(new_app_name)
        log.info("Search the app which is created new manually")
        assert new_app_name == my_apps.top_first_search(new_app_name)

    @pytest.mark.regression
    @pytest.mark.apps
    def test_04_Verify_App_Detail_Page_Navigation(self):
        """
            Verify the app detail page redirection
            Validation - 1. On the basis of Window's title
                         2. app title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        searched_app_title = my_apps.top_first_search(new_app_name)
        log.info("Click on the searched app")
        my_apps.click_first_search_result()
        page_title = action.get_title()
        app_title_summary = my_apps.read_app_title()
        assert page_title == 'App Summary | Cyware Orchestrate' \
               and searched_app_title == app_title_summary

    @pytest.mark.regression
    @pytest.mark.apps
    def test_05_Verify_Switch_App_Actions_tab(self):
        """
            Verify user is able to switch app action tab
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on actions tab")
        my_apps.click_app_actions_tab()
        page_title = action.get_title()
        assert page_title == 'App Actions | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.apps
    def test_06_Verify_Switch_App_Instances_tab(self):
        """
            Verify user is able to switch on Instance App tab
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on instance tab")
        my_apps.click_app_instance_tab()
        page_title = action.get_title()
        assert page_title == 'App Instances | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.apps
    def test_07_Create_New_Instance_for_Custom_Created_App(self):
        """
            Verify user is able to new instance.
            Validation - 1. By check presence of created instance's title on page
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on new instance button")
        my_apps.click_on_new_instance_btn()
        log.info("Enter the instance name")
        my_apps.enter_instance_name('test')
        log.info("Enter the instance description")
        my_apps.enter_instance_description('test')
        log.info("Click on instance create button")
        my_apps.click_slider_instance_create_btn()
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        assert 'Success' == toast_msg and my_apps.read_default_instance() == 'test'


    @pytest.mark.regression
    @pytest.mark.apps
    def test_08_Verify_Switch_Playbook_tab(self):
        """
            Verify user is able to switch to playbook tab.
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on playbook tab")
        my_apps.click_app_playbooks_tab()
        page_title = action.get_title()
        assert page_title == 'App Playbooks | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.apps
    def test_09_Clone_Custom_App_and_Uninstall(self):
        """
        Verify user is able to clone the custom app
        Validation-1:  Based on the redirection to edit mode page with clone title
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Navigate back to listing page")
        my_apps.click_back_btn()
        log.info("Mouse hover on the more options button")
        my_apps.mouse_hover_list_more_options()
        log.info("Check for visibility of clone app button")
        my_apps.visibility_of_clone_app_btn()
        log.info("Click on the clone button")
        my_apps.click_clone_app_btn()
        log.info("Switch to new tab")
        parent = my_apps.switch_new_tab()
        log.info("Read page heading")
        page_heading = my_apps.get_clone_page_heading()
        log.info("Read cloned app name")
        global cloned_app_name
        cloned_app_name = my_apps.get_cloned_app_name()
        log.info("Click on active app")
        my_apps.click_active_app()
        log.info("CLick on save button")
        my_apps.click_save_app_button()
        log.info("Read the tooltip msg")
        toast_msg_1 = tooltip.read_tooltip_msg()
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        log.info("Switch back to parent window")
        my_apps.switch_back_parent_window(parent)
        log.info("Clear the search bar")
        my_apps.click_clear_search_btn()
        log.info("Search the cloned app")
        my_apps.search_for_app(cloned_app_name)
        log.info("Search the app which is created new manually")
        search_result = my_apps.top_first_search(cloned_app_name)
        my_apps.mouse_hover_list_more_options()
        log.info("Click on uninstall app")
        my_apps.click_on_uninstall_app()
        log.info("Click on confirm button to uninstall app")
        my_apps.click_confirm_uninstall_app()
        log.info("Read the tooltip msg")
        toast_msg_2 = tooltip.read_tooltip_msg()
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        assert 'Clone App' in page_heading and 'Success' == toast_msg_1 \
               and cloned_app_name == search_result and 'Success' == toast_msg_2

    @pytest.mark.regression
    @pytest.mark.apps
    def test_10_Verify_Custom_App_Edit(self):
        """
        Verify user is able to edit the custom app
        Validation -1: Based on the page title
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Clear the search bar")
        my_apps.click_clear_search_btn()
        log.info("Search the cloned app")
        my_apps.search_for_app(new_app_name)
        log.info("Mouse hover to more options")
        my_apps.mouse_hover_list_more_options()
        log.info("Visibility of edit app button")
        my_apps.visibility_of_edit_button()
        log.info("Click on the edit app button")
        my_apps.click_on_edit_btn()
        log.info("Read page heading")
        page_heading = my_apps.get_edit_app_heading()
        my_apps.click_save_app_button()
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        assert new_app_name == page_heading and 'Success' == toast_msg

    @pytest.mark.regression
    @pytest.mark.apps
    def test_11_Export_Custom_Created_App(self):
        """
        Verify user is able to export the app or not
        Validation -1: Based on the file downloaded
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Mouse hover to more options")
        my_apps.mouse_hover_list_more_options()
        log.info("Visibility of export app button")
        my_apps.visibility_of_export_btn()
        log.info("Click on the edit app button")
        my_apps.click_on_export_btn()
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        assert new_app_name in my_apps.check_file_downloaded_and_get_file_directory_path(new_app_name, 'zip')\
               and 'Success' == toast_msg

    @pytest.mark.regression
    @pytest.mark.apps
    def test_12_Uninstall_Custom_Created_App(self):
        """
            Verify user is able to uninstall app
            Validation - 1. On the basis of search same app
                         2. On the basis of tooltip after successful uninstall
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Mouse hover to more options")
        my_apps.mouse_hover_list_more_options()
        log.info("Check visibility of uninstall app button")
        my_apps.visibility_of_uninstall_btn()
        log.info("Click on uninstall app")
        my_apps.click_on_uninstall_app()
        log.info("Click on confirm button to uninstall app")
        my_apps.click_confirm_uninstall_app()
        log.info("Validating app uninstalled successfully or not")
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        search_result_message = my_apps.get_search_result_after_uninstall()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("Clear the search result")
        my_apps.click_clear_search_btn()
        log.info("Wait till visibility of first app")
        my_apps.visibility_of_first_app()
        assert toast_msg == 'Success' and search_result_message == 'No Results Found'


    @pytest.mark.regression
    @pytest.mark.apps
    def test_13_Import_Custom_App(self):
        """
        Verify user is able to import the custom app
        Validation-1 : Based on the imported successful message
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Get the exact app location")
        app_name = my_apps.check_file_downloaded_and_get_file_directory_path(new_app_name, 'zip')
        app_path = my_apps.get_file_downloaded_path(app_name)
        log.info("send app file location to import button")
        my_apps.send_file_path_to_upload_input_field(app_path)
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("Deleting the downloaded file")
        my_apps.delete_downloaded_file(app_path)
        assert 'Success' == toast_msg
        log.info("search for the imported app")
        my_apps.search_for_app(new_app_name)
        log.info("Wait until visibility of installed app")
        my_apps.visibility_of_first_app()
        self.test_12_Uninstall_Custom_Created_App()



    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.apps
    def test_14_Uninstall_imported_app_and_switch_to_appstore(self):
        """
            Verify user is able to switch from My apps to App Store
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on App Store tab")
        myapps.app_store_tab()
        log.info("Check if walk through is initiated")
        myapps.click_on_close_walkthrough()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'Appstore | Cyware Orchestrate' \
               and error_msg_visibility is False


    @pytest.mark.regression
    @pytest.mark.apps
    def test_15_Clone_CFTR_App_to_Debug(self):
        """
        Verify user is able to clone the cyware published app
        Validation-1: Based on the app visibility and success message
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        global app_name
        app_name = "Cyware Fusion and Threat Response (CFTR)"
        log.info("Search for app")
        my_apps.search_for_app(app_name)
        my_apps.top_first_search(app_name)
        log.info("Check whether app is installed or not")
        my_apps.Verify_app_installed_or_not()
        log.info("Mouse hover on the more options button")
        my_apps.mouse_hover_list_more_options()
        my_apps.visibility_of_clone_app_btn()
        log.info("Click on the clone button")
        my_apps.click_clone_app_btn()
        log.info("Click on slider clone button")
        my_apps.click_clone_btn_on_slider()
        log.info("Switch to new tab")
        parent = my_apps.switch_new_tab()
        log.info("Read page heading")
        page_heading = my_apps.get_clone_page_heading()
        log.info("Read cloned app name")
        global cloned_cyware_app_name
        cloned_cyware_app_name = my_apps.get_cloned_app_name()
        log.info("Click on refresh button")
        my_apps.click_app_refresh_button()
        log.info("Read the tooltip msg")
        toast_msg_1 = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("Click on active app")
        my_apps.click_active_app()
        log.info("CLick on save button")
        my_apps.click_save_app_button()
        log.info("Read the tooltip msg")
        toast_msg_2 = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("Switch back to parent")
        my_apps.switch_back_parent_window(parent)
        log.info("Clear search bar")
        my_apps.click_clear_search_btn()
        my_apps.visibility_of_first_app()
        log.info("Switch to active tab")
        my_apps.My_Apps_Tab()
        log.info("Search the cloned app")
        my_apps.search_for_app(cloned_cyware_app_name)
        log.info("Search the app which is created new manually")
        assert cloned_cyware_app_name == my_apps.top_first_search(cloned_cyware_app_name) \
               and 'Clone App' in page_heading and 'Success' == toast_msg_1 and 'Success' == toast_msg_2

    @pytest.mark.regression
    @pytest.mark.apps
    def test_16_Verify_Debugging_App(self):
        """
        Verify user is able to debug the cyware published app by cloning it
        Validation 1: Based on the result
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on the cloned app")
        my_apps.click_first_search_result()
        log.info("Navigate to instance tab and create the instance")
        log.info("Navigate to instance tab")
        my_apps.click_app_instance_tab()
        log.info("create new instance")
        my_apps.click_on_new_instance_btn()
        log.info("Enter Instance name")
        global instance_name
        instance_name = "ui_automation" + action.get_current_time()
        my_apps.enter_instance_name(instance_name)
        log.info("Enter base url")
        my_apps.enter_cftr_base_url(ReadConfig.cftr_baseurl())
        log.info("Enter Access id")
        my_apps.enter_cftr_access_key(ReadConfig.cftr_access_key())
        log.info("Enter Secret Key")
        my_apps.enter_cftr_secret_key(ReadConfig.cftr_secret_key())
        log.info("Click on create instance button")
        my_apps.click_slider_instance_create_btn()
        log.info("Read the tooltip msg")
        toast_msg_1 = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        # log.info("Mouse hover on the created instance")
        # my_apps.mouse_hover_on_created_instance(instance_name)
        # log.info("Click on test instance button")
        # my_apps.click_on_test_instance_btn()
        # log.info("Check visibility of successful test connectivity")
        # successful_visibility = my_apps.visibility_of_successful_test_connectivity()
        # assert successful_visibility is True
        # log.info("Click ont instance connectivity slider close")
        # my_apps.click_instance_connectivity_slider_close()
        log.info("Mouser hover on the more actions")
        my_apps.mouse_hover_on_more_Actions()
        log.info("Click on the edit button")
        my_apps.click_on_edit_btn()
        log.info("Click on the run button")
        my_apps.click_on_run_btn()
        log.info("Click on the instance field")
        my_apps.click_on_instance_field()
        log.info("Select the created instance from drop down")
        my_apps.select_created_instance(instance_name)
        log.info("Click on the action field")
        my_apps.click_on_action_field()
        log.info("Select the create incident action from drop down")
        my_apps.click_on_create_incident_action_name()
        log.info("Enter the incident title")
        my_apps.put_incident_title_field_value("UI Automation")
        log.info("Enter the incident status")
        my_apps.put_incident_status("untriaged")
        log.info("Enter the incident description")
        my_apps.put_incident_description("UI Automation")
        log.info("Enter the severity level")
        my_apps.put_incident_severity_level("low")
        log.info("Click on the debug button")
        my_apps.click_on_debug_test_btn()
        debug_console_data = my_apps.get_debug_console_status()
        debug_result_data = my_apps.get_debug_result_data()
        my_apps.click_save_app_button()
        log.info("Read the tooltip msg")
        toast_msg_2 = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        assert 'Success' == toast_msg_1 and 'SUCCESS' == debug_console_data \
               and '"status": 201' in debug_result_data and 'Success' == toast_msg_2

    @pytest.mark.regression
    @pytest.mark.apps
    def test_17_Uninstall_Debugged_App(self):
        """
        Verify whether user is able to uninstall the debugged app
        Validation-1: Based on
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        self.test_12_Uninstall_Custom_Created_App()


    @pytest.mark.regression
    @pytest.mark.apps
    def test_18_Install_App_from_App_Store(self):
        """
        Verify user is able to install the cyware published app or not
        Validation 1: Based on the installed text visibility
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        my_apps.app_store_tab()
        my_apps.visibility_of_first_app()
        log.info("Apply pagination if install button not found and Scroll "
                 "to install button view if found")
        my_apps.scroll_to_install_btn_view()
        log.info("Read the app name")
        global available_app_name
        available_app_name = my_apps.get_installing_app_name()
        log.info("Enter the app name to search")
        my_apps.search_for_app(available_app_name)
        log.info("Click on install button")
        my_apps.click_on_install_btn()
        log.info("Check install app slider title is same as installing app name")
        assert my_apps.get_install_app_slider_title() == available_app_name
        log.info("Click on install button in slider")
        my_apps.click_slider_install_btn()
        log.info("Verify whether success tooltip is visible after installing")
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Click on close tool tip")
        tooltip.click_close_tooltip()
        log.info("clear search bar")
        my_apps.click_clear_search_btn()
        log.info("Wait till visibility of first app")
        my_apps.visibility_of_first_app()
        assert 'Success' == toast_msg

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.apps
    def test_19_Verify_My_Apps_Switch_tab(self):
        """
            Verify user is able to switch from App Store to My Apps
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on App Store tab")
        myapps.My_Apps_Tab()
        log.info("Check visibility of 1st app")
        myapps.visibility_of_first_app()
        assert action.get_title() == 'My Apps | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.apps
    def test_20_Verify_Installed_App(self):
        """
        Verify whether installed app is coming under my apps tab
        Validation: Based on the search result
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Search for the app")
        my_apps.search_for_app(available_app_name)
        log.info("Search the app which is installed")
        search_result = my_apps.top_first_search(available_app_name)
        assert available_app_name == search_result

    @pytest.mark.regression
    @pytest.mark.apps
    def test_21_Export_Cyware_App(self):
        """
        Verify whether user is able to export the cyware app
        Validation-1: Based on the successful message
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Mouse hover to more options")
        my_apps.mouse_hover_list_more_options()
        log.info("Visibility of export app button")
        my_apps.visibility_of_export_btn()
        log.info("Click on the export app button")
        my_apps.click_on_export_btn()
        if my_apps.visibility_of_export_app_slider() is True:
            log.info("Since slider is visible clicking on export app button")
            my_apps.click_on_export_app_btn()
            log.info("Click on slider close button")
            my_apps.click_on_slider_close_btn()
        global first_3_app_letters
        first_3_app_letters = my_apps.get_first_3_letter_of_downloaded_app(available_app_name)
        assert first_3_app_letters in my_apps.check_file_downloaded_and_get_file_directory_path(first_3_app_letters,
                                                                                                'zip')

    @pytest.mark.regression
    @pytest.mark.apps
    def test_22_Uninstall_Installed_Cyware_App(self):
        """
        Verify whether user is able to uninstall the cyware installed app
        Validation-1: Based on the uninstallation successful message
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("click on search field")
        my_apps.click_on_Search_bar()
        log.info("Uninstalling the installed cyware app")
        self.test_12_Uninstall_Custom_Created_App()

    @pytest.mark.regression
    @pytest.mark.apps
    def test_23_Import_Cyware_App(self):
        """
        Verify user is able to import the installed cyware app
        Validation-1: Based on the successful message
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Get the exact app location")
        app_name = my_apps.check_file_downloaded_and_get_file_directory_path(first_3_app_letters, 'zip')
        app_path = my_apps.get_file_downloaded_path(app_name)
        log.info("send app file location to import button")
        my_apps.send_file_path_to_upload_input_field(app_path)
        log.info("Read the tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        log.info("Deleting the downloaded file")
        my_apps.delete_downloaded_file(app_path)
        log.info("Search for the app")
        my_apps.search_for_app(available_app_name)
        log.info("Wait until visibility of first app")
        my_apps.visibility_of_first_app()
        assert 'Success' == toast_msg
        log.info("Uninstall the imported app")
        self.test_12_Uninstall_Custom_Created_App()

    @pytest.mark.regression
    @pytest.mark.apps
    def test_24_Switch_to_List_View(self):
        """
        Verify user is able to switch to list view
        Validation-1: Based on the app view visibility
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("click on the list view button")
        my_apps.click_on_list_view_btn()
        list_view_visibility = my_apps.visibility_of_app_in_list_view()
        assert list_view_visibility is True
