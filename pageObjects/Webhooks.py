import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class Webhooks(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_webhooks = "//p[contains(text(),'Webhook')]/parent::div/parent::div"

    def click_webhooks(self):
        """
            Click on webhook
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_webhooks)

    btn_new_webhook = "//header//button"

    def click_new_webhook(self):
        """
            Click on new webhook button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.btn_new_webhook)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        """
            Get New Webhook slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, Webhooks.text_slider_heading)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        """
            Click on close slider button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        """
            Click on Inactive tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.tab_inactive)

    inactive_tab_text = "//*[@id='-tab-2']/a"

    def get_inactive_tab_title(self):
        """
            Get the text of inactive tab text
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.inactive_tab_text)

    def get_inactive_tab_color(self):
        """
            Get Inactive tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_inactive, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        """
            Click on active tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.tab_active)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.tab_All)

    def get_all_tab_color(self):
        """
            Get all tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_All, 'color')

    webhook_title = "(//div[contains(@class,'cy-input')]//input)[1]"

    def put_webhook_title(self, value):
        """
            Put webhook title in text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, Webhooks.webhook_title, value)

    def clear_webhook_title(self):
        """
            Clear Webhook title text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, Webhooks.webhook_title)

    expiry_calendar = "//i[contains(@class,'cyicon-calendar')]"

    def open_calendar(self):
        """
            Open calender
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.expiry_calendar)

    select_expiry_date = "(//tr//td[contains(@class,'today')])[1]"

    def click_on_expiry_date(self):
        """
            Click on expiry date
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.select_expiry_date)

    list_user = "//div[@name='bot_user']//span[contains(@class,'cyicon-chevron-down')]"

    def click_on_list_user(self):
        """
            Click on list user
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.list_user)

    top_1_user = "//div[@name='bot_user']//li[1]"

    def select_first_user(self):
        """
            Select first user
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.top_1_user)

    description = "//div[contains(@class,'cy-textarea')]//textarea"

    def put_description_webhook(self, value):
        """
            Put description on text field on webhook
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, Webhooks.description, value)

    generate_btn = "//div[contains(@class,'px-5 text-right')]//button"

    def click_generate_token_btn(self):
        """
            Click on generate button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Webhooks.generate_btn)

    title_count = "//h1[contains(text(),'Webhooks (')]"

    def get_webhook_count(self):
        """
            Get webhook total count
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, Webhooks.title_count)

    first_active_webhook = "(//span[text()='Active' and @class='status__text'])[1]"

    def Pass_even_first_Active_Webhook_is_not_visible(self):
        """
            Wait until visibility of first active webhook. It will pass even the element is not visible
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, Webhooks.first_active_webhook)

    first_webhook = "(//tr//td//a)[1]"

    def visibility_of_created_webhook(self):
        """
        Visibility of created webhook
        :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Webhooks.first_webhook)


    def click_on_first_webhook(self):
        """
            Click on first webhook from table
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.first_webhook)

    def get_first_webhhook_name(self):
        """
            Get first webhook name from table
            :return:
        """
        return Action.get_text(self, By.XPATH, Webhooks.first_webhook)

    first_inactive_webhook = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def Pass_even_first_inactive_Webhook_is_not_visible(self):
        """
            Wait until visibility of first inactive webhook. It will pass even the element is not visible
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, Webhooks.first_inactive_webhook)

    def click_enter_using_keyboard(self):
        """
            Click enter using Keyboard
            :return:
        """
        return Action.Press_enter(self)


    get_token = "//div[@id='token__data-new']"

    def get_generated_token(self):
        """
            Get generated token
            :return:
        """
        return Action.get_text(self, By.XPATH, Webhooks.get_token)


    token_data = "(//div[@id='token__data'])[1]"

    def get_token_data(self):
        """
            Get token data
            :return:
        """
        return Action.get_text(self, By.XPATH, Webhooks.token_data)

    active_btn = "//span[@class='cyicon-check']"

    def deactivate_webhook(self):
        """
            Deactivate webhook
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.active_btn)

    def update_webhook(self):
        """
            Update webhook
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.generate_btn)

    webhook_baseurl = "(//div[@id='token__data'])[2]"

    def get_base_webhook_url(self):
        """
            Get base webhook URL
            :return:
        """
        return Action.get_text(self, By.XPATH, Webhooks.webhook_baseurl)

    main_input = "//input[@id='main-input']"

    def search_input_string(self, value):
        """
            Search input string for webhook title
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, Webhooks.main_input, value)

    def Clear_Search_field(self):
        """
            Clear input field
            :return:
        """
        return Action.clear_field(self, By.XPATH, Webhooks.main_input)



    dd_more_options = "(//span[@role='button']/parent::div[@class='el-dropdown'])[1]"

    def mouser_hover_on_more_options(self):
        """
            Check dropdown
            :return:
        """
        return Action.mouse_hover_on_element(self, By.XPATH, Webhooks.dd_more_options)

    edit_button = "//body/ul[1]/li[1]"

    def click_edit_button(self):
        """
            Click edit button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.edit_button)

    def visibility_of_edit_btn(self):
        """
        Wait visibility of edit button
        :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Webhooks.edit_button)

    copy_token = "//body/ul[1]/li[2]"

    def click_copy_token_button(self):
        """
            Click on copy token button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.copy_token)

    def visibility_of_copy_token_btn(self):
        """
        Visibility of copy token btn
        :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Webhooks.copy_token)

    deactivate_btn = "//body/ul[1]/li[3]"

    def click_deactivate_btn(self):
        """
            Click on deactivate webhook
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Webhooks.deactivate_btn)

    def visibility_of_deactivate_btn(self):
        """
        Visibility of deactivate button
        :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Webhooks.deactivate_btn)

    select_time = "//input[contains(@placeholder,'Select time')]"

    def clear_select_time_field(self):
        """
            Clear Select time field
            :return:
        """
        return Action.clear_field(self, By.XPATH, Webhooks.select_time)

    def click_on_select_time(self):
        """
            Click on select time
            :return:
        """
        return Action.send_keys(self, By.XPATH, Webhooks.select_time, "11:59:59 PM")
