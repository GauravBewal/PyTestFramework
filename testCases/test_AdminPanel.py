import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestAdminPanel(Base):

    @pytest.mark.smoke
    def test_01_admin_panel_redirection(self):
        """
            Verify redirection of the admin menu
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Admin_Menu())
        log.info("Click on Admin Menu")
        assert action.getTitle() in 'Admin Panel | Cyware Orchestrate'
