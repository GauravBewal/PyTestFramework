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
    def test_01_Verify_Data_Sync_redirection(self):
        """
            Verify Data Sync redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        dataSync = DataSync(self.driver)
        nav.click_Main_Menu()
        nav.Navigate_Data_Sync()
        page_heading = dataSync.get_page_heading_text()
        assert action.getTitle() == 'Data Sync Jobs | Cyware Orchestrate' and page_heading == 'Data Sync Jobs'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Click_Create_Data_Sync_btn(self):
        """
            Verify creation of new data sync job from Main Menu
            Validation -1. On the basis of Page title
        """
        log = self.getlogger()
        dataSync = DataSync(self.driver)
        action = Action(self.driver)
        log.info('Click on create data sync button')
        dataSync.click_create_data_sync()
        log.info('Store the page title in page_title variable for validation')
        page_title = action.getTitle()
        log.info('click on back button to cancel the data sync job creation')
        dataSync.click_back_button()
        log.info('click on close without saving button to cancel the data sync job creation')
        dataSync.click_confirm_close()
        log.info('validation based on the page title')
        assert page_title == 'Create Data Sync Policy | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Run_History(self):
        """
            Verify switch from Data Sync to Run History Logs
            Validation - 1. On the basis of Window's title
        """
        dataSync = DataSync(self.driver)
        action = Action(self.driver)
        log = self.getlogger()
        log.info("Click on the run history button")
        dataSync.click_run_history()
        assert action.getTitle() == 'Run History Logs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Verify_Switch_Data_Sync_Job_Details(self):
        """
            Verify switch from Run History Logs to Data Sync Job details
            Validation - 1. On the basis of Window's title
        """
        dataSync = DataSync(self.driver)
        action = Action(self.driver)
        dataSync.click_job_details()
        assert action.getTitle() == 'Data Sync Jobs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Click_on_Filter_btn(self):
        """
        Verify user is able to click on the filter button
        Validation: Based on the filter slider title
        """
        log = self.getlogger()
        action = Action(self.driver)
        dataSync = DataSync(self.driver)
        log.info("Click on the filter button")
        dataSync.click_on_filter_btn()
        log.info("Read slider title")
        slider_title = dataSync.get_filter_slider_title()
        assert slider_title == 'FILTERS'
