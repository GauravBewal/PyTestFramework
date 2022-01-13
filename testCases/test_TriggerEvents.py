import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestTriggerEvents(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_trigger_events_redirection(self):
        """
            Verify Trigger Events redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Trigger_Event())
        assert action.getTitle() in 'Trigger Events | Cyware Orchestrate'
