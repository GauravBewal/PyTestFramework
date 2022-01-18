import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestHomePage(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_main_menu_redirection(self):
        """
            Verify Main Menu is clickable
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        assert action.getTitle() in 'Dashboard | Cyware Orchestrate'
