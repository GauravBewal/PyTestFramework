import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestAdminPanel(Base):

    @pytest.mark.admin
    def test_01_admin_panel_redirection(self):
        """
            Verify redirection of the admin menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Admin_Menu())
        assert action.getTitle() in 'Admin Panel | Cyware Orchestrate'
