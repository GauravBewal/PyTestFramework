import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.MyApps import MyApps
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestApps(Base):

    global new_app_name
    new_app_name = " "

    @pytest.mark.smoke
    def test_01_apps_redirection(self):
        """
            Verify Apps redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on Main Menu")
        action.click(nav.Click_Main_Menu())
        log.info("Click on Apps from Menu")
        action.click(nav.Navigate_Apps())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'App(s) | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_02_appstore_switch_tab(self):
        """
            Verify user is able to switch from My apps to App Store
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on App Store tab")
        action.click(myapps.App_Store_Tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'App-store | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_03_my_apps_switch_tab(self):
        """
            Verify user is able to switch from App Store to My Apps
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Click on App Store tab")
        action.click(myapps.My_Apps_Tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'App(s) | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_04_create_new_app(self):
        """
            Verify user is able to create a new app manually
            Validation - 1. By check count increase under My apps
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        log.info("Get the count of total apps before app creation")
        count_of_app_before_creation = action.getCountfromString(myapps.get_app_count())
        log.info("Click on App create button")
        action.click(myapps.Create_App_button())
        log.info("Enter app name")
        global new_app_name
        new_app_name = "newapp" + action.getRandomDigit()
        action.sendKeys(myapps.enter_app_name(), new_app_name)
        log.info("Enter app supported api version")
        action.sendKeys(myapps.enter_supported_api_version(), "1.0.0")
        log.info("Click on refresh button")
        action.click(myapps.click_app_refresh_button())
        log.info("Click on close tool tip")
        action.click(myapps.close_tooltip())
        log.info("Click on active app")
        action.click(myapps.click_active_app())
        log.info("Click on app save button")
        action.click(myapps.click_save_app_button())
        time.sleep(ReadConfig.MediumsleepWait())
        log.info("Click on close tool tip")
        action.click(myapps.close_tooltip())
        time.sleep(ReadConfig.sleepWait())
        count_of_app_after_creation = action.getCountfromString(myapps.get_app_count())
        assert count_of_app_before_creation+1 == count_of_app_after_creation

    @pytest.mark.smoke
    def test_05_search_app(self):
        """
            Verify user is able to search new manually created app.
            Validation - 1. search the app which is created new manually.
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        action.sendKeys(myapps.click_on_app_search(), new_app_name)
        log.info("Search the app which is created new manually")
        time.sleep(ReadConfig.sleepWait())
        assert new_app_name == action.getText(myapps.top_first_search())

    @pytest.mark.smoke
    def test_06_app_detail(self):
        """
            Verify the app detail page redirection
            Validation - 1. On the basis of Window's title
                         2. app title
        """
        log = self.getlogger()
        action = Action(self.driver)
        myapps = MyApps(self.driver)
        app_title_listing = action.getText(myapps.top_first_search())
        log.info("Click on the searched app")
        action.click(myapps.top_first_search())
        page_title = action.getTitle()
        time.sleep(ReadConfig.sleepWait())
        app_title_summary = action.getText(myapps.read_app_title())
        assert page_title == 'App Summary | Cyware Orchestrate' and app_title_listing == app_title_summary

    @pytest.mark.smoke
    def test_07_switch_app_actions_tab(self):
        """
            Verify user is able to switch app action tab
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on actions tab")
        action.click(my_apps.click_app_actions_tab())
        page_title = action.getTitle()
        assert page_title == 'App Actions | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_08_switch_app_instance_tab(self):
        """
            Verify user is able to switch on Instance App tab
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on instance tab")
        action.click(my_apps.click_app_instance_tab())
        page_title = action.getTitle()
        assert page_title == 'App Instances | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_09_create_new_instance(self):
        """
            Verify user is able to new instance.
            Validation - 1. By check presence of created instance's title on page
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on new instance button")
        action.click(my_apps.click_on_new_instance())
        action.sendKeys(my_apps.enter_instance_name(), 'test')
        action.sendKeys(my_apps.enter_instance_description(), 'test')
        action.click(my_apps.click_instance_creation())
        assert action.getText(my_apps.read_default_instance()) == 'test'

    @pytest.mark.smoke
    def test_10_switch_playbook_tab(self):
        """
            Verify user is able to switch to playbook tab.
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Click on playbook tab")
        action.click(my_apps.click_app_playbooks_tab())
        page_title = action.getTitle()
        assert page_title == 'App Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_11_uninstall_app(self):
        """
            Verify user is able to uninstall app
            Validation - 1. On the basis of search same app
                         2. On the basis of tooltip after successful uninstall
        """
        log = self.getlogger()
        action = Action(self.driver)
        my_apps = MyApps(self.driver)
        log.info("Mouse hover to more options")
        action.mouse_hover_on_element(my_apps.mouse_hover_on_more_Actions())
        log.info("Click on uninstall app")
        action.click(my_apps.click_on_uninstall_app())
        log.info("Click on confirm button to uninstall app")
        action.click(my_apps.click_confirm_uninstall_app())
        time.sleep(ReadConfig.sleepWait())
        log.info("Validating app uninstalled successfully or not")
        tooltip_message = action.getText(my_apps.read_app_uninstall_success_message())
        search_result_message = action.getText(my_apps.get_search_result_after_uninstall())
        assert tooltip_message == 'App deleted successfully.' and search_result_message == 'No Results Found'
