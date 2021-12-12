import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.AppStore import AppStore
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestApps(Base):

    @pytest.mark.smoke
    def test_01_apps_redirection(self):
        """
            Verify Apps redirection from Main Menu
            Validation - 1. On the basis of Window title
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
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        appStore = AppStore(self.driver)
        log.info("Click on App Store tab")
        action.click(appStore.App_Store_Tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'App-store | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_03_My_Apps_switch_tab(self):
        """
            Verify user is able to switch from App Store to My Apps
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        appstore = AppStore(self.driver)
        log.info("Click on App Store tab")
        action.click(appstore.My_Apps_Tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'App(s) | Cyware Orchestrate'


