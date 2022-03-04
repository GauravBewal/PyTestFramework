import pytest

from pageObjects.ConfigureTrigger import ConfigureTrigger
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestConfigureTriggers(Base):

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_01_Verify_Configure_Triggers_redirection(self):
        """
            Verify Configure Triggers redirection from Main Menu
            Validation: Based on the page title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on Main menu")
        nav.click_main_menu()
        log.info("Click on configure event")
        nav.navigate_configure_event()
        page_heading = config_trigger.get_page_heading()
        assert action.get_title() == 'Configure Triggers | Cyware Orchestrate' and 'Configure Triggers' in page_heading

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Click_Configure_New_Trigger_btn(self):
        """
          Verify configuration of new trigger
          Validation 2: Based on the slider title
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on configure new trigger button")
        config_trigger.click_configure_trigger()
        log.info("Read the slider heading")
        slider_heading = config_trigger.get_slider_heading()
        log.info("Click on close slider button")
        config_trigger.click_close_slider()
        log.info("Validating the slider heading")
        assert slider_heading == 'New Configure Event'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on inactive tab")
        config_trigger.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = config_trigger.read_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on All tab")
        config_trigger.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = config_trigger.read_all_tab_color()
        assert tab_color == '#1a3ee8'
