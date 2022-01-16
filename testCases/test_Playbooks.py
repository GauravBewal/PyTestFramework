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
    @pytest.mark.readOnly
    def test_01_manage_playbook(self):
        """
            Verify Manage Playbook redirection from Main Menu
            Validation- 1. On the basis of page heading
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        playbooks = Playbooks(self.driver)
        action = Action(self.driver)
        log.info("Click on Main Menu")
        action.click(nav.click_Main_Menu())
        log.info("Click on Manage Playbook from Main Menu")
        action.click(nav.Navigate_Manage_Playbook())
        read_page_heading = action.getText(playbooks.get_manage_playbook_heading())
        assert read_page_heading == 'Manage Playbooks'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Cyware_Playbooks_switch_tab(self):
        """
            Verify user is able to switch from My Playbooks to Cyware Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on Cyware Playbooks for switch tab ")
        action.click(playbooks.cyware_playbook_tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() == 'Cyware Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_view_playbook(self):
        """
        Verify view playbook from cyware play
        :return:
        """

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_My_Playbooks_switch_tab(self):
        """
            Verify user is able to switch from Cyware Playbooks to My Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on My Playbooks for switch tab")
        action.click(playbooks.my_playbook_tab())
        time.sleep(ReadConfig.sleepWait())
        assert action.getTitle() == 'My Playbooks | Cyware Orchestrate'

'''

    @pytest.mark.smoke
    def test_04_create_new_playbook(self):
        """
        Verify user is able to create a new playbook
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on create new playbook cta")
        action.click(playbooks.click_on_create_plybook_btn())
        log.info("clearing the default playbook name")
        action.clear_field(playbooks.enter_playbook_name())
        log.info("Enter playbook name")
        action.sendKeys(playbooks.enter_playbook_name(), "test")
        log.info("Enter playbook description")
        action.sendKeys(playbooks.enter_playbook_description(), "test")
        action.mouse_hover_on_element(playbooks.mouse_hover_on_save_btn())
        action.click(playbooks.save_and_exit_btn())
        time.sleep(10)
        
'''




