import time

import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base
from configuration.readConfiguration import ReadConfig
from pageObjects.ConfigureTrigger import ConfigureTrigger


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
        time.sleep(ReadConfig.MediumsleepWait())
        action.javascript_click_element(config_trigger.click_configure_trigger())
        log.info("Read the slider heading")
        slider_heading = action.getText(config_trigger.get_slider_heading())
        log.info("Click on close slider button")
        action.click(config_trigger.click_close_slider())
        log.info("Validating the slider heading")
        assert slider_heading == 'New Configure Event'


