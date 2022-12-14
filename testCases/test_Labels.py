import time

import pytest

from pageObjects.ConfigureTrigger import ConfigureTrigger
from pageObjects.Labels import Labels
from pageObjects.Navigation import Navigation
from pageObjects.Playbooks import Playbooks
from pageObjects.Runlogs import Runlogs
from pageObjects.TriggerEvents import TriggerEvents
from pageObjects.CommonElements import Tooltip
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestLabels(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.labels
    def test_01_Labels_redirection(self):
        """
            Verify Labels Page redirection from Main Menu
            TC_ID: Label-TC-001
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Click on to main menu")
        nav.click_main_menu()
        log.info("Click on to label module for redirection")
        nav.navigate_labels()
        log.info("Validating the page title")
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        log.info("Read the no of active labels available")
        global active_labels
        active_labels = label.get_label_count()
        assert action.get_title() == 'Labels | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.labels
    def test_02_Switch_to_Inactive_tab(self):
        """
        Verify whether user is able to switch to inactive tab
        Validation based on the tab color
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Click on the inactive tab")
        label.click_inactive_tab()
        log.info("Read the tab color")
        tab_color = label.get_inactive_tab_color()
        log.info("Check visibility of first inactive label")
        label.Pass_even_inactive_label_is_not_visible()
        log.info("Read the no of inactive labels available")
        global inactive_labels
        inactive_labels = label.get_label_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.labels
    def test_03_Switch_to_All_tab(self):
        """
                Verify whether user is able to switch to all tab
                Validation based on the tab color
                """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Click on the inactive tab")
        label.click_all_tab()
        log.info("Read the tab color")
        tab_color = label.get_all_tab_color()
        log.info("Check visibility of first label")
        label.Pass_even_active_label_is_not_visible()
        log.info("Read the no of active labels available")
        all_tab_count = label.get_label_count()
        assert tab_color == '#1a3ee8' and all_tab_count == active_labels + inactive_labels

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.labels
    def test_04_Click_on_Create_Label_btn(self):
        """
            Verify user is able to get error message when tried to create a label without any name
            TC_ID: Label-TC-002
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Switch to active tab")
        label.click_active_tab()
        log.info("Check visibility of first label")
        label.Pass_even_active_label_is_not_visible()
        log.info("Click on to New Label Button")
        label.click_new_label()
        slider_title = label.get_label_slider_title()
        log.info("Click on to close label slider button")
        label.close_label_slider()
        assert slider_title == 'New Label'

    @pytest.mark.regression
    @pytest.mark.labels
    def test_05_Create_New_Label(self):
        """
            Verify Label Create functionality
            TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on to create new label")
        label.click_new_label()
        global label_text
        label_text = "ui_automation_label" + action.get_current_time()
        log.info("Entering new label name")
        label.put_label_name(label_text)
        log.info("Entering label description")
        label.put_description("Test Description")
        log.info("Click on create label button")
        label.create_Label()
        log.info("Read the tool tip msg")
        tooltip_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tooltip_msg
        log.info("Click on to close label creation tooltip ")
        tooltip.click_close_tooltip()
        log.info("Check visibility of first label")
        assert label.visibility_of_created_label() is True
        log.info("Reading count of total labels after creating a new label")
        after_label_creation_count = label.get_label_count()
        log.info("Read the first label name")
        get_created_label_name = label.get_top_1_label_name()
        log.info("Validating total count of labels before and after creation of new label, also checking the "
                 "newly created label is listing or not")
        assert label_text == get_created_label_name and active_labels + 1 == after_label_creation_count

    @pytest.mark.regression
    @pytest.mark.labels
    def test_06_Search_Label(self):
        """
            Verify Search functionality of the Labels
            TC_ID: Label-TC-005
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Entering" + label_text + "text for searching")
        label.put_search_string(label_text)
        log.info("Click on ENTER")
        label.click_enter_for_search()
        log.info("Wait until first label is visible")
        assert label.visibility_of_created_label() is True
        read_top_search_result = label.get_top_1_label_name()
        log.info("Validating search results")
        assert label_text == read_top_search_result

    @pytest.mark.regression
    @pytest.mark.labels
    def test_07_Update_Label(self):
        """
          verify user is able to update the label
          TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on label present at top in listing")
        label.click_top_first_label()
        log.info("Deleting and Entering new name to the existing label")
        label.clear_label_field()
        global new_label_name
        new_label_name = "ui_automation_label" + action.get_current_time()
        label.put_label_name(new_label_name)
        log.info("Deleting and entering new description the existing label")
        label.clear_description_field()
        label.put_description("updated description")
        log.info("Click on update label button")
        label.click_update_label()
        log.info("Read tool tip msg")
        tooltip_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tooltip_msg
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        log.info("Clear search")
        label.clear_search()
        log.info("Enter update label name")
        label.put_search_string(new_label_name)
        log.info("Click Enter")
        label.click_enter_for_search()
        assert label.visibility_of_created_label() is True
        top_label = label.get_top_1_label_name()
        log.info("Clear search")
        label.clear_search()
        log.info("Validating the new label name is updated or not ")
        assert new_label_name == top_label

    @pytest.mark.regression
    @pytest.mark.labels
    def test_08_Read_Modified_Created_Column_Data(self):
        """
        Verify user is able to see the created by and modified by details after creating and modifying label
        TC_ID: Label-TC-002
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Reading label created user name")
        label_created_user_name = label.get_label_created_user()
        log.info("Reading label modified user name")
        label_modified_user_name = label.get_label_modified_user()
        log.info("Validating both created and modified user")
        assert label_created_user_name == label_modified_user_name

    @pytest.mark.regression
    @pytest.mark.labels
    def test_09_Verify_Label_Listing_While_Configuring_Event(self):
        """
        Verify whether created label is getting listed while configuring event
        Validation 1: Based on the label visibility
        """
        log = self.getlogger()
        configure_event = ConfigureTrigger(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Navigate to configure events")
        nav.navigate_configure_event()
        log.info("Check for visibility of first configure event")
        configure_event.visibility_of_first_active_configure_trigger()
        log.info("Click on new button")
        configure_event.click_new_configure_trigger_btn()
        log.info("Click on the label field")
        configure_event.click_on_label_field()
        log.info("Enter label name")
        configure_event.put_label_name(new_label_name)
        log.info("Get the first label name")
        top_label = configure_event.get_top_label()
        assert top_label == new_label_name
        configure_event.click_close_slider()

    @pytest.mark.regression
    @pytest.mark.labels
    def test_10_Trigger_Label_Linked_Playbook(self):
        """
        Verify whether user is able to see the created label in playbook
        Validation-1: Based on the label visibility
        """
        log = self.getlogger()
        playbook = Playbooks(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        runlogs = Runlogs(self.driver)
        tooltip = Tooltip(self.driver)
        trigger_events = TriggerEvents(self.driver)
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Navigate to playbook module")
        nav.navigate_manage_playbook()
        log.info("Check visibility of walkthrough")
        playbook.click_on_close_walkthrough()
        log.info("Visibility of first playbook")
        playbook.Pass_even_first_custom_playbook_is_not_visible()
        log.info("Click on create new playbook")
        playbook.click_on_create_playbook_btn()
        log.info("Check if walk through is initiated")
        playbook.click_on_close_walkthrough()
        log.info("Click on the playbook overview button")
        playbook.click_on_playbook_overview_btn()
        log.info("Clear default name")
        playbook.remove_default_playbook_name()
        log.info("Enter playbook name")
        global playbook_name
        playbook_name = "label_test" + action.get_current_time()
        playbook.enter_playbook_name(playbook_name)
        log.info("Click on labels dropdown")
        playbook.click_on_label_field()
        log.info("Enter the label name")
        playbook.put_label_name(new_label_name)
        assert playbook.visibility_of_label(new_label_name) is True
        playbook.click_on_top_searched_label()
        log.info("Click on label field to close")
        playbook.click_on_label_field()
        log.info("Mouse hover on the save button")
        playbook.mouse_hover_on_save_btn()
        log.info("Click on save and exit button")
        playbook.click_save_and_exit_btn()
        log.info("Read the tooltip msg")
        tool_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tool_msg
        log.info("Click on close tooltip")
        tooltip.click_close_tooltip()
        log.info("Click on back button")
        playbook.click_on_back_button()
        log.info("Wait till visibility of first playbook")
        playbook.Pass_even_first_custom_playbook_is_not_visible()
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Navigate to triggered events module")
        nav.navigate_trigger_event()
        log.info("Click on create new event button")
        trigger_events.click_create_new_event()
        global event_name
        event_name = "ui_automation" + action.get_current_time()
        log.info("Enter the event title")
        trigger_events.put_event_name(event_name)
        log.info("Click on the labels field")
        trigger_events.click_on_labels_field()
        log.info("Enter label name to search")
        trigger_events.enter_label_name_to_search(new_label_name)
        log.info("Check visibility of created label")
        assert trigger_events.visibility_of_label(new_label_name) is True
        log.info("Click on the first label")
        trigger_events.click_on_top_label()
        log.info("close the label field")
        trigger_events.click_on_labels_field()
        log.info("Click on create button")
        trigger_events.click_on_create_button()
        log.info("Read tooltip msg")
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        tooltip.click_close_tooltip()
        log.info("Navigate to run logs")
        nav.click_main_menu()
        log.info("Navigate to run logs")
        nav.navigate_run_logs()
        assert 'Run Logs' in runlogs.get_read_heading()
        log.info("Refresh the page to make sure apis are up to date")
        nav.page_refresh()
        assert runlogs.verify_playbook_visibility_in_runlog(playbook_name) is True


    @pytest.mark.regression
    @pytest.mark.labels
    def test_11_Deactivate_Label(self):
        """
        Verify label is being listed under inactive tab once label was de-activated
        TC_ID: Label-TC-003
        """
        log = self.getlogger()
        label = Labels(self.driver)
        nav = Navigation(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Navigate to playbook module")
        nav.navigate_labels()
        log.info("Check for visibility of first label")
        assert label.visibility_of_created_label() is True
        label_name_before_deactivating = label.get_top_1_label_name()
        log.info("Click on label present at top in listing")
        label.click_top_first_label()
        log.info("Click on label inactive toggle")
        label.click_inactive_toggle()
        log.info("Click on update label button")
        label.click_update_label()
        log.info("Read tool tip msg")
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        tooltip.click_close_tooltip()
        log.info("Wait till visibility of active label")
        label.Pass_even_active_label_is_not_visible()
        log.info("Click on inactive button")
        # navigating inactive tab to check whether the label is de-activated or not
        label.click_inactive_tab()
        label.Pass_even_inactive_label_is_not_visible()
        log.info("Validating label name before and after deactivating")
        # checking whether same label is visible in inactive tab listing after deactivating it
        assert label_name_before_deactivating == label.get_top_1_label_name()
