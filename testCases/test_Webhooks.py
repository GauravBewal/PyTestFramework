import time

import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Webhooks import Webhooks
from utilities.Actions import Action
from utilities.Base import Base
from configuration.readConfiguration import ReadConfig


@pytest.mark.usefixtures("setup")
class TestWebhooks(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_admin_Webhooks_redirection(self):
        """
            Verify redirection of Webhooks from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on Admin menu")
        action.click(nav.click_Admin_Menu())
        log.info("Click on Webhooks tab from Admin Page")
        action.click(webhook.click_Webhooks())
        assert action.getTitle() in 'Webhooks | Cyware Orchestrate'
        time.sleep(ReadConfig.Wait_10_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_click_new_webhook_btn(self):
        """
            Verify create button functionality of new webhook
            Validation - 2. On the basis of slider title
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        action = Action(self.driver)
        log.info("Click on add webhook button")
        action.click(webhook.click_new_webhook())
        log.info("Read the slider title")
        time.sleep(ReadConfig.Wait_3_Sec())
        slider_title = action.getText(webhook.get_slider_title())
        log.info("Click on close slider button")
        action.click(webhook.click_slider_close())
        assert slider_title == 'Add Webhook'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        action = Action(self.driver)
        webhook = Webhooks(self.driver)
        log.info("Click on inactive tab")
        action.click(webhook.click_inactive_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(webhook.click_inactive_tab())
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Verify_switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        action = Action(self.driver)
        webhook = Webhooks(self.driver)
        log.info("Click on All tab")
        action.click(webhook.click_All_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(webhook.click_All_tab())
        assert tab_color == '#1a3ee8'
