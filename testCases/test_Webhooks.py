import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Webhooks import Webhooks
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestWebhooks(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Admin_Webhooks_redirection(self):
        """
            Verify redirection of Webhooks from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on Admin menu")
        nav.click_admin_menu()
        log.info("Click on Webhooks tab from Admin Page")
        webhook.click_webhooks()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() in 'Webhooks | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Click_New_Webhook_btn(self):
        """
            Verify create button functionality of new webhook
            Validation - 2. On the basis of slider title
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Click on add webhook button")
        webhook.click_new_webhook()
        log.info("Read the slider title")
        slider_title = webhook.get_slider_title()
        log.info("Click on close slider button")
        webhook.click_slider_close()
        assert slider_title == 'Add Webhook'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Click on inactive tab")
        webhook.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = webhook.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Click on All tab")
        webhook.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = webhook.get_all_tab_color()
        assert tab_color == '#1a3ee8'
