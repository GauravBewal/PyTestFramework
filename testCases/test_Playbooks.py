import time
import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.Playbooks import Playbooks
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybook(Base):

    @pytest.mark.smoke
    def test_01_manage_playbook(self):
        """
            Verify Manage Playbook redirection from Main Menu
            Validation- 1. On the basis of window title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on Main Menu")
        action.click(nav.Click_Main_Menu())
        log.info("Click on Manage Playbook from Main Menu")
        action.click(nav.Navigate_Manage_Playbook())
        assert action.getTitle() in 'My Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_02_Cyware_Playbooks_switch_tab(self):
        """
            Verify user is able to switch from My Playbooks to Cyware Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on Cyware Playbooks for switch tab ")
        action.click(playbooks.cyware_app_tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'Cyware Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_03_My_Playbooks_switch_tab(self):
        """
            Verify user is able to switch from Cyware Playbooks to My Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on My Playbooks for switch tab")
        action.click(playbooks.custom_app_tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() in 'My Playbooks | Cyware Orchestrate'



