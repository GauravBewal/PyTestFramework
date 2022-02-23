import time

import pytest
from selenium.common.exceptions import NoSuchElementException

from configuration.readConfiguration import ReadConfig
from pageObjects.Dashboard import Dashboard
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestDashBoard(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_dashboard_redirection(self):
        """
            Verify Dashboard redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Dashboard())
        assert action.getTitle() in 'Dashboard | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Switch_dark_mode(self):
        """
        Verify whether user is able to switch to dark mode
        Validation-1: Based on the icon visibility and element color visibility
        """
        log = self.getlogger()
        action = Action(self.driver)
        dashboard = Dashboard(self.driver)
        log.info("Checking whether dark mode is enabled. If enabled disable it and run the test cases")
        try:
            action.click(dashboard.click_dark_mode_btn())
        except NoSuchElementException:
            action.click(dashboard.click_light_mode_btn())
            time.sleep(ReadConfig.Wait_3_Sec())
            action.click(dashboard.click_dark_mode_btn())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the header color")
        element_color = action.getElementColor(dashboard.read_header_color())
        log.info("Check visibility of light mode")
        visibility = action.check_visibility_of_element(dashboard.click_light_mode_btn())
        log.info("switch to light mode")
        action.click(dashboard.click_light_mode_btn())
        time.sleep(ReadConfig.Wait_3_Sec())
        assert visibility is True and element_color == '#2c3e50'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Check_all_widgets_visibility(self):
        """
        Check whether user is able to see all the widgets
        Validation: Based on the widget title's
        """
        log = self.getlogger()
        action = Action(self.driver)
        dashboard = Dashboard(self.driver)
        action.check_visibility_of_element(dashboard.click_dark_mode_btn())
        log.info("Read all the widget titles")
        widget_titles = ['PLAYBOOK EXECUTION TIMELINE', 'FREQUENTLY USED PLAYBOOKS',
                         'PLAYBOOK EXECUTION TIME (ON AVERAGE)'
            , 'FREQUENTLY USED INSTANCES', 'FREQUENTLY USED APPS', 'FREQUENTLY USED ACTIONS',
                         'FREQUENTLY EXECUTED ACTIONS'
            , 'FREQUENTLY UTILIZED APPS', 'FREQUENTLY UTILIZED INSTANCES', 'TOTAL EVENT COUNT'
            , 'INCOMING SOURCE EVENTS', 'PERCENTAGE OF UNUTILIZED EVENTS',
                         'PERCENTAGE OF EVENTS THAT CAUSE PLAYBOOK EXECUTION ERROR']
        all_widget_elements = dashboard.get_all_widget_elements()
        for ele in range(1, len(all_widget_elements) + 1):
            path = "(//div[contains(@class,'widget-label')]/div)[" + str(ele) + "]"
            title = action.getText(dashboard.find_element_path(path))
            assert widget_titles[ele - 1] == title
        time.sleep(ReadConfig.Wait_3_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Click_on_ViewAll_btn(self):
        """
            Verify that View All button is working as expected or not
            Validation - 1. On the basis of Legends button visibility
        """
        dashboard = Dashboard(self.driver)
        action = Action(self.driver)
        action.check_visibility_of_element(dashboard.click_dark_mode_btn())
        elements_list = dashboard.get_all_viewall_elements()
        for element in range(1, len(elements_list) + 1):
            path = "(//div[@class='cy-dahsboard-layout__widget']//div[contains(text(),'View all')])[" + str(
                element) + "]"
            action.click(dashboard.find_element_path(path))
            time.sleep(ReadConfig.Wait_6_Sec())
            t = action.check_visibility_of_element(dashboard.visibility_of_legends_btn())
            action.click(dashboard.click_on_back_btn())
            time.sleep(ReadConfig.Wait_3_Sec())
            assert t is True

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Click_maximize_btn(self):
        """
        Check whether user is able to click on the maximize button
        Validation: Based on the minimize button visibility after clicking on maximize button
        """
        log = self.getlogger()
        action = Action(self.driver)
        dashboard = Dashboard(self.driver)
        log.info("Click on the maximize button")
        action.click(dashboard.click_maximize_btn())
        log.info("Check whether minimize button is visible or not")
        visibility = action.check_visibility_of_element(dashboard.click_minimize_btn())
        log.info("Click on minimize button")
        action.click(dashboard.click_minimize_btn())
        assert visibility is True

    @pytest.mark.smoke
    def test_06_Apply_one_week_in_calendar(self):
        """
        Verify whether user is able to enter the date as per his wish
        Validation: Based on the date visibility after entering
        """
        log = self.getlogger()
        action = Action(self.driver)
        dashboard = Dashboard(self.driver)
        log.info("Click on the start date button")
        action.click(dashboard.click_start_date_btn())
        log.info("Select start date from calendar")
        action.javascript_click_element(dashboard.select_calendar_start_date())
        log.info("select end date from calendar")
        action.click(dashboard.select_calendar_end_date())
        log.info("Click on the start date button to check whether date is selected or not")
        action.click(dashboard.click_start_date_btn())
        start_date_color = action.getElementColor(dashboard.select_calendar_start_date())
        end_date_color = action.getElementColor(dashboard.select_calendar_end_date())
        assert start_date_color == '#606266' and end_date_color == '#606266'
