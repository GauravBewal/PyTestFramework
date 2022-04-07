from selenium.webdriver.common.by import By

from utilities.Actions import Action


class OpenApi(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_open_API = "//p[contains(text(),'Open API')]/parent::div/parent::div"

    def click_open_api_tab(self):
        """
            Click on Open API tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, OpenApi.tab_open_API)

    btn_new_open_api = "//header//i[contains(@class,'icon-plus')]/parent::button"

    def click_new_open_api_btn(self):
        """
            Click new open API button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, OpenApi.btn_new_open_api)

    field_open_api_title = "//input[@aria-placeholder='API Title *']"

    def put_open_api_title(self, title):
        """
            Put open API title
            :param title:
            :return:
        """
        return Action.send_keys(self, By.XPATH, OpenApi.field_open_api_title, title)

    def clear_open_api_title_field(self):
        """
            Clear Open API title field
            :return:
        """
        return Action.clear_field(self, By.XPATH, OpenApi.field_open_api_title)

    update_btn = "//button[contains(text(),'Update')]"

    def click_on_update_btn(self):
        """
            Click on update button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.update_btn)

    field_open_api_expiration_date = "//div[contains(@class,'date-editor')]/input"

    def click_on_expiration_field(self):
        """
            Click on expiration field
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.field_open_api_expiration_date)

    calendar_current_date = "(//td[@class='available today'])[1]"

    def select_on_today_in_calendar(self):
        """
            Select on today in calender
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.calendar_current_date)

    field_bot_user = "//span[contains(@class,'cyicon-chevron-down ')]/parent::div"

    def click_on_bot_user_field(self):
        """
            Click on bot user field
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.field_bot_user)

    btn_create = "//button[text()='Create']"

    def click_on_create_btn(self):
        """
            Click on create button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.btn_create)

    dd_first_bot_user = "//div[@name='bot_user']//ul//li[1]"

    def visibility_of_first_bot_user(self):
        """
        Visibility of first bot user
        :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.dd_first_bot_user)

    def click_on_first_bot_user(self):
        """
            Click on first bot user
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.dd_first_bot_user)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        """
            Get Slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, OpenApi.text_slider_title)

    openapi_count = "//h1[contains(text(),'Open API (')]"

    def get_openapi_count(self):
        """
            Get Open API count
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, OpenApi.openapi_count)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        """
            Click on Slider close button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, OpenApi.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        """
            Click on In-active tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.tab_inactive)

    def get_inactive_tab_color(self):
        """
            Get Inactive tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, OpenApi.tab_inactive, 'color')

    tab_Active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        """
            Click on active tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.tab_Active)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.tab_All)

    def get_all_tab_color(self):
        """
            Get All tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, OpenApi.tab_All, 'color')

    search_bar_field = "//input[@placeholder='Search or filter results']"

    def put_string_in_search_bar(self, value):
        """
            Put String in search bar
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, OpenApi.search_bar_field, value)

    def click_enter_for_search(self):
        """
            Click enter for search
            :return:
        """
        return Action.press_enter(self)

    top_openapi_in_listing = "(//tr//a)[1]"

    def get_top_1_openapi(self):
        """
            Get top first open APi
            :return:
        """
        return Action.get_text(self, By.XPATH, OpenApi.top_openapi_in_listing)

    def click_on_first_openapi(self):
        """
            Click on first Open API
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.top_openapi_in_listing)

    first_active_openapi = "(//span[text()='Active' and @class='status__text'])[1]"

    def Pass_even_first_active_openapi_is_not_visible(self):
        """
            Visibility of first Active Open API
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, OpenApi.first_active_openapi)

    first_inactive_openapi = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def Pass_even_first_inactive_openapi_is_not_visible(self):
        """
            Visibility of first InActive Open API
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, OpenApi.first_inactive_openapi)

    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        """
            Clear Search
            :return:
        """
        return Action.javascript_click(self, By.XPATH, OpenApi.click_clear_search)

    btn_inactive_toggle = "//form//div[4]//span[text()='On ']"

    def click_inactive_toggle(self):
        """
            Click In Active toggle
            :return:
        """
        return Action.javascript_click(self, By.XPATH, OpenApi.btn_inactive_toggle)

    openapi_url_txt = "//div[contains(text(),'soarapi/')]"

    def get_api_url(self):
        """
            Get API URL
            :return:
        """
        return Action.get_text(self, By.XPATH, OpenApi.openapi_url_txt)

    def visibility_of_api_url(self):
        """
            Visibility of API URL
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.openapi_url_txt)

    openapi_secret_key_txt = "//input[@id='copy-2']/preceding-sibling::div/span[contains(text(),'**')]"

    def visibility_of_secret_key(self):
        """
            Visibility of secret Key
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.openapi_secret_key_txt)

    openapi_access_id_txt = "//input[@id='copy-3']/preceding-sibling::div/span[contains(text(),'**')]"

    def visibility_of_access_id(self):
        """
            Visibility of Access ID
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.openapi_access_id_txt)

    secret_key_show_btn = "(//i[@class='icon-eye']/parent::span)[1]"

    def click_secret_key_show_btn(self):
        """
            Click on Secret Key Show Button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.secret_key_show_btn)

    access_id_show_btn = "(//i[@class='icon-eye']/parent::span)[2]"

    def click_access_id_show_btn(self):
        """
            Click on Access ID Show button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.access_id_show_btn)

    hide_btn = "//i[contains(@class,'cross icon')]/parent::span"

    def click_on_hide_btn(self):
        """
            Click on hide button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.hide_btn)

    secret_key_copy_btn = "(//i[contains(@class,'icon-documents')]/parent::span)[2]"

    def click_secret_key_copy_btn(self):
        """
            Click secret key copy button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.secret_key_copy_btn)

    access_id_copy_btn = "(//i[contains(@class,'icon-documents')]/parent::span)[3]"

    def click_access_id_copy_btn(self):
        """
            Click access ID copy button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.access_id_copy_btn)

    api_url_copy_btn = "(//i[contains(@class,'icon-documents')]/parent::span)[1]"

    def click_apiurl_copy_btn(self):
        """
            Click APi URL copy button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, OpenApi.api_url_copy_btn)

    copied_check_btn = "//span[@class='cursor-pointer']/i[contains(@class,'icon-check')]"

    def visibility_of_copied_check_btn(self):
        """
            Visibility of copied check button
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.copied_check_btn)

    download_keys_btn = "//i[contains(@class,'icon-download')]/parent::span"

    def visibility_of_download_keys_btn(self):
        """
            Visibility of download keys button
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, OpenApi.download_keys_btn)
