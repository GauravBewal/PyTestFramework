import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestDashBoard(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_dashboard_redirection(self):
        """
            Verify Dashboard redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Dashboard())
        assert action.getTitle() in 'Dashboard | Cyware Orchestrate'


