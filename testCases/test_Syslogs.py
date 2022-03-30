import time

import pytest

from pageObjects.CommonElements import Tooltip
from pageObjects.ConfigureTrigger import ConfigureTrigger
from pageObjects.Navigation import Navigation
from pageObjects.Syslogs import Syslogs
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestSyslogs(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Admin_SysLogs_redirection(self):
        """
            Verify redirection of SysLogs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on Main menu")
        nav.click_admin_menu()
        log.info("Click on SysLogs tab from Admin Page")
        syslog.click_syslogs()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        global active_count
        active_count = syslog.get_syslog_count()
        assert action.get_title() in 'Syslogs | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        log.info("Click on inactive tab")
        syslog.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = syslog.get_inactive_tab_color()
        log.info("Check for first inactive syslog")
        syslog.visibility_of_first_inactive_syslog()
        global inactive_count
        inactive_count = syslog.get_syslog_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        log.info("Click on all tab")
        syslog.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = syslog.get_all_tab_color()
        log.info("Check for active syslog visibility")
        syslog.visibility_of_first_active_syslog()
        global all_tab_count
        all_tab_count = syslog.get_syslog_count()
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count + active_count

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Click_New_Syslogs_btn(self):
        """
            Verify create button functionality of new syslogs
            Validation - 2. On the basis of slider title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        syslog.click_active_tab()
        log.info("Check for active syslog visibility")
        syslog.visibility_of_first_active_syslog()
        log.info("Click on add syslog button")
        syslog.click_new_syslog()
        log.info("Read the slider title")
        slider_title = syslog.get_slider_title()
        log.info("Click on close slider button")
        syslog.click_slider_close()
        assert slider_title == 'Configure Syslog'

    @pytest.mark.regression
    def test_05_Create_Syslog(self):
        """
            verify the create syslog
            Validation . On basis of increase in number of syslogs
            TC_ID : 005
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        tooltip = Tooltip(self.driver)
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on to main menu")
        nav.click_main_menu()
        log.info("Click on configure event")
        nav.navigate_configure_event()
        config_trigger.visibility_of_first_active_configure_trigger()
        config_trigger.click_inactive_tab()
        config_trigger.visibility_of_first_inactive_configure_trigger()
        config_trigger_name = config_trigger.get_first_configure_trigger()
        config_trigger.click_first_configure_trigger()
        config_trigger.click_active_configure_trigger_btn()
        config_trigger.click_on_update()
        log.info("Read the success message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        tooltip.click_close_tooltip()
        log.info("Click on Main menu")
        nav.click_admin_menu()
        log.info("Click on SysLogs tab from Admin Page")
        syslog.click_syslogs()
        log.info("Click on all tab")
        syslog.click_active_tab()
        syslog.visibility_of_first_active_syslog()
        global syslog_title
        syslog_title = "test_syslog_" + action.get_current_time()
        log.info("Click on the create new button")
        syslog.click_new_syslog()
        log.info("Add the Syslog title in the specified input field")
        syslog.put_syslog_title(syslog_title)
        port_number = syslog.generate_port_number()
        log.info("Add the Port Number in the specified input field")
        syslog.put_port_number(port_number)
        syslog.click_on_list_Source_Events_App()
        syslog.put_source_event_app(config_trigger_name)
        log.info("Select the Source Event App for the Syslog")
        syslog.select_first_source_event_app_and_type()
        log.info("Select the Source Event Type for the Syslog")
        syslog.click_on_list_Source_Events_Type()
        syslog.select_first_source_event_app_and_type()
        syslog.click_save_btn()
        log.info("Read the tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' in toast_msg
        log.info("click on close toop tip")
        tooltip.click_close_tooltip()
        syslog.visibility_of_first_active_syslog()
        assert active_count + 1 == syslog.get_syslog_count()

    @pytest.mark.regression
    def test_06_Search_Syslog(self):
        """
            Verify the Searchbar Functionality is working.
            Validation-1: On basis of the Name Comparison.

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Search Functionality of Syslogs")
        syslog.search_input_string(syslog_title)
        syslog.click_enter_for_search()
        search_result = syslog.get_name_first_syslog()
        assert syslog_title == search_result

    @pytest.mark.regression
    def test_07_Update_Syslog(self):
        """
        Verify user is able to edit the syslog
        Validation-1: Based on the successful message
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on the first syslog")
        syslog.click_first_syslog()
        global updated_syslog_name
        updated_syslog_name = "ui_automtion" + action.get_current_time()
        log.info("Clear the previous title")
        syslog.clear_syslog_title()
        log.info("Enter updated syslog name")
        syslog.put_syslog_title(updated_syslog_name)
        log.info("Click on save button")
        syslog.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.get_tooltip_msg()
        log.info("Close tool tip")
        tooltip.click_close_tooltip()
        assert 'Success' in toast_msg
        log.info("Clear search")
        syslog.clear_search()

    @pytest.mark.regression
    def test_08_Check_the_Dropdown_Edit_Visibility(self):
        """
            Verify the dropdown button Visibility.
            Validation -1 : Check The Edit Slider Title
        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Enter the syslog name to search")
        syslog.search_input_string(updated_syslog_name)
        log.info("Press Enter to search")
        syslog.click_enter_for_search()
        log.info("Check for the visibility of first active syslog")
        syslog.visibility_of_first_active_syslog()
        log.info("Mouse over the dropdown")
        syslog.check_drop_down()
        log.info("Click on Edit button in Drop down")
        syslog.click_edit_button()
        log.info("Get the Slider Name")
        slider_title = syslog.get_slider_title()
        log.info("Close the Slider")
        syslog.click_slider_close()
        assert slider_title == "Edit Syslog"

    @pytest.mark.regression
    def test_09_Deactivate_Syslog(self):
        """
            Verify the deactivating syslog functionality
            Validation 1: Based on the Status of the syslog
        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Mouse hover the dropdown")
        syslog.check_drop_down()
        log.info("Click on deactive button")
        syslog.click_deactivate_button()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.get_tooltip_msg()
        assert 'Success' in tooltip_msg
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        log.info("Clear search")
        syslog.clear_search()
        log.info("switch to inactive tab")
        syslog.click_inactive_tab()
        syslog.visibility_of_first_inactive_syslog()
        first_syslog_name = syslog.get_name_first_syslog()
        assert updated_syslog_name == first_syslog_name

    @pytest.mark.regression
    def test_10_Activate_Syslog(self):
        """
            Verify the deactivating syslog functionality
            Validation 1: Based on the Status of the syslog
        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Search Functionality of Syslogs")
        syslog.search_input_string(updated_syslog_name)
        syslog.click_enter_for_search()
        log.info("Mouse hover the dropdown")
        syslog.check_drop_down()
        log.info("Click on active button")
        syslog.click_activate_button()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.get_tooltip_msg()
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        assert 'Success' in tooltip_msg
        log.info("Clear the search")
        syslog.clear_search()
        syslog.page_refresh()
        log.info("switch to active tab")
        syslog.click_active_tab()
        syslog.visibility_of_first_active_syslog()
        first_syslog_name = syslog.get_name_first_syslog()
        assert updated_syslog_name == first_syslog_name

    @pytest.mark.regression
    def test_11_Delete_Syslog(self):
        """
            Verify the delete syslog functionality
            Validation 1: Based on the Count of the syslogs

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Mouse over the dropdown")
        syslog.check_drop_down()
        syslog.click_delete_button()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.get_tooltip_msg()
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        assert 'Success' in tooltip_msg
        syslog.visibility_of_first_active_syslog()
        assert active_count == syslog.get_syslog_count()
