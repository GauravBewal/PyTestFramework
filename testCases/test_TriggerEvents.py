import pytest

from pageObjects.Navigation import Navigation
from pageObjects.TriggerEvents import TriggerEvents
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestTriggerEvents(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
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
        assert action.get_title() == 'Trigger Events | Cyware Orchestrate' and 'Triggered Events' in page_heading

    @pytest.mark.regression
    @pytest.mark.readOnly
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
