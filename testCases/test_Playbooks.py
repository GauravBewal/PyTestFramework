import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybook(Base):

    @pytest.mark.smoke
    def test_01_manage_playbook(self):
        """
            Verify Manage Playbook redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Main_Menu())
        action.click(nav.Navigate_Manage_Playbook())
        assert action.getTitle() in 'Custom Playbooks | Cyware Orchestrate'
