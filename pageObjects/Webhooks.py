from selenium.webdriver.common.by import By
from utilities.Actions import Action
from configuration.readConfiguration import ReadConfig

import time


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

    tab_inactive = "//li[3]/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Webhooks.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.tab_All)

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

    select_expiry_date = "(//table[contains(@class,'el-date-table')]//td[@class='available'])[1]"

    def click_on_expiry_date(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.select_expiry_date)

    list_user = "//div[contains(@class,'cy-select__menu--chevron-transform')]"

    def click_on_list_user(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.wait_and_click(self, By.XPATH, Webhooks.list_user)

    top_1_user = "(//div//ul[@id='dropdown-list']//div)[1]"

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
        time.sleep(ReadConfig.Wait_6_Sec())
        return Action.get_count_from_string(self, By.XPATH, Webhooks.title_count)

    def click_confirm(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.click_enter(self)

    get_token = "//div[@id='token__data-new']"

    def get_generated_token(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.get_text(self, By.XPATH, Webhooks.get_token)

    first_webhook = "(//tr[contains(@class, 'el-table__row')]//div//span//a)[1]"

    def click_on_first_webhook(self):
        return Action.javascript_click(self, By.XPATH, Webhooks.first_webhook)

    def get_first_webhhook_name(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.get_text(self, By.XPATH, Webhooks.first_webhook)

    token_data = "(//div[@id='token__data'])[1]"

    def get_token_data(self):
        return Action.get_text(self, By.XPATH, Webhooks.token_data)

    active_btn = "//span[@class='cyicon-check']"

    def deactive_webhook(self):
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

    three_dot = "(//div[contains(@class,'el-dropdown')]//span//i[contains(@class,'icon icon-more-vertical ')])[1]"

    def check_drop_down(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Webhooks.three_dot)

    edit_button = "(//ul//li[@class='el-dropdown-menu__item'][normalize-space()='Edit'])[1]"

    def click_edit_button(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.edit_button)

    copy_token = "(//ul//li[@class='el-dropdown-menu__item'][normalize-space()='Copy Token'])[1]"

    def click_copy_token_button(self):
        return Action.wait_and_click(self, By.XPATH, Webhooks.copy_token)

    success_toast_message = "(//div[@role='alert']//span[contains(text(),'Success')])[1]"

    def check_success_copy_token(self):
        return Action.check_visibility_of_element(self, By.XPATH, Webhooks.success_toast_message)

