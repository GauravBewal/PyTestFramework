import pytest

from pageObjects.CommonElements import Tooltip
from pageObjects.Navigation import Navigation
from pageObjects.TenantManagement import TenantManagement
from utilities.Actions import Action
from utilities.Base import Base

@pytest.mark.usefixtures("setup")
class TestTenantManagement(Base):

    @pytest.mark.regression
    @pytest.mark.tenantmanagement
    def test_01_Verify_Tenant_Management_redirection(self):
        """
        Verify redirection of Tenant Management from the admin page
        Validation 1: On the basis of window title
        """
        log = self.getlogger()
        action = Action(self.driver)
        nav = Navigation(self.driver)
        tenant = TenantManagement(self.driver)
        log.info("Click on admin menu")
        nav.click_admin_menu()
        log.info("Click on Tenant Management tab from Admin Page")
        tenant.click_tenant_management()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        global active_count
        active_count = tenant.get_tenant_count()
        assert action.get_title() == 'Tenant Management | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.tenantmanagement
    def test_02_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        log.info("Click on inactive tab")
        tenant.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = tenant.get_inactive_tab_color()
        log.info("Check for visbility of first inactive tab")
        tenant.Pass_even_first_inactive_Tenant_is_not_visible()
        global inactive_count
        inactive_count = tenant.get_tenant_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.tenantmanagement
    def test_03_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        log.info("Click on All tab")
        tenant.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = tenant.get_all_tab_color()
        tenant.Pass_even_first_active_Tenant_is_not_visible()
        global all_tab_count
        all_tab_count = tenant.get_tenant_count()
        assert tab_color == '#1a3ee8' and all_tab_count == active_count + inactive_count

    @pytest.mark.regression
    @pytest.mark.tenantmanagement
    def test_04_Click_New_Tenant_btn(self):
        """
            Verify whether user is able to click on new tenant button
            Validation: Based on the slider title
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        log.info("Switch to active tab")
        tenant.click_active_tab()
        tenant.Pass_even_first_active_Tenant_is_not_visible()
        log.info("Click on add tenant button")
        tenant.click_new_tenant()
        log.info("Read the tenant form slider title")
        slider_text = tenant.get_slider_title()
        log.info("Click on slider close button")
        tenant.click_slider_close()
        assert slider_text == 'Add Tenant'


    # @pytest.mark.regression
    # @pytest.mark.tenantmanagement
    # def test_05_Create_New_Tenant(self):
    #     """
    #         Verify whether user is able to create new tenant button
    #         Validation: Based on the Number of active tenants
    #     """
    #     log = self.getlogger()
    #     tenant = TenantManagement(self.driver)
    #     action = Action(self.driver)
    #     tooltip = Tooltip(self.driver)
    #     log.info("Switch to active tab")
    #     tenant.click_active_tab()
    #     tenant.Pass_even_first_active_Tenant_is_not_visible()
    #     active_count = tenant.get_count_of_tenants()
    #     log.info("Click on add tenant button")
    #     tenant.click_new_tenant()
    #     global tenant_name
    #     global domain_name
    #     tenant_name = "ui-automation" + action.get_random_digit()
    #     domain_name = tenant_name + ".cywareqa.com"
    #     log.info("Adding tenant name")
    #     tenant.put_tenant_name(tenant_name)
    #     log.info("Adding tenant domain")
    #     tenant.put_domain_name(domain_name)
    #     log.info("Click on save button")
    #     tenant.click_save_btn()
    #     log.info("Click on the close tool tip")
    #     toast_msg = tooltip.get_tooltip_msg()
    #     assert "Success" in toast_msg
    #     log.info("Click on close tooltip")
    #     tooltip.click_close_tooltip()
    #     log.info("Click on Continue using Cyware Orchestrate button")
    #     tenant.click_continue_using_co_btn()
    #     log.info("Wait until created tenant is visible")
    #     tenant.visibility_of_created_Tenant()
    #     assert tenant.get_count_of_tenants() == active_count + 1
    #
    # @pytest.mark.regression
    # @pytest.mark.tenantmanagement
    # def test_06_Search_Tenant(self):
    #     """
    #         Verify the Searchbar Functionality is working.
    #         Validation-1: On basis of the Name Comparison.
    #
    #     """
    #     tenant = TenantManagement(self.driver)
    #     log = self.getlogger()
    #     log.info("Search Functionality of Tenant")
    #     tenant.search_input_string(tenant_name)
    #     tenant.click_enter_for_search()
    #     log.info("Wait until create tenant is visible")
    #     tenant.visibility_of_created_Tenant()
    #     log.info("Get the tenant name")
    #     search_result = tenant.get_name_first_tenant()
    #     assert tenant_name == search_result
