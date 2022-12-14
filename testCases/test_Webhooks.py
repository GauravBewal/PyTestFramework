import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.CommonElements import Tooltip
from pageObjects.Navigation import Navigation
from pageObjects.Webhooks import Webhooks
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestWebhooks(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.webhooks
    def test_01_Verify_Admin_Webhooks_redirection(self):
        """
            Verify redirection of Webhooks from the admin page
            Validation - 1. On the basis of Window's title
            TC_ID : 001
        """
        global active_count
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on Admin menu")
        nav.click_admin_menu()
        log.info("Click on Webhooks tab from Admin Page")
        webhook.click_webhooks()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        active_count = webhook.get_webhook_count()
        assert action.get_title() in 'Webhooks | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.webhooks
    def test_03_Verify_Switch_to_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 3. On the basis of tab color
            TC_ID : 003
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Click on inactive tab")
        global inactive_count
        webhook.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = webhook.get_inactive_tab_color()
        webhook.Pass_even_first_inactive_Webhook_is_not_visible()
        inactive_count = webhook.get_webhook_count()
        assert webhook.get_inactive_tab_title() == 'Inactive' and tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.webhooks
    def test_04_Verify_Switch_to_All_tab(self):
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
        webhook.Pass_even_first_Active_Webhook_is_not_visible()
        all_tab_count = webhook.get_webhook_count()
        assert tab_color == '#1a3ee8' and all_tab_count == inactive_count + active_count

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.webhooks
    def test_02_Click_on_New_Webhook_btn(self):
        """
            Verify create button functionality of new webhook
            Validation - 2. On the basis of slider title
            TC_ID : 002
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        log.info("Switch to active tab")
        webhook.click_active_tab()
        webhook.Pass_even_first_Active_Webhook_is_not_visible()
        log.info("Click on add webhook button")
        webhook.click_new_webhook()
        log.info("Read the slider title")
        slider_title = webhook.get_slider_title()
        log.info("Click on close slider button")
        webhook.click_slider_close()
        assert slider_title == 'Add Webhook'

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_05_Create_Webhook(self):
        """
            Verify creation of webhooks
            Validation . On basis of button click and adding required data.
            TC_ID : 005
        """
        log = self.getlogger()
        webhook = Webhooks(self.driver)
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        global webhook_title
        global token
        log.info("Generating the new Webhook title")
        webhook_title = "test_webhook_" + action.get_current_time()
        log.info("Click on the create new button")
        webhook.click_new_webhook()
        log.info("Add the description")
        description = "New test webhook added by automation script"
        log.info("Add the Webhook title in the specified input field")
        webhook.put_webhook_title(webhook_title)
        log.info("Add the Webhook description in required webhook field")
        webhook.put_description_webhook(description)
        log.info("Select the expiration date")
        webhook.open_calendar()
        webhook.click_on_expiry_date()
        webhook.clear_select_time_field()
        webhook.click_on_select_time()
        webhook.click_enter_using_keyboard()
        log.info("Select the Bot User for the specified Webhook")
        webhook.click_on_list_user()
        webhook.select_first_user()
        log.info("Click on create/ Generate the Token")
        webhook.click_generate_token_btn()
        token = webhook.get_generated_token()
        log.info("Close the Create slider")
        webhook.click_slider_close()
        log.info("Read the tooltip message")
        toast_msg = tooltip.read_tooltip_msg()
        log.info("Close the tooltip")
        tooltip.click_close_tooltip()
        webhook.visibility_of_created_webhook()
        assert 'Success' in toast_msg
        assert active_count + 1 == webhook.get_webhook_count()

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_06_Check_Generated_Token(self):
        """
            Verify the Generated Token
            Validation -1 : Verify the data / Token shown in the webhook and the token generated during
            TC_ID : 006
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Get the Webhook token data and compare with the token generated at creation of Webhook")
        webhook.click_on_first_webhook()
        assert token == webhook.get_token_data()

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_07_Check_Base_URL(self):
        """
            Verify the Base Url generated for the Webhook
            Validation -1: Compare the Url generated while creating the Webhook
            TC_ID : 007
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Comparing the base url with the Generated Webhook Base Url")
        baseurl = ReadConfig.getAppURL() + "api/webhooks_auth/events/"
        assert baseurl == webhook.get_base_webhook_url()
        log.info("Click on close slider button")
        webhook.click_slider_close()

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_08_Search_Webhook(self):
        """
             Verify the search bar functionality
             Validation -1 : Compare the result with the searched/Updated webhook
             TC_ID : 008
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Verifying the searching of the created Webhook")
        log.info("Provide input for the search bar")
        webhook.search_input_string(webhook_title)
        log.info("Click Enter/Confirm")
        webhook.click_enter_using_keyboard()
        log.info("Visibility of first webhook")
        assert webhook.visibility_of_created_webhook() is True
        log.info("Get the first/ Name of the searched webhook")
        searched_name = webhook.get_first_webhhook_name()
        log.info("Assert based on the input to search bar and the webhook title that result shown.")
        assert searched_name == webhook_title

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_09_Update_Webhook_Name(self):
        """
            Update New Webhook Name
            Validation -1 : Comparing the Name the updated Webhook Name.
            TC_ID : 009
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        action = Action(self.driver)
        tooltip = Tooltip(self.driver)
        log.info("Click on the first Webhook in list")
        webhook.click_on_first_webhook()
        log.info("Clear the old name of Webhook")
        webhook.clear_webhook_title()
        log.info("Generating the New Webhook Name")
        global updated_webhook
        updated_webhook = "test_webhook_" + action.get_current_time()
        log.info("Update a New Name to Webhook")
        webhook.put_webhook_title(updated_webhook)
        log.info("Click Update/Save Button")
        webhook.update_webhook()
        log.info("read the toast message")
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("Close the tooltip")
        tooltip.click_close_tooltip()
        log.info("Click on clear search icon")
        webhook.Clear_Search_field()
        log.info("Press Enter")
        webhook.click_enter_using_keyboard()
        log.info("Visibility of created webhook")
        webhook.visibility_of_created_webhook()
        assert updated_webhook == webhook.get_first_webhhook_name()

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_10_Check_the_Dropdown_Edit_btn_functionality(self):
        """
            Verify the dropdown button Visibility.
            Validation -1 : Check The Edit Slider Title
            TC_ID:010
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        log.info("Search the new updated Webhook Name")
        webhook.search_input_string(updated_webhook)
        log.info("Press Enter")
        webhook.click_enter_using_keyboard()
        log.info("Wait till visibility of created webhook")
        assert webhook.visibility_of_created_webhook() is True
        log.info("Mouse over the dropdown")
        webhook.mouser_hover_on_more_options()
        log.info("check visibility of edit button")
        assert webhook.visibility_of_edit_btn() is True
        log.info("Click on Edit button in Drop down")
        webhook.click_edit_button()
        log.info("Get the Slider Name")
        slider_title = webhook.get_slider_title()
        log.info("Close the Slider")
        webhook.click_slider_close()
        assert slider_title == "Edit Webhook"

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_11_Copy_Token(self):
        """
            Verify user is able to copy the token
            Validation -1 : Verify by the notification status
            TC_ID :011
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Mouse Over the Drop down")
        webhook.mouser_hover_on_more_options()
        log.info("Visibility of copy token button")
        assert webhook.visibility_of_copy_token_btn() is True
        log.info("Click on the Copy token Button in Drop down")
        webhook.click_copy_token_button()
        log.info("Get the toast message Information")
        toast_message = tooltip.read_tooltip_msg()
        log.info("Close tool tip message")
        tooltip.click_close_tooltip()
        assert 'Success' == toast_message

    @pytest.mark.regression
    @pytest.mark.webhooks
    def test_12_Deactivate_Webhook(self):
        """
            Verify to deactivate the Webhook
            Validation 1: Based on the Count of the Inactive Webhook
            TC_ID : 012
        """
        webhook = Webhooks(self.driver)
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        log.info("Click on dropdown")
        webhook.mouser_hover_on_more_options()
        log.info("Check visibility of deactivate button")
        assert webhook.visibility_of_deactivate_btn() is True
        log.info("Click on inactive button")
        webhook.click_deactivate_btn()
        log.info("Read the tool tip message")
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("Close tooltip")
        tooltip.click_close_tooltip()
        log.info("Clear search field")
        webhook.Clear_Search_field()
        log.info("Click Enter using keyboard")
        webhook.click_enter_using_keyboard()
        log.info("Check visibility of first active webhook")
        webhook.Pass_even_first_Active_Webhook_is_not_visible()
        log.info("Switch to inactive Tab")
        webhook.click_inactive_tab()
        log.info("Wait until visibility of first inactive webhook")
        webhook.Pass_even_first_inactive_Webhook_is_not_visible()
        log.info("Enter Webhook name to search")
        webhook.search_input_string(updated_webhook)
        log.info("Click Enter to search")
        webhook.click_enter_using_keyboard()
        log.info("Check for visibility of first inactive webhook")
        assert webhook.visibility_of_created_webhook() is True
        log.info("Read the created webhook name")
        name = webhook.get_first_webhhook_name()
        assert updated_webhook == name
        log.info("Clear the search field")
        webhook.Clear_Search_field()
        log.info("Press Enter")
        webhook.click_enter_using_keyboard()
