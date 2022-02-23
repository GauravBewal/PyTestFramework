import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.Runlogs import Runlogs
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestRUnLogs(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_Run_Logs_redirection(self):
        """
            Verify Run Logs redirection from Main Menu
        """
        nav = Navigation(self.driver)
        log = self.getlogger()
        action = Action(self.driver)
        log.info("Click on the main menu")
        action.click(nav.click_Main_Menu())
        log.info("Click on runlogs button")
        action.click(nav.Navigate_Run_Logs())
        assert action.getTitle() in 'Run Logs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Click_on_Filters_btn(self):
        """
            Verify whether user is able click on filter
            Validation: Based on the filter title
        """
        log = self.getlogger()
        action = Action(self.driver)
        runlogs = Runlogs(self.driver)
        log.info("Click on the filter button")
        action.click(runlogs.click_on_filter_btn())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the slider title")
        slider_title = action.getText(runlogs.get_filter_slider_title())
        assert slider_title == 'FILTERS'
