import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Webhooks import Webhooks
from utilities.Actions import Action
from utilities.Base import Base
from configuration.readConfiguration import ReadConfig


@pytest.mark.usefixtures("setup")
class TestWebhooks(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Admin_Webhooks_redirection(self):
        """
            Verify redirection of Webhooks from the admin page
            Validation - 1. On the basis of Window's title
            TC_ID : 001
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
            TC_ID : 002
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
            TC_ID : 003
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Click on inactive tab")
        global count
        webhook.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = webhook.get_inactive_tab_color()
        count = webhook.get_webhook_count()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 3. On the basis of tab color
            TC_ID :004
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Click on All tab")
        webhook.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = webhook.get_all_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    def test_05_create_webhook(self):
        """
            verify the create webhooks
            Validation . On basis of Buttton Click and Adding required data.
            TC_ID : 005
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        action = Action(self.driver)
        log.info("Click On New Webhook Button")
        global webhook_title
        global token
        log.info("Generating the new Webhook title")
        webhook_title = "test_webhook_"+action.get_current_time()
        log.info("Get the Webhook count before the create function")
        count = webhook.get_webhook_count()
        log.info("Click on the create new button")
        webhook.click_new_webhook()
        log.info("Add the description")
        description = "New Test Webhook"
        log.info("Add the Webhook title in the specified input field")
        webhook.put_webhook_title(webhook_title)
        log.info("Add the Webhook description in required webhook field")
        webhook.put_description_webhook(description)
        log.info("Select the expiration date")
        webhook.open_calendar()
        webhook.click_on_expiry_date()
        webhook.click_confirm()
        log.info("Select the Bot User for the specified Webhook")
        webhook.click_on_list_user()
        webhook.select_first_user()
        log.info("Click on create/ Generate the Token")
        webhook.click_generate_token_btn()
        token = webhook.get_generated_token()
        log.info("Close the Create slider")
        webhook.click_slider_close()
        assert count + 1 == webhook.get_webhook_count()

    @pytest.mark.regression
    def test_06_deactive_webhook(self):
        """
            Verify the deactivate the Webhook
            Validation 1: Based on the Count of the Inactive Webhook
            TC_ID : 007
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Click on first Webhook listing")
        webhook.click_on_first_webhook()
        log.info("Click on Deactivate button")
        webhook.deactive_webhook()
        log.info("Click on Update Button")
        webhook.update_webhook()
        log.info("Click/ Switch on the inactive Tab")
        webhook.click_inactive_tab()
        assert count+1 == webhook.get_webhook_count()

    @pytest.mark.regression
    def test_07_check_generated_token(self):
        """
            Verify the Generated Token
            Validation -1 : Verify the data / Token shown in the webhook and the token generated during
            TC_ID : 008
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Get the Webhook token data and compare with the token generated at creation of Webhook")
        webhook.click_on_first_webhook()
        assert token == webhook.get_token_data()

    @pytest.mark.regression
    def test_08_check_base_url(self):
        """
            Verify the Base Url generated for the Webhook
            Validation -1: Compare the Url generated while creating the Webhook
            TC_ID : 008
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Comparing the base url with the Generated Webhook Base Url")
        baseurl = ReadConfig.getAppURL()+"api/webhooks_auth/events/"
        assert baseurl == webhook.get_base_webhook_url()

    # @pytest.mark.regression
    # def test_09_search_webhook(self):
    #     """
    #          Verify the search bar functionality
    #          Validation -1 : Compare the result with the searched/Updated webhook
    #          TC_ID : 009
    #     """
    #     webhook = Webhooks(self.driver)
    #     log = self.getlogger()
    #     webhook.search_input_string(webhook_title)
    #     webhook.click_confirm()
    #     searched_name = webhook.get_first_webhhook_name()
    #     webhook.clear_input_field()
    #     assert searched_name == webhook_title
    #
    # @pytest.mark.regression
    # def test_10_update_webhook_name(self):
    #     webhook = Webhooks(self.driver)
    #     log = self.getlogger()
    #     action = Action(self.driver)
    #     webhook.click_inactive_tab()
    #     webhook.click_on_first_webhook()
    #     webhook.clear_webhook_title()
    #     updated_webhook = "test_webhook_"+action.get_current_time()
    #     webhook.put_webhook_title(updated_webhook)
    #     webhook.update_webhook()
    #     webhook.search_input_string(updated_webhook)
    #     webhook.click_confirm()
    #     assert updated_webhook == webhook.get_first_webhhook_name()





