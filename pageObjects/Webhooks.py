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
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_webhooks)

    btn_new_webhook = "//header//button"

    def click_new_webhook(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.btn_new_webhook)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, Webhooks.text_slider_heading)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_inactive, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.tab_active)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.tab_All)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_All, 'color')

    webhook_title = "(//div[contains(@class,'cy-input')]//input)[1]"

    def put_webhook_title(self, value):
        return Action.send_keys(self, By.XPATH, Webhooks.webhook_title, value)

    def clear_webhook_title(self):
        return Action.clear_field(self, By.XPATH, Webhooks.webhook_title)

    expiry_calendar = "//i[contains(@class,'cyicon-calendar')]"

    def open_calendar(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.expiry_calendar)

    select_expiry_date = "(//tr//td[contains(@class,'today')])[1]"

    def click_on_expiry_date(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.select_expiry_date)

    list_user = "//div[@name='bot_user']//span[contains(@class,'cyicon-chevron-down')]"

    def click_on_list_user(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.list_user)

    top_1_user = "//div[@name='bot_user']//li[1]"

    def select_first_user(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.top_1_user)

    description = "//div[contains(@class,'cy-textarea')]//textarea"

    def put_description_webhook(self, value):
        return Action.send_keys(self, By.XPATH, Webhooks.description, value)

    generate_btn = "//div[contains(@class,'px-5 text-right')]//button"

    def click_generate_token_btn(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.generate_btn)

    title_count = "//h1[contains(text(),'Webhooks (')]"

    def get_webhook_count(self):
        return Action.get_count_from_string(self, By.XPATH, Webhooks.title_count)

    first_active_webhook = "(//span[text()='Active' and @class='status__text'])[1]"

    def visibility_of_first_active_webhook(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, Webhooks.first_active_webhook)

    first_inactive_webhook = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def visibility_of_first_inactive_webhook(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, Webhooks.first_inactive_webhook)

    def click_enter_using_keyboard(self):
        time.sleep(3)
        return Action.click_enter(self)

    get_token = "//div[@id='token__data-new']"

    def get_generated_token(self):
        return Action.get_text(self, By.XPATH, Webhooks.get_token)

    first_webhook = "//tr[1]//a"

    def click_on_first_webhook(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.first_webhook)

    def get_first_webhhook_name(self):
        return Action.get_text(self, By.XPATH, Webhooks.first_webhook)

    token_data = "(//div[@id='token__data'])[1]"

    def get_token_data(self):
        return Action.get_text(self, By.XPATH, Webhooks.token_data)

    active_btn = "//span[@class='cyicon-check']"

    def deactivate_webhook(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.active_btn)

    def update_webhook(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.generate_btn)

    webhook_baseurl = "(//div[@id='token__data'])[2]"

    def get_base_webhook_url(self):
        return Action.get_text(self, By.XPATH, Webhooks.webhook_baseurl)

    main_input = "//input[@id='main-input']"

    def search_input_string(self, value):
        return Action.send_keys(self, By.XPATH, Webhooks.main_input, value)

    def clear_input_field(self):
        return Action.clear_field(self, By.XPATH, Webhooks.main_input)

    search_bar_clear_btn = "//div[contains(@class,'clear-button')]"

    def click_on_search_clear_btn(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.search_bar_clear_btn)

    three_dot = "(//i[contains(@class,'icon-more-vertical')]/parent::span)[1]"

    def check_drop_down(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Webhooks.three_dot)

    edit_button = "//body/ul[1]/li[1]"

    def click_edit_button(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.edit_button)

    copy_token = "//body/ul[1]/li[2]"

    def click_copy_token_button(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.copy_token)

    deactivate = "//body/ul[1]/li[3]"

    def click_deactivate_webhook(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.deactivate)

    select_time = "//input[contains(@placeholder,'Select time')]"

    def clear_select_time_field(self):
        return Action.clear_field(self, By.XPATH, Webhooks.select_time)

    def click_on_select_time(self):
        return Action.send_keys(self, By.XPATH, Webhooks.select_time, "11:59:59 PM")

