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
        assert action.getTitle() in 'Data Sync Jobs | Cyware Orchestrate'

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
        assert action.getTitle() in 'Run History Logs | Cyware Orchestrate'

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
        assert action.getTitle() in 'Data Sync Jobs | Cyware Orchestrate'
