import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from configuration.readConfiguration import ReadConfig
from pageObjects.Dashboard import Dashboard
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base



@pytest.mark.usefixtures("setup")
class TestDashBoard(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.dashboard
    def test_01_Verify_Dashboard_redirection(self):
        """
            Verify Dashboard redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log = self.getlogger()
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Click on dashboard button")
        nav.navigate_dashboard()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'Dashboard | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.dashboard
    def test_02_Switch_Dark_Mode(self):
        """
        Verify whether user is able to switch to dark mode
        Validation-1: Based on the icon visibility and element color visibility
        """
        log = self.getlogger()
        dashboard = Dashboard(self.driver)
        log.info("Checking whether dark mode is enabled. If enabled disable it and run the test cases")
        try:
            dashboard.check_visibility_of_dark_mode_btn()
            dashboard.click_dark_mode_btn()
        except (NoSuchElementException, TimeoutException):
            dashboard.click_light_mode_btn()
            dashboard.click_dark_mode_btn()
        log.info("Read the header color")
        element_color = dashboard.read_header_color()
        log.info("Check visibility of light mode")
        visibility = dashboard.check_visibility_of_light_btn()
        log.info("switch to light mode")
        dashboard.click_light_mode_btn()
        log.info("Refresh the page")
        dashboard.click_sync_btn()
        assert visibility is True and element_color == '#2c3e50'

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.dashboard
    def test_03_Check_All_Widgets_Visibility(self):
        """
        Check whether user is able to see all the widgets
        Validation: Based on the widget title's
        """
        log = self.getlogger()
        dashboard = Dashboard(self.driver)
        log.info("Read all the widget titles")
        elements_list = dashboard.get_list_of_elements(dashboard.get_all_widget_elements(), dashboard.widget_elements)
        if len(elements_list) > 0:
            for element in range(0, len(elements_list)):
                title = dashboard.find_element_path_and_get_text(elements_list[element])
                assert dashboard.widget_titles[element] == title
        else:
            return False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.dashboard
    def test_04_Click_on_View_All_btn(self):
        """
            Verify that View All button is working as expected or not
            Validation - 1. On the basis of Legends button visibility
        """
        dashboard = Dashboard(self.driver)
        elements_list = dashboard.get_list_of_elements(dashboard.get_all_view_all_elements(), dashboard.btn_view_all)
        if len(elements_list) > 0:
            for element in range(0, len(elements_list)):
                dashboard.click_on_view_all_btn(elements_list[element])
                visibility = dashboard.visibility_of_legends_btn()
                dashboard.click_on_back_btn()
                assert visibility is True
        else:
            assert False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.dashboard
    def test_05_Click_Maximize_btn(self):
        """
        Check whether user is able to click on the maximize button
        Validation: Based on the minimize button visibility after clicking on maximize button
        """
        log = self.getlogger()
        dashboard = Dashboard(self.driver)
        log.info("Click on the maximize button")
        dashboard.click_maximize_btn()
        log.info("Check whether minimize button is visible or not")
        visibility = dashboard.check_visibility_of_minimize_btn()
        log.info("Click on minimize button")
        dashboard.click_minimize_btn()
        assert visibility is True

    @pytest.mark.regression
    @pytest.mark.dashboard
    def test_06_Apply_current_date_filter_using_calendar(self):
        """
        Verify whether user is able to enter the date as per his wish
        Validation: Based on the date visibility after entering
        """
        log = self.getlogger()
        dashboard = Dashboard(self.driver)
        log.info("Click on the start date button")
        dashboard.click_start_date_btn()
        log.info("Select start date from calendar")
        dashboard.select_calendar_start_date()
        log.info("select end date from calendar")
        dashboard.select_calendar_start_date()
        log.info("Click on the start date button to check whether date is selected or not")
        dashboard.click_start_date_btn()
        start_date_color = dashboard.get_calendar_start_date_color()
        assert start_date_color == '#1a3ee8'
