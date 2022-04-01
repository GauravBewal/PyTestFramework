import pytest

from pageObjects.CommonElements import Tooltip
from pageObjects.Navigation import Navigation
from pageObjects.TriggerEvents import TriggerEvents
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestTriggerEvents(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.triggerevents
    def test_01_Verify_Trigger_Events_redirection(self):
        """
            Verify Trigger Events redirection from Main Menu
            Validation 1: Based on the page title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        trigger_events = TriggerEvents(self.driver)
        action = Action(self.driver)
        log.info("click on main menu")
        nav.click_main_menu()
        log.info("click on trigger events")
        nav.navigate_trigger_event()
        log.info("Read page heading")
        page_heading = trigger_events.get_page_heading()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        global active_count
        active_count = trigger_events.get_events_count()
        assert action.get_title() == 'Trigger Events | Cyware Orchestrate' \
               and 'Triggered Events' in page_heading and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.triggerevents
    def test_02_Click_New_Event_btn(self):
        """
            Verify creation of new trigger event from trigger event page
            Validation 2: Based on slider heading
        """
        log = self.getlogger()
        trigger_events = TriggerEvents(self.driver)
        log.info("Click on create new event button")
        trigger_events.click_create_new_event()
        log.info("Reading the slider heading")
        page_title = trigger_events.get_slider_text()
        trigger_events.click_close_slider()
        assert page_title == 'New Triggered Event'

    @pytest.mark.regression
    @pytest.mark.triggerevents
    def test_03_Create_Trigger_Event(self):
        """
        Verify whether user is able to create new trigger event
        Validation 1: Based on the count increased and successful msg
        """
        log = self.getlogger()
        trigger_events = TriggerEvents(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on the create new button")
        trigger_events.click_create_new_event()
        global event_name
        event_name = "ui_automation_event " + action.get_current_time()
        log.info("Enter the trigger name")
        trigger_events.put_event_name(event_name)
        log.info("Click on the label field")
        trigger_events.click_on_labels_field()
        log.info("Select the first label")
        trigger_events.click_on_top_label()
        log.info("Click on create button")
        trigger_events.click_on_create_button()
        log.info("Read the successful message")
        creation_msg = tooltip.get_tooltip_msg()
        log.info("Close the tool tip")
        tooltip.click_close_tooltip()
        events_count_after_creation = trigger_events.get_events_count()
        assert creation_msg == 'Success' and active_count + 1 == events_count_after_creation

    @pytest.mark.regression
    @pytest.mark.triggerevents
    def test_04_Search_Trigger_Event(self):
        """
        Verify user is able to search the created event
        Validation 1: Based on the event name visibility
        """
        log = self.getlogger()
        trigger_events = TriggerEvents(self.driver)
        log.info("click on the search bar")
        trigger_events.put_string_to_search(event_name)
        log.info("Click on ENTER")
        trigger_events.click_enter_for_search()
        read_top_search_result = trigger_events.get_first_event_name()
        trigger_events.clear_search()
        log.info("Validating search results")
        assert event_name == read_top_search_result
