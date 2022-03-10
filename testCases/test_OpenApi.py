import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.OpenApi import OpenApi
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestOpenApi(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_1_Verify_Admin_Open_API_Redirection(self):
        """
            Verify redirection of Open APIs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Cyware Agent")
        nav.click_admin_menu()
        log.info("Click on Open APIs tab from Admin Page")
        openapi.click_open_api_tab()
        assert action.get_title() == 'Open APIs | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Click_New_Open_Api_btn(self):
        """
        Verify whether user is able on click on new openapi button
        Validation: Based on the create slider title
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on add openapi button")
        openapi.click_new_open_api()
        log.info("Read the slider title")
        slider_title = openapi.get_slider_title()
        log.info("Click on close slider button")
        openapi.click_slider_close()
        assert slider_title == 'New Open API'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on inactive tab")
        openapi.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = openapi.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on All tab")
        openapi.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = openapi.get_all_tab_color()
        assert tab_color == '#1a3ee8'
