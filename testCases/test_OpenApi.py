import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.OpenApi import OpenApi
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestOpenApi(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_1_admin_Open_APIs(self):
        """
            Verify redirection of Open APIs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Cyware Agent")
        action.click(nav.click_Admin_Menu())
        log.info("Click on Open APIs tab from Admin Page")
        action.click(openapi.click_Open_API_tab())
        assert action.getTitle() == 'Open APIs | Cyware Orchestrate'
        time.sleep(ReadConfig.Wait_10_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_click_new_openapi(self):
        log = self.getlogger()
        action = Action(self.driver)
        openapi = OpenApi(self.driver)
        log.info("Click on add openapi button")
        action.click(openapi.click_new_open_api())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the slider title")
        slider_title = action.getText(openapi.get_slider_title())
        log.info("Click on close slider button")
        action.click(openapi.click_slider_close())
        assert slider_title == 'New Open API'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        action = Action(self.driver)
        log.info("Click on inactive tab")
        action.click(openapi.click_inactive_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(openapi.click_inactive_tab())
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_switch_All_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        action = Action(self.driver)
        log.info("Click on All tab")
        action.click(openapi.click_All_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(openapi.click_All_tab())
        assert tab_color == '#1a3ee8'
