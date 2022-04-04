import pytest

from pageObjects.ConfigureTrigger import ConfigureTrigger
from pageObjects.Navigation import Navigation
from pageObjects.CommonElements import Tooltip
from utilities.Actions import Action
from utilities.Base import Base

@pytest.mark.usefixtures("setup")
class TestConfigureTriggers(Base):

    @pytest.mark.readOnly
    @pytest.mark.regression
    @pytest.mark.configuretriggers
    def test_01_Verify_Configure_Triggers_redirection(self):
        """
            Verify Configure Triggers redirection from Main Menu
            Validation-1: Based on the page title
            TC-CT-001
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on Main menu")
        nav.click_main_menu()
        log.info("Click on configure event")
        nav.navigate_configure_event()
        log.info("Read page heading")
        page_heading = config_trigger.get_page_heading()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        global active_count
        active_count = config_trigger.get_configure_trigger_count()
        assert action.get_title() == 'Configure Triggers | Cyware Orchestrate' \
               and 'Configure Triggers' in page_heading and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.configuretriggers
    def test_02_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
            TC-CT-003
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on inactive tab")
        config_trigger.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = config_trigger.read_inactive_tab_color()
        config_trigger.visibility_of_first_inactive_configure_trigger()
        global inactive_count
        inactive_count = config_trigger.get_configure_trigger_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.configuretriggers
    def test_03_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
            TC-CT-004
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on All tab")
        config_trigger.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = config_trigger.read_all_tab_color()
        config_trigger.visibility_of_first_active_configure_trigger()
        all_tab_count = config_trigger.get_configure_trigger_count()
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count + active_count

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.configuretriggers
    def test_04_Click_Configure_New_Trigger_btn(self):
        """
          Verify configuration of new trigger
          Validation 2: Based on the slider title
          TC-CT-002
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Switching to active tab")
        config_trigger.click_active_tab()
        log.info("Check for visibility of first configure event")
        config_trigger.visibility_of_first_active_configure_trigger()
        log.info("Click on configure new trigger button")
        config_trigger.click_new_configure_trigger_btn()
        log.info("Read the slider heading")
        slider_heading = config_trigger.get_slider_heading()
        log.info("Click on close slider button")
        config_trigger.click_close_slider()
        log.info("Validating the slider heading")
        assert slider_heading == 'New Configure Event'

    @pytest.mark.regression
    @pytest.mark.configuretriggers
    def test_05_Create_New_Configure_Trigger(self):
        """
            Verify Create New Configure Trigger
            Validate -1 : On bases on Count of Configure Trigger
            TC-CT-005
        """
        log = self.getlogger()
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Creating a New Configure Trigger")
        config_trigger.click_new_configure_trigger_btn()
        log.info("Enter the data into Input Fields")
        global source_app
        source_app = "TestSource_App" + action.get_current_time()
        config_trigger.put_source_app_name(source_app)
        global Event_Type
        log.info("Enter the SourceEvent Data")
        Event_Type = "TestSourceEvent_Type" + action.get_current_time()
        config_trigger.put_source_event_type(Event_Type)
        config_trigger.click_on_label_field()
        log.info("Select the top most label")
        config_trigger.click_first_label()
        log.info("Enter the Create Button")
        config_trigger.click_create_btn()
        log.info("Read the tooltip msg")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("click on close toop tip")
        tooltip.click_close_tooltip()
        log.info("Check for visibility of first configure event")
        config_trigger.visibility_of_first_active_configure_trigger()
        assert active_count + 1 == config_trigger.get_configure_trigger_count()

    @pytest.mark.regression
    @pytest.mark.configuretriggers
    def test_06_Search_Configured_Trigger(self):
        """
            Verify the Searchbar Functionality is working.
            Validation-1: On basis of the Name Comparison.
            TC-CT-006
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Search Functionality of Configure Triggers")
        config_trigger.search_input_string(source_app)
        config_trigger.click_enter_for_search()
        search_result = config_trigger.get_first_configure_trigger_name()
        log.info("Clearing the Search Field")
        config_trigger.clear_search()
        assert source_app == search_result

    @pytest.mark.regression
    @pytest.mark.configuretriggers
    def test_07_Update_Configured_Trigger(self):
        """
            Verify the Update Functionality by Updating the Name
            Validation-1 : Validate on comparison of the First Configure Trigger Name and Input Name
            TC-CT-008
        """
        log = self.getlogger()
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Updating the Name of the Configure Trigger Source Name")
        config_trigger.click_first_configure_trigger()
        log.info("Clear The previous Name")
        config_trigger.clear_source_app_name()
        new_config_name = "TestConfig_Trigger" + action.get_current_time()
        log.info("Add a New Configure Trigger Source App Name")
        config_trigger.put_source_app_name(new_config_name)
        log.info("Click On Update")
        config_trigger.click_on_update()
        log.info("Read tooltip msg")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("click on close toop tip")
        tooltip.click_close_tooltip()
        log.info("Check for visibility of first configure event")
        config_trigger.visibility_of_first_active_configure_trigger()
        top_first_event_name = config_trigger.get_first_configure_trigger_name()
        assert new_config_name == top_first_event_name

    @pytest.mark.regression
    @pytest.mark.configuretriggers
    def test_08_Deactivate_Configured_Trigger(self):
        """
            Verify the Update Functionality of  Configure Trigger
            Validation-1 : Validate On basis on of the count in Inactive Tab
            TC-CT-007
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        tooltip = Tooltip(self.driver)
        tirgger_name_before_deactivating = config_trigger.get_first_configure_trigger_name()
        log.info("Click on Active Tab and select first configure trigger")
        config_trigger.click_first_configure_trigger()
        log.info("Deactivate the Configure Trigger")
        config_trigger.click_inactive_configure_trigger()
        log.info("Click on Update Button")
        config_trigger.click_on_update()
        log.info("Read tooltip msg")
        toast_msg = tooltip.get_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("click on close toop tip")
        tooltip.click_close_tooltip()
        config_trigger.click_inactive_tab()
        log.info("Check for visibility of first configure event")
        config_trigger.visibility_of_first_inactive_configure_trigger()
        trigger_name_after_deactivated = config_trigger.get_first_configure_trigger_name()
        assert tirgger_name_before_deactivating == trigger_name_after_deactivated
