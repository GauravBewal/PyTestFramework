import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from pageObjects.AdminPage import Admin
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestAdminPanel(Base):


    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_Admin_Panel_redirection(self):
        """
            Verify redirection of the admin menu
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        admin = Admin(self.driver)
        log.info("Check if walk through is initiated")
        admin.click_on_close_walkthrough()
        log.info("Click on Admin Menu")
        nav.click_Admin_Menu()
        assert action.getTitle() == 'Admin Panel | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_Admin_Configurations_redirection(self):
        """
            Verify redirection of Configurations from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on Configurations tab from Admin Page")
        admin.click_Configuration()
        assert action.getTitle() == 'Configurations | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Verify_Admin_Authentication_redirection(self):
        """
            Verify redirection of Authentication from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Configurations")
        admin.click_Back_Button()
        log.info("Click on Authentication tab from Admin Page")
        admin.click_Authentication()
        assert action.getTitle() == 'Authentication | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Verify_Admin_License_Management_redirection(self):
        """
            Verify redirection of License Management from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Authentication")
        admin.click_Back_Button()
        log.info("Click on License Management  tab from Admin Page")
        admin.click_License_Management()
        assert action.getTitle() == 'License Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_06_Click_Update_Licence_Key_btn(self):
        """
            Verify updation of licence key
            Validation - 1 : Based on the placeholder text of licence field
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on update button")
        admin.click_licence_update_button()
        log.info("Read licence field placeholder text")
        placeholder_text = admin.field_licence_key("placeholder")
        assert placeholder_text == 'Enter License Key *'

    @pytest.mark.smoke
    def test_07_Verify_Admin_Cyware_Agent_redirection(self):
        """
            Verify redirection of Cyware Agent from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from User Groups Management")
        admin.click_Back_Button()
        log.info("Click on User Cyware Agent tab from Admin Page")
        admin.click_Cyware_Agent()
        assert action.getTitle() == 'Cyware Agent | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_08_Verify_Admin_Console_Status_redirection(self):
        """
            Verify redirection of Console Status from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from SysLogs")
        admin.click_Back_Button()
        log.info("Click on Console Status tab from Admin Page")
        admin.click_Console_Status()
        assert action.getTitle() == 'Console Status | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_09_Verify_Admin_Playbook_Tags_redirection(self):
        """
            Verify redirection of Playbook Tags from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Console Status")
        admin.click_Back_Button()
        log.info("Click on Playbook Tags tab from Admin Page")
        admin.click_Playbook_tags()
        assert action.getTitle() == 'Playbook Tags | Cyware Orchestrate'
