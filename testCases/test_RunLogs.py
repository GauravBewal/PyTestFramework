import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Runlogs import Runlogs
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestRunLogs(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.runlogs
    def test_01_Verify_Run_Logs_redirection(self):
        """
            Verify Run Logs redirection from Main Menu
            Validation-1: Based on the page title
        """
        nav = Navigation(self.driver)
        log = self.getlogger()
        action = Action(self.driver)
        log.info("Click on the main menu")
        nav.click_main_menu()
        log.info("Click on runlogs button")
        nav.navigate_run_logs()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() in 'Run Logs | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.runlogs
    def test_02_Click_on_Filters_btn(self):
        """
            Verify whether user is able click on filter
            Validation: Based on the filter title
        """
        log = self.getlogger()
        runlogs = Runlogs(self.driver)
        log.info("Click on the filter button")
        runlogs.click_on_filter_btn()
        log.info("Read the slider title")
        slider_title = runlogs.get_filter_slider_title()
        assert slider_title == 'FILTERS'
