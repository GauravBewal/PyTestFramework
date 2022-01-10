import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestConfigureTriggers(Base):

    @pytest.mark.smoke
    def test_01_configure_triggers_redirection(self):
        """
            Verify Configure Triggers redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Main_Menu())
        action.click(nav.Navigate_Configure_Event())
        assert action.getTitle() in 'Configure Triggers | Cyware Orchestrate'
