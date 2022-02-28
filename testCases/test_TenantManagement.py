import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.TenantManagement import TenantManagement
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestTenantManagement(Base):

    @pytest.mark.smoke
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
        nav.click_Admin_Menu()
        log.info("Click on Tenant Management tab from Admin Page")
        tenant.click_Tenant_Management()
        assert action.getTitle() == 'Tenant Management | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_02_Click_New_Tenant_btn(self):
        """
        Verify whether user is able to click on new tenant button
        Validation: Based on the slider title
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        log.info("Click on add tenant button")
        tenant.click_new_tenant()
        log.info("Read the tenant form slider title")
        slider_text = tenant.get_slider_title()
        log.info("Click on slider close button")
        tenant.click_slider_close()
        assert slider_text == 'Add Tenant'


    @pytest.mark.smoke
    def test_03_Verify_Switch_Inactive_tab(self):
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
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        log.info("Click on All tab")
        tenant.click_All_tab()
        log.info("Read the tab color after switching")
        tab_color = tenant.get_all_tab_color()
        assert tab_color == '#1a3ee8'
