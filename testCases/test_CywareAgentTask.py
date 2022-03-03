import logging

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
        log = self.getlogger()
        log.info("click on the main menu")
        nav.click_main_menu()
        log.info("click on the cyware agent tasks button")
        nav.navigate_agent_task()
        assert action.get_title() == 'Cyware Agent Tasks | Cyware Orchestrate'
