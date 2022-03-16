import pytest

from pageObjects.AdminPage import Admin
from pageObjects.LicenseManagement import LicenseManagement
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestLicenseManagement(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Admin_License_Management_redirection(self):
        """
            Verify redirection of License Management from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        nav.click_admin_menu()
        log.info("Click on Admin Menu")
        admin.click_license_management()
        log.info("Click on License Management tab from Admin Page")
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'License Management | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Click_Update_Licence_Key_btn(self):
        """
            Verify updation of licence key
            Validation - 1 : Based on the placeholder text of licence field
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Click on update button")
        license.click_licence_update_button()
        log.info("Read licence field placeholder text")
        placeholder_text = license.licence_key_field("placeholder")
        cross_and_tick_button_visible = license.check_cross_and_tick_btn()
        assert placeholder_text == 'Enter License Key *' and cross_and_tick_button_visible

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Visiblity_of_User_Accounts_Card(self):
        """
            Verify visiblity of User Account card
            Validation - 1. On the basis of Card's title
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read User Accounts card title")
        title = license.get_text_from_user_accounts_card()
        assert title == 'User Accounts'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Visiblity_of_Open_APIs_Card(self):
        """
            Verify visiblity of Open APIs card
            Validation - 1. On the basis of Card's title
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read Open API card title")
        title = license.get_text_from_Open_APIs_card()
        assert title == 'Open APIs'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_05_Visiblity_of_Webhooks_Card(self):
        """
            Verify visiblity of Webhooks card
            Validation - 1. On the basis of Card's title
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read Webhooks card title")
        title = license.get_text_from_Webhooks_card()
        assert title == 'Webhooks'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_06_Days_left_for_expiration(self):
        """
            Verify number of days left for expiration is more than 10 days
            Validation - 1. On the basis of number of days left
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read Number of days left for expiration")
        number_of_days_left = license.get_number_of_days_left()
        assert int(number_of_days_left) > 10

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_07_Tenant_Name_visiblity(self):
        """
            Verify if the name of the tenant is visible
            Validation - 1. On the basis of visiblity of name
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read Name of the tenant Name")
        tenant_name = license.get_name_of_Tenant()
        assert len(tenant_name) > 0

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_08_Tenant_code_visiblity(self):
        """
            Verify if the name of the tenant code is visible
            Validation - 1. On the basis of visiblity of code name
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read Name of the tenant code")
        tenant_code = license.get_name_of_Tenant_code()
        assert len(tenant_code) > 0

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_09_Tenant_version_visiblity(self):
        """
            Verify if the name of the tenant version is visible
            Validation - 1. On the basis of visiblity of version name
        """
        log = self.getlogger()
        license = LicenseManagement(self.driver)
        log.info("Read Name of the tenant version")
        tenant_version = license.get_name_of_Tenant_version()
        assert len(tenant_version) > 0
