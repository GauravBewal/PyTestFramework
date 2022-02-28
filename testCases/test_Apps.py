import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from configuration.readConfiguration import ReadConfig
from pageObjects.MyApps import MyApps
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestApps(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_Apps_redirection(self):
        """
            Verify Apps redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on Main Menu")
        nav.click_Main_Menu()
        log.info("Click on Apps from Menu")
        nav.Navigate_Apps()
        log.info("Read page heading")
        page_heading = myapps.get_page_heading()
        assert action.getTitle() == 'My Apps | Cyware Orchestrate' and page_heading == 'Apps'

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_02_My_Apps_close_automatic_walkthrough(self):
        """
            close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        myapps = MyApps(self.driver)
        log.info("Check if walk through is initiated")
        myapps.click_on_close_walkthrough()

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_App_Store_switch_tab(self):
        """
            Verify user is able to switch from My apps to App Store
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on App Store tab")
        myapps.App_Store_Tab()
        assert action.getTitle() in 'Appstore | Cyware Orchestrate'

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_04_Cyware_Apps_close_automatic_walkthrough(self):
        """
            close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        myapps = MyApps(self.driver)
        log.info("Check if walk through is initiated")
        myapps.click_on_close_walkthrough()

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Verify_My_Apps_switch_tab(self):
        """
            Verify user is able to switch from App Store to My Apps
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on App Store tab")
        myapps.My_Apps_Tab()
        assert action.getTitle() in 'My Apps | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_06_Create_New_Custom_App(self):
        """
            Verify user is able to create a new app manually
            Validation - 1. By check count increase under My apps
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Get the count of total apps before app creation")
        count_of_app_before_creation = myapps.get_app_count()
        log.info("Click on App create button")
        myapps.Create_App_button()
        log.info("Enter app name")
        global new_app_name
        new_app_name = "newapp" + action.getRandomDigit()
        myapps.enter_app_name(new_app_name)
        log.info("Enter app supported api version")
        myapps.enter_supported_api_version("1.0.0")
        log.info("Click on refresh button")
        myapps.click_app_refresh_button()
        log.info("Click on close tool tip")
        myapps.close_tooltip()
        log.info("Click on active app")
        myapps.click_active_app()
        log.info("Click on app save button")
        myapps.click_save_app_button()
        log.info("Click on close tool tip")
        myapps.close_tooltip()
        time.sleep(ReadConfig.Wait_3_Sec())
        count_of_app_after_creation = myapps.get_app_count()
        assert count_of_app_before_creation + 1 == count_of_app_after_creation

    @pytest.mark.smoke
    def test_07_Search_Manual_Created_App(self):
        """
            Verify user is able to search new manually created app.
            Validation - 1. search the app which is created new manually.
        """
        log = self.getlogger()
        myapps = MyApps(self.driver)
        myapps.click_on_app_search(new_app_name)
        log.info("Search the app which is created new manually")
        assert new_app_name == myapps.top_first_search(new_app_name)

    @pytest.mark.smoke
    def test_08_App_Detail_for_Custom_Created(self):
        """
            Verify the app detail page redirection
            Validation - 1. On the basis of Window's title
                         2. app title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        app_title_listing = myapps.top_first_search(new_app_name)
        log.info("Click on the searched app")
        myapps.click_first_search_result()
        page_title = action.getTitle()
        app_title_summary = myapps.read_app_title()
        assert page_title == 'App Summary | Cyware Orchestrate' and app_title_listing == app_title_summary

    @pytest.mark.smoke
    def test_09_Verify_Switch_App_Actions_tab(self):
        """
            Verify user is able to switch app action tab
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on actions tab")
        my_apps.click_app_actions_tab()
        page_title = action.getTitle()
        assert page_title == 'App Actions | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_10_Verify_Switch_App_Instances_tab(self):
        """
            Verify user is able to switch on Instance App tab
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on instance tab")
        my_apps.click_app_instance_tab()
        page_title = action.getTitle()
        assert page_title == 'App Instances | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_11_Create_New_Instance_for_Custom_Created_App(self):
        """
            Verify user is able to new instance.
            Validation - 1. By check presence of created instance's title on page
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Click on new instance button")
        my_apps.click_on_new_instance()
        my_apps.enter_instance_name('test')
        my_apps.enter_instance_description('test')
        my_apps.click_instance_creation()
        assert my_apps.read_default_instance() == 'test'

    @pytest.mark.smoke
    def test_12_Verify_Switch_Playbook_tab(self):
        """
            Verify user is able to switch to playbook tab.
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on playbook tab")
        my_apps.click_app_playbooks_tab()
        page_title = action.getTitle()
        assert page_title == 'App Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_13_Uninstall_Custom_Created_App(self):
        """
            Verify user is able to uninstall app
            Validation - 1. On the basis of search same app
                         2. On the basis of tooltip after successful uninstall
        """
        log = self.getlogger()
        my_apps = MyApps(self.driver)
        log.info("Mouse hover to more options")
        my_apps.mouse_hover_on_more_Actions()
        log.info("Click on uninstall app")
        my_apps.click_on_uninstall_app()
        log.info("Click on confirm button to uninstall app")
        my_apps.click_confirm_uninstall_app()
        log.info("Validating app uninstalled successfully or not")
        tooltip_message = my_apps.read_app_uninstall_success_message()
        search_result_message = my_apps.get_search_result_after_uninstall()
        assert tooltip_message == 'App deleted successfully.' and search_result_message == 'No Results Found'
