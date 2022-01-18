import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action


@pytest.mark.usefixtures("setup")
class TestRUnLogs:

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_run_logs(self):
        """
            Verify Run Logs redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Run_Logs())
        assert action.getTitle() in 'Run Logs | Cyware Orchestrate'
