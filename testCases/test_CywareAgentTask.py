import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestCywareAgentTask(Base):

    @pytest.mark.regression
    @pytest.mark.cywareagenttask
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
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        log.info("Read page heading")
        page_heading = nav.get_page_heading()
        assert action.get_title() == 'Cyware Agent Tasks | Cyware Orchestrate' \
               and 'Cyware Agent Tasks' in page_heading and error_msg_visibility is False
