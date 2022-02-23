import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestCywareAgentTask(Base):

    @pytest.mark.smoke
    def test_01_Verify_Cyware_Agent_Task_redirection(self):
        """
            Verify Cyware Agent Task redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Agent_task())
        assert action.getTitle() in 'Cyware Agent Tasks | Cyware Orchestrate'
