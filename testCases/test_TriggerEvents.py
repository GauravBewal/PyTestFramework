import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base
from pageObjects.TriggerEvents import TriggerEvents


@pytest.mark.usefixtures("setup")
class TestTriggerEvents(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_trigger_events_redirection(self):
        """
            Verify Trigger Events redirection from Main Menu
            Validation 1: Based on the page title
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("click on main menu")
        action.click(nav.click_Main_Menu())
        log.info("click on trigger events")
        action.click(nav.Navigate_Trigger_Event())
        assert action.getTitle() in 'Trigger Events | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_click_new_event(self):
        """
        Verify creation of new trigger event from trigger event page
        Validation 2: Based on slider heading
        """
        log = self.getlogger()
        action = Action(self.driver)
        trigger_events = TriggerEvents(self.driver)
        log.info("Click on create new event button")
        action.javascript_click_element(trigger_events.click_create_new_event())
        # action.click(trigger_events.click_create_new_event())
        log.info("Reading the slider heading")
        time.sleep(ReadConfig.mediumSleepWait())
        page_title = action.getText(trigger_events.get_slider_text())
        action.click(trigger_events.click_close_slider())
        assert page_title == 'New Triggered Event'

