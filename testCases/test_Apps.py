import time

import pytest

from pageObjects.MyApps import MyApps
from pageObjects.Navigation import Navigation
from pageObjects.Playbooks import Playbooks
from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestApps(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
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
        log.info("Check if walk through is initiated")
        my_apps.click_on_close_walkthrough()
        assert action.get_title() == 'My Apps | Cyware Orchestrate' and page_heading == 'Apps'

    @pytest.mark.regression
    def test_02_Create_New_Custom_App(self):
        """
            Verify user is able to create a new app manually
            Validation - 1. By check count increase under My apps
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Get the count of total apps before app creation")
        count_of_app_before_creation = my_apps.get_app_count()
        log.info("Click on App create button")
        my_apps.Create_App_button()
        log.info("Enter app name")
        global new_app_name
        new_app_name = "newapp" + action.get_random_digit()
        my_apps.enter_app_name(new_app_name)
        log.info("Enter app supported api version")
        my_apps.enter_supported_api_version("1.0.0")
        log.info("Click on refresh button")
        my_apps.click_app_refresh_button()
        log.info("Click on close tool tip")
        my_apps.close_tooltip()
        log.info("Click on active app")
        my_apps.click_active_app()
        log.info("Click on app save button")
        my_apps.click_save_app_button()
        log.info("Click on close tool tip")
        my_apps.close_tooltip()
        log.info("Check visibility of 1st app")
        my_apps.visibility_of_first_app()
        count_of_app_after_creation = my_apps.get_app_count()
        assert count_of_app_before_creation + 1 == count_of_app_after_creation

    @pytest.mark.regression
    def test_03_Search_Manual_Created_App(self):
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
    def test_04_App_Detail_for_Custom_Created(self):
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
        assert page_title == 'App Summary | Cyware Orchestrate' and searched_app_title == app_title_summary

    @pytest.mark.regression
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
    def test_07_Create_New_Instance_for_Custom_Created_App(self):
        """
            Verify user is able to new instance.
            Validation - 1. By check presence of created instance's title on page
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Click on new instance button")
        my_apps.click_on_new_instance_btn()
        log.info("Enter the instance name")
        my_apps.enter_instance_name('test')
        log.info("Enter the instance description")
        my_apps.enter_instance_description('test')
        log.info("Click on instance create button")
        my_apps.click_slider_instance_create_btn()
        log.info("Click on close tool tip")
        my_apps.close_tooltip()
        assert my_apps.read_default_instance() == 'test'

    @pytest.mark.regression
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
    @pytest.mark.readOnly
    def test_09_clone_custom_app_and_uninstall(self):
        """
        Verify user is able to clone the custom app
        Validation-1:  Based on the redirection to edit mode page with clone title
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        action = Action(self.driver)
        log.info("Navigate back to listing page")
        my_apps.click_back_btn()
        log.info("Mouse hover on the more options button")
        my_apps.mouse_hover_list_more_options()
        log.info("Click on the clone button")
        my_apps.click_clone_app_btn()
        log.info("Read page heading")
        page_heading = my_apps.get_clone_page_heading()
        assert action.get_title() == 'Clone App | Cyware Orchestrate' and 'Clone App' in page_heading
        log.info("Read cloned app name")
        global cloned_app_name
        cloned_app_name = my_apps.get_cloned_app_name()
        log.info("Click on active app")
        my_apps.click_active_app()
        log.info("CLick on save button")
        my_apps.click_save_app_button()
        log.info("Close the tool tip")
        my_apps.close_tooltip()
        log.info("Clear the search bar")
        my_apps.click_clear_search_btn()
        log.info("Search the cloned app")
        my_apps.search_for_app(cloned_app_name)
        log.info("Search the app which is created new manually")
        assert cloned_app_name == my_apps.top_first_search(cloned_app_name)
        my_apps.mouse_hover_list_more_options()
        log.info("Click on uninstall app")
        my_apps.click_on_uninstall_app()
        log.info("Click on confirm button to uninstall app")
        my_apps.click_confirm_uninstall_app()


    @pytest.mark.regression
    def test_09_Uninstall_Custom_Created_App(self):
        """
            Verify user is able to uninstall app
            Validation - 1. On the basis of search same app
                         2. On the basis of tooltip after successful uninstall
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Clear the search bar")
        my_apps.click_clear_search_btn()
        log.info("Search the cloned app")
        my_apps.search_for_app(new_app_name)
        log.info("Mouse hover to more options")
        my_apps.mouse_hover_list_more_options()
        log.info("Click on uninstall app")
        my_apps.click_on_uninstall_app()
        log.info("Click on confirm button to uninstall app")
        my_apps.click_confirm_uninstall_app()
        log.info("Validating app uninstalled successfully or not")
        tooltip_message = my_apps.read_app_uninstall_success_message()
        search_result_message = my_apps.get_search_result_after_uninstall()
        log.info("Click on close tool tip")
        my_apps.close_tooltip()
        log.info("Clear the search result")
        my_apps.click_clear_search_btn()
        assert tooltip_message == 'App deleted successfully.' and search_result_message == 'No Results Found'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_10_Verify_App_Store_switch_tab(self):
        """
            Verify user is able to switch from My apps to App Store
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on App Store tab")
        myapps.app_store_tab()
        log.info("Check if walk through is initiated")
        myapps.click_on_close_walkthrough()
        assert action.get_title() == 'Appstore | Cyware Orchestrate'


    @pytest.mark.regression
    def test_11_install_app_from_app_store(self):
        """
        Verify user is able to install the cyware published app or not
        Validation 1: Based on the installed text visibility
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Apply pagination if install button not found and Scroll to install button view if found")
        my_apps.scroll_to_install_btn_view()
        log.info("Read the app name")
        global app_name
        app_name = my_apps.get_installing_app_name()
        log.info("Click on install button")
        my_apps.click_on_install_btn()
        log.info("Check whether slider is visible or not")
        assert my_apps.get_install_app_slider_title() == app_name
        log.info("Click on install button in slider")
        my_apps.click_slider_install_btn()
        log.info("Verify whether success tooltip is visible after installing")
        tooltip_msg = my_apps.get_install_successful_tooltip_txt()
        log.info("Close successful tooltip")
        my_apps.close_tooltip()
        assert 'success' or 'Successful' in tooltip_msg

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_12_Verify_My_Apps_switch_tab(self):
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
    def test_13_Verify_installed_app(self):
        """
        Verify whether installed app is coming under my apps tab
        Validation: Based on the search result
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        my_apps.My_Apps_Tab()
        log.info("Search for the app")
        my_apps.search_for_app(app_name)
        log.info("Search the app which is installed")
        search_result = my_apps.top_first_search(app_name)
        log.info("Clear the search result")
        my_apps.click_clear_search_btn()
        assert app_name == search_result






