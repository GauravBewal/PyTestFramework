import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestApps(Base):

    @pytest.mark.smoke
    def test_01_apps_redirection(self):
        """
            Verify Apps redirection from Main Menu
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Main_Menu())
        log.info("Click on Apps from Menu")
        action.click(nav.Navigate_Apps())
        assert action.getTitle() in 'App(s) | Cyware Orchestrate'
