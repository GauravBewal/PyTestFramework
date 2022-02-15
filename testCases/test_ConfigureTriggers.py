import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.ConfigureTrigger import ConfigureTrigger
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestConfigureTriggers(Base):

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_01_configure_triggers_redirection(self):
        """
            Verify Configure Triggers redirection from Main Menu
            Validation: Based on the page title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Configure_Event())
        assert action.getTitle() in 'Configure Triggers | Cyware Orchestrate'
        time.sleep(ReadConfig.Wait_10_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_click_configure_new_trigger(self):
        """
          Verify configuration of new trigger
          Validation 2: Based on the slider title
        """
        log = self.getlogger()
        action = Action(self.driver)
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on configure new trigger button")
        action.click(config_trigger.click_configure_trigger())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the slider heading")
        slider_heading = action.getText(config_trigger.get_slider_heading())
        log.info("Click on close slider button")
        action.click(config_trigger.click_close_slider())
        log.info("Validating the slider heading")
        assert slider_heading == 'New Configure Event'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        action = Action(self.driver)
        log.info("Click on inactive tab")
        action.click(config_trigger.click_inactive_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(config_trigger.click_inactive_tab())
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        config_trigger = ConfigureTrigger(self.driver)
        action = Action(self.driver)
        log.info("Click on All tab")
        action.click(config_trigger.click_All_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(config_trigger.click_All_tab())
        assert tab_color == '#1a3ee8'

