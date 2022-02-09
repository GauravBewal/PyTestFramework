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
        time.sleep(ReadConfig.Wait_20_Sec())
        log.info("Click on Cyware Playbooks for switch tab ")
        action.click(playbooks.cyware_playbook_tab())
        time.sleep(ReadConfig.Wait_10_Sec())
        assert action.getTitle() == 'Cyware Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_view_playbook(self):
        """
        Verify opening playbook in view mode from cyware playbook
        Validation : Based on the window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on the first playbook")
        action.click(playbooks.click_first_playbook())
        time.sleep(ReadConfig.Wait_20_Sec())
        log.info("Switch to new tab")
        parent_window = action.switch_new_window(1)
        log.info("Read the window title")
        page_title = action.getTitle()
        log.info("Switch back to parent window and close child window")
        action.switch_back_parent_window(parent_window)
        assert page_title == 'View Playbook | Cyware Orchestrate'


    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_My_Playbooks_switch_tab(self):
        """
            Verify user is able to switch from Cyware Playbooks to My Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on My Playbooks for switch tab")
        action.click(playbooks.my_playbook_tab())
        time.sleep(ReadConfig.Wait_10_Sec())
        assert action.getTitle() == 'My Playbooks | Cyware Orchestrate'



    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_create_new_playbook(self):
        """
        Verify user is able to create a new playbook
        Validation : Based on the window title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on create new playbook cta")
        action.click(playbooks.click_on_create_playbook_btn())
        log.info("Read the page title")
        page_title = action.getTitle()
        log.info("click on the back button")
        action.click(playbooks.click_on_back_button())
        log.info("Click exit without save button")
        action.click(playbooks.click_exit_without_save())
        assert page_title == 'Add Playbook | Cyware Orchestrate'

    #@pytest.mark.readOnly
    @pytest.mark.smoke
    def test_06_click_add_node(self):
        """
          Verify click on add node button
          Validation : Based on the add node slider title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on add node button")
        action.click(playbooks.click_add_node())
        log.info("Read the add node slider title")
        slider_text = action.getText(playbooks.get_add_node_slider_text())
        assert slider_text == ''





