import time

from selenium.webdriver.common.by import By
from utilities.Actions import Action

class OpenApi(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_open_API = "//p[contains(text(),'Open API')]/parent::div/parent::div"

    def click_open_api_tab(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.tab_open_API)

    btn_new_open_api = "//button[contains(@aria-describedby,'el-tooltip')]"

    def click_new_open_api(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.btn_new_open_api)


    field_open_api_title = "//input[@aria-placeholder='API Title *']"

    def put_open_api_title(self, title):
        return Action.send_keys(self, By.XPATH, OpenApi.field_open_api_title, title)

    def clear_open_api_title_field(self):
        return Action.clear_field(self, By.XPATH, OpenApi.field_open_api_title)

    update_btn = "//button[contains(text(),'Update')]"

    def click_on_update_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.update_btn)

    field_open_api_expiration_date = "//div[contains(@class,'date-editor')]/input"

    def click_on_expiration_field(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.field_open_api_expiration_date)

    calendar_current_date = "//td[@class='available today']"

    def select_on_today_in_calendar(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.calendar_current_date)


    field_bot_user = "//span[contains(@class,'cyicon-chevron-down ')]/parent::div"

    def click_on_bot_user_field(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.field_bot_user)

    btn_create = "//button[text()='Create']"

    def click_on_create_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.btn_create)

    dd_first_bot_user = "//div[@name='bot_user']//ul//li[1]"

    def click_on_first_bot_user(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.dd_first_bot_user)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, OpenApi.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, OpenApi.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.tab_All)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, OpenApi.tab_All, 'color')

    search_bar_field = "//input[@placeholder='Search or filter results']"

    def put_string_in_search_bar(self, value):
        return Action.send_keys(self, By.XPATH, OpenApi.search_bar_field, value)

    def click_enter_for_search(self):
        return Action.click_enter(self)

    top_openapi_in_listing = "(//tr//a)[1]"

    def visibility_of_first_openapi(self):
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.top_openapi_in_listing)

    def get_top_1_openapi_name(self):
        return Action.get_text(self, By.XPATH, OpenApi.top_openapi_in_listing)

    def click_on_first_openapi(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.top_openapi_in_listing)

    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.click_clear_search)

    btn_inactive_toggle = "//form//div[4]//span[text()='On ']"

    def click_inactive_toggle(self):
        return Action.javascript_click(self, By.XPATH, OpenApi.btn_inactive_toggle)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tooltip(self):
        return Action.normal_click(self, By.XPATH, OpenApi.tooltip_close)

    openapi_successful_created_msg = "//div[@class='el-notification__content']" \
                                     "//span[contains(text(),'created successful')]"

    def get_successfully_created_msg(self):
        return Action.get_text(self, By.XPATH, OpenApi.openapi_successful_created_msg)

    openapi_url_txt = "//div[contains(text(),'soarapi/')]"

    def get_api_url(self):
        return Action.get_text(self, By.XPATH, OpenApi.openapi_url_txt)

    def visibility_of_api_url(self):
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.openapi_url_txt)

    openapi_secret_key_txt = "//input[@id='copy-2']/preceding-sibling::div/span[contains(text(),'**')]"

    def visibility_of_secret_key(self):
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.openapi_secret_key_txt)

    openapi_access_id_txt = "//input[@id='copy-3']/preceding-sibling::div/span[contains(text(),'**')]"

    def visibility_of_access_id(self):
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.openapi_access_id_txt)

    secret_key_show_btn = "(//i[@class='icon-eye']/parent::span)[1]"

    def click_secret_key_show_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.secret_key_show_btn)

    access_id_show_btn = "(//i[@class='icon-eye']/parent::span)[2]"

    def click_access_id_show_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.access_id_show_btn)

    hide_btn = "//i[contains(@class,'cross icon')]/parent::span"

    def click_on_hide_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.hide_btn)

    secret_key_copy_btn = "(//i[contains(@class,'icon-documents')]/parent::span)[2]"

    def click_secret_key_copy_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.secret_key_copy_btn)

    access_id_copy_btn = "(//i[contains(@class,'icon-documents')]/parent::span)[3]"

    def click_access_id_copy_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.access_id_copy_btn)


    api_url_copy_btn = "(//i[contains(@class,'icon-documents')]/parent::span)[1]"

    def click_apiurl_copy_btn(self):
        return Action.wait_and_click(self, By.XPATH, OpenApi.api_url_copy_btn)

    copied_check_btn = "//span[@class='cursor-pointer']/i[contains(@class,'icon-check')]"

    def visibility_of_copied_check_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.copied_check_btn)

    download_keys_btn = "//i[contains(@class,'icon-download')]/parent::span"

    def visibility_of_download_keys_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.download_keys_btn)
