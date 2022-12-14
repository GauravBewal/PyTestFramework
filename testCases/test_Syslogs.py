import os
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

    # This module has dependency with configure trigger module. Please run both if wanted to run sylogs

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.syslogs
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
    @pytest.mark.syslogs
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
        syslog.Pass_even_first_inactive_syslog_is_not_visible()
        global inactive_count
        inactive_count = syslog.get_syslog_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.syslogs
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
        syslog.Pass_even_first_active_syslog_is_not_visible()
        global all_tab_count
        all_tab_count = syslog.get_syslog_count()
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count + active_count

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.syslogs
    def test_04_Click_New_Syslogs_btn(self):
        """
            Verify create button functionality of new syslogs
            Validation - 2. On the basis of slider title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        log.info("Switch to active tab")
        syslog.click_active_tab()
        log.info("Check for active syslog visibility")
        syslog.Pass_even_first_active_syslog_is_not_visible()
        log.info("Click on add syslog button")
        syslog.click_new_syslog()
        log.info("Read the slider title")
        slider_title = syslog.get_slider_title()
        log.info("Click on close slider button")
        syslog.click_slider_close()
        assert slider_title == 'Configure Syslog'

    @pytest.mark.regression
    @pytest.mark.syslogs
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
        log.info("Wait until visibility of first active configure trigger")
        config_trigger.visibility_of_first_active_configure_trigger()
        log.info("Switch to inactive tab")
        config_trigger.click_inactive_tab()
        log.info("Wait until visibility of first inactive configure trigger")
        config_trigger.visibility_of_first_inactive_configure_trigger()
        log.info("Get the first configure trigger name")
        global config_trigger_name
        config_trigger_name = config_trigger.get_first_configure_trigger_name()
        log.info("Click on the first configure trigger")
        config_trigger.click_first_configure_trigger()
        log.info("Make configure trigger as active")
        config_trigger.click_active_configure_trigger_btn()
        log.info("Click on update button")
        config_trigger.click_on_update()
        log.info("Read the success message")
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("Close tooltip")
        tooltip.click_close_tooltip()
        log.info("Click on Main menu")
        nav.click_admin_menu()
        log.info("Click on SysLogs tab from Admin Page")
        syslog.click_syslogs()
        log.info("Click on active tab")
        syslog.click_active_tab()
        log.info("Wait until first active syslog is visible")
        syslog.Pass_even_first_active_syslog_is_not_visible()
        global syslog_title
        syslog_title = "test_syslog_" + action.get_current_time()
        log.info("Click on the create new button")
        syslog.click_new_syslog()
        log.info("Add the Syslog title in the specified input field")
        syslog.put_syslog_title(syslog_title)
        port_number = syslog.generate_port_number()
        log.info("Add the Port Number in the specified input field")
        syslog.put_port_number(port_number)
        log.info("Click on source events app field")
        syslog.click_on_list_Source_Events_App()
        log.info("Enter configure trigger name")
        syslog.put_source_event_app(config_trigger_name)
        log.info("Select the Source Event App for the Syslog")
        syslog.select_first_source_event_app_and_type()
        log.info("Select the Source Event Type for the Syslog")
        syslog.click_on_list_Source_Events_Type()
        log.info("Select first source event app tye")
        syslog.select_first_source_event_app_and_type()
        log.info("Click on save button")
        syslog.click_save_btn()
        log.info("Read the tool tip message")
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("click on close toop tip")
        tooltip.click_close_tooltip()
        assert syslog.visibility_of_created_syslog() is True \
               and active_count + 1 == syslog.get_syslog_count()


    @pytest.mark.regression
    @pytest.mark.syslogs
    def test_06_Search_Syslog(self):
        """
            Verify the Searchbar Functionality is working.
            Validation-1: On basis of the Name Comparison.

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Enter String to search")
        syslog.Put_string_to_search(syslog_title)
        log.info("Press Enter")
        syslog.click_enter_for_search()
        log.info("Wait till visibility of first syslog")
        assert syslog.visibility_of_created_syslog() is True
        log.info("Get the first syslog name")
        search_result = syslog.get_first_syslog_name()
        assert syslog_title == search_result

    @pytest.mark.regression
    @pytest.mark.syslogs
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
        updated_syslog_name = "updated_syslog" + action.get_current_time()
        log.info("Clear the previous title")
        syslog.clear_syslog_title()
        log.info("Enter updated syslog name")
        syslog.put_syslog_title(updated_syslog_name)
        log.info("Click on save button")
        syslog.click_save_btn()
        log.info("Read tool tip message")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Close tool tip")
        tooltip.click_close_tooltip()
        assert 'Success' == toast_msg
        log.info("Clear search")
        syslog.click_clear_search_btn()
        assert syslog.visibility_of_created_syslog() is True
        log.info("Enter updated syslog name in search bar")
        syslog.Put_string_to_search(updated_syslog_name)
        log.info("Press Enter")
        syslog.click_enter_for_search()
        log.info("Wait until created syslpgs is visible")
        assert syslog.visibility_of_created_syslog() is True \
               and updated_syslog_name == syslog.get_first_syslog_name()

    @pytest.mark.regression
    @pytest.mark.syslogs
    def test_08_Check_the_Dropdown_Edit_Visibility(self):
        """
            Verify the dropdown button Visibility.
            Validation -1 : Check The Edit Slider Title
        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Clear search")
        syslog.click_clear_search_btn()
        assert syslog.visibility_of_created_syslog() is True
        log.info("Enter the syslog name to search")
        syslog.Put_string_to_search(updated_syslog_name)
        log.info("Press Enter to search")
        syslog.click_enter_for_search()
        log.info("Check for the visibility of first active syslog")
        syslog.Pass_even_first_active_syslog_is_not_visible()
        log.info("Mouse over the dropdown")
        syslog.check_drop_down()
        log.info("Check visibility of edit button")
        assert syslog.visibility_of_edit_button() is True
        log.info("Click on Edit button in Drop down")
        syslog.click_edit_button()
        log.info("Get the Slider Name")
        slider_title = syslog.get_slider_title()
        log.info("Close the Slider")
        syslog.click_slider_close()
        assert slider_title == "Edit Syslog"

    @pytest.mark.regression
    @pytest.mark.syslogs
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
        log.info("Check visibility of edit button")
        assert syslog.visibility_of_deactivate_button() is True
        log.info("Click on deactivate button")
        syslog.click_deactivate_button()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tooltip_msg
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        log.info("Clear search")
        syslog.click_clear_search_btn()
        log.info("Wait until visibility of active syslog")
        syslog.Pass_even_first_active_syslog_is_not_visible()
        log.info("switch to inactive tab")
        syslog.click_inactive_tab()
        log.info("Enter string to search")
        syslog.Put_string_to_search(updated_syslog_name)
        log.info("Press Enter to search")
        syslog.click_enter_for_search()
        log.info("Check for visibility of first inactive syslog")
        assert syslog.visibility_of_created_syslog() is True
        log.info("Get the first syslog name")
        first_syslog_name = syslog.get_first_syslog_name()
        assert updated_syslog_name == first_syslog_name

    @pytest.mark.regression
    @pytest.mark.syslogs
    def test_10_Activate_Syslog(self):
        """
            Verify the deactivating syslog functionality
            Validation 1: Based on the Status of the syslog
        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Mouse hover the dropdown")
        syslog.check_drop_down()
        log.info("Visibility of activate button")
        syslog.visibility_of_active_button()
        log.info("Click on active button")
        syslog.click_activate_button()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.read_tooltip_msg()
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        assert 'Success' == tooltip_msg
        log.info("Clear the search")
        syslog.click_clear_search_btn()
        log.info("Switch to active tab")
        syslog.click_active_tab()
        log.info("Visibility of created syslog")
        assert syslog.visibility_of_created_syslog() is True
        log.info("Enter String to search")
        syslog.Put_string_to_search(updated_syslog_name)
        log.info("Press Enter to search")
        syslog.click_enter_for_search()
        log.info("Check for first active syslog")
        assert syslog.visibility_of_created_syslog() is True
        log.info("Read the first syslog name")
        syslog_name = syslog.get_first_syslog_name()
        assert updated_syslog_name == syslog_name

    @pytest.mark.regression
    @pytest.mark.syslogs
    def test_11_Delete_Syslog(self):
        """
            Verify the delete syslog functionality
            Validation 1: Based on the Count of the syslogs

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        nav = Navigation(self.driver)
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Mouse over the dropdown")
        syslog.check_drop_down()
        log.info("Check visibility of delete button")
        assert syslog.visibility_of_delete_button() is True
        log.info("Click on delete button")
        syslog.click_delete_button()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tooltip_msg
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        log.info("Click on search clear button")
        syslog.click_clear_search_btn()
        log.info("Wait till visibility of first active syslog")
        syslog.Pass_even_first_active_syslog_is_not_visible()
        assert active_count == syslog.get_syslog_count()
        log.info("Click on to main menu")
        nav.click_main_menu()
        log.info("Click on configure event")
        nav.navigate_configure_event()
        log.info("Switch to active tab")
        config_trigger.click_active_tab()
        log.info("Wait until visibility of first active configure trigger")
        config_trigger.visibility_of_first_active_configure_trigger()
        log.info("Search for activated configure trigger")
        config_trigger.search_input_string(config_trigger_name)
        log.info("Press Enter")
        config_trigger.click_enter_for_search()
        log.info("Click on the first config trigger")
        config_trigger.click_first_configure_trigger()
        log.info("Click on inactive toggle ")
        config_trigger.click_inactive_configure_trigger()
        log.info("Click on update button")
        config_trigger.click_on_update()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tooltip_msg
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        log.info("Clear Search ")
        config_trigger.clear_search()

