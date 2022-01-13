import pytest

from pageObjects.AdminPage import Admin
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestAdminPanel(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_admin_panel_redirection(self):
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
    def test_02_admin_Configurations(self):
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
    def test_03_admin_Authentication(self):
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
    def test_04_admin_License_Management(self):
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
    def test_05_admin_Tenant_Management(self):
        """
            Verify redirection of Tenant Management from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from License Management")
        action.click(admin.click_Back_Button())
        log.info("Click on Tenant Management tab from Admin Page")
        action.click(admin.click_Tenant_Management())
        assert action.getTitle() in 'Tenant Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_06_admin_User_Management(self):
        """
            Verify redirection of User Management from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Tenant Management")
        action.click(admin.click_Back_Button())
        log.info("Click on User Management tab from Admin Page")
        action.click(admin.click_User_Management())
        assert action.getTitle() in 'User Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_07_admin_User_Groups_Management(self):
        """
            Verify redirection of User Groups Management from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from User Management")
        action.click(admin.click_Back_Button())
        log.info("Click on User Groups Management tab from Admin Page")
        action.click(admin.click_User_Group_Management())
        assert action.getTitle() in 'User Groups Management | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_08_admin_Cyware_Agent(self):
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
    def test_09_admin_Open_APIs(self):
        """
            Verify redirection of Open APIs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Cyware Agent")
        action.click(admin.click_Back_Button())
        log.info("Click on Open APIs tab from Admin Page")
        action.click(admin.click_Open_API())
        assert action.getTitle() in 'Open APIs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_10_admin_Webhooks(self):
        """
            Verify redirection of Webhooks from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Open APIs")
        action.click(admin.click_Back_Button())
        log.info("Click on Webhooks tab from Admin Page")
        action.click(admin.click_Webhooks())
        assert action.getTitle() in 'Webhooks | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_11_admin_SysLogs(self):
        """
            Verify redirection of SysLogs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Webhooks")
        action.click(admin.click_Back_Button())
        log.info("Click on SysLogs tab from Admin Page")
        action.click(admin.click_SysLogs())
        assert action.getTitle() in 'Syslogs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_12_Console_Status(self):
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
    def test_13_Playbook_tags(self):
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
