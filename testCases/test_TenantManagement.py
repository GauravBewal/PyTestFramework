import time

import pytest

from pageObjects.Navigation import Navigation
from pageObjects.TenantManagement import TenantManagement
from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestTenantManagement(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Tenant_Management_redirection(self):
        """
        Verify redirection of Tenant Management from the admin page
        Validation 1: On the basis of window title
        """
        log = self.getlogger()
        action = Action(self.driver)
        nav = Navigation(self.driver)
        tenant = TenantManagement(self.driver)
        log.info("Click on admin menu")
        action.click(nav.click_Admin_Menu())
        log.info("Click on Tenant Management tab from Admin Page")
        action.click(tenant.click_Tenant_Management())
        assert action.getTitle() == 'Tenant Management | Cyware Orchestrate'
        time.sleep(ReadConfig.Wait_10_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_click_new_tenant(self):
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on add tenant button")
        action.javascript_click_element(tenant.click_new_tenant())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the tenant form slider title")
        slider_text = action.getText(tenant.get_slider_title())
        log.info("Click on slider close button")
        action.click(tenant.click_slider_close())
        assert slider_text == 'Add Tenant'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on inactive tab")
        action.click(tenant.click_inactive_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(tenant.click_inactive_tab())
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on inactive tab")
        action.click(tenant.click_inactive_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(tenant.click_inactive_tab())
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_switch_All_tab(self):
        """
            Verify switch to All tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        tenant = TenantManagement(self.driver)
        action = Action(self.driver)
        log.info("Click on All tab")
        action.click(tenant.click_All_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(tenant.click_All_tab())
        assert tab_color == '#1a3ee8'
