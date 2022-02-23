import pytest
from selenium.common.exceptions import NoSuchElementException

from pageObjects.AdminPage import Admin
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestAdminPanel(Base):

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_01_Dashboard_close_automatic_walkthrough(self):
        """
            Close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        action = Action(self.driver)
        admin = Admin(self.driver)
        try:
            log.info("click on the next button")
            tooltip_count = action.get_no_of_walkthrough_and_pagination_count(admin.get_tooltip_count())
            for i in range(0, tooltip_count):
                action.click(admin.click_on_next_btn())
        except NoSuchElementException:
            log.info("Automatic walkthrough was not initiated. Hence passing this testcase")
            pass

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Verify_Admin_Panel_redirection(self):
        """
            Verify redirection of the admin menu
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Admin_Menu())
        log.info("Click on Admin Menu")
        assert action.getTitle() in 'Admin Panel | Cyware Orchestrate'

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
        action.click(admin.click_Configuration())
        assert action.getTitle() in 'Configurations | Cyware Orchestrate'

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
        action.click(admin.click_Back_Button())
        log.info("Click on Authentication tab from Admin Page")
        action.click(admin.click_Authentication())
        assert action.getTitle() in 'Authentication | Cyware Orchestrate'

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
        action.click(admin.click_Back_Button())
        log.info("Click on License Management  tab from Admin Page")
        action.click(admin.click_License_Management())
        assert action.getTitle() in 'License Management | Cyware Orchestrate'

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
        action.click(admin.click_licence_update_button())
        log.info("Read licence field placeholder text")
        placeholder_text = action.getattribute(admin.field_licence_key(), 'placeholder')
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
        action.click(admin.click_Back_Button())
        log.info("Click on User Cyware Agent tab from Admin Page")
        action.click(admin.click_Cyware_Agent())
        assert action.getTitle() in 'Cyware Agent | Cyware Orchestrate'

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
        action.click(admin.click_Back_Button())
        log.info("Click on Console Status tab from Admin Page")
        action.click(admin.click_Console_Status())
        assert action.getTitle() in 'Console Status | Cyware Orchestrate'

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
        action.click(admin.click_Back_Button())
        log.info("Click on Playbook Tags tab from Admin Page")
        action.click(admin.click_Playbook_tags())
        assert action.getTitle() in 'Playbook Tags | Cyware Orchestrate'
