import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.DataSync import DataSync
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestDataSync(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_data_sync_redirection(self):
        """
            Verify Data Sync redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Data_Sync())
        assert action.getTitle() == 'Data Sync Jobs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_create_data_sync(self):
        """
            Verify creation of new data sync job from Main Menu
            Validation -1. On the basis of Page title
        """
        log = self.getlogger()
        dataSync = DataSync(self.driver)
        action = Action(self.driver)
        log.info('Click on create data sync button')
        time.sleep(ReadConfig.MediumsleepWait())
        action.javascript_click_element(dataSync.click_create_data_sync())
        log.info('Store the page title in page_title variable for validation')
        page_title = action.getTitle()
        log.info('click on back button to cancel the data sync job creation')
        action.click(dataSync.click_back_button())
        log.info('click on close without saving button to cancel the data sync job creation')
        action.click(dataSync.click_confirm_close())
        log.info('validation based on the page title')
        assert page_title == 'Create Data Sync Policy | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_switch_run_history(self):
        """
            Verify switch from Data Sync to Run History Logs
            Validation - 1. On the basis of Window's title
        """
        dataSync = DataSync(self.driver)
        action = Action(self.driver)
        action.click(dataSync.click_run_history())
        assert action.getTitle() == 'Run History Logs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_job_details_data_Sync(self):
        """
            Verify switch from Run History Logs to Data Sync Job details
            Validation - 1. On the basis of Window's title
        """
        dataSync = DataSync(self.driver)
        action = Action(self.driver)
        time.sleep(ReadConfig.sleepWait())
        action.click(dataSync.click_job_details())
        assert action.getTitle() == 'Data Sync Jobs | Cyware Orchestrate'
