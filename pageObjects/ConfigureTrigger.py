from selenium.webdriver.common.by import By
from utilities.Actions import Action
from configuration.readConfiguration import ReadConfig

import time


class ConfigureTrigger(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_configure_trigger = "//header//button"

    def click_new_configure_trigger_btn(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.button_configure_trigger)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        return Action.get_text(self, By.XPATH, ConfigureTrigger.text_page_heading)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_heading(self):
        return Action.get_text(self, By.XPATH, ConfigureTrigger.text_slider_heading)

    button_close_slider = "//div[@class='modal--header']//i"

    def click_close_slider(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.button_close_slider)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.tab_inactive)

    def read_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, ConfigureTrigger.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.tab_All)

    def read_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, ConfigureTrigger.tab_All, 'color')

    source_app = "(//div[contains(@class,'cy-input')]//input)[1]"

    def put_source_app_name(self, value):
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.source_app, value)

    def clear_source_app_name(self):
        return Action.clear_field(self, By.XPATH, ConfigureTrigger.source_app)

    source_event_type = "(//div[contains(@class,'cy-input')]//input)[2]"

    def put_source_event_type(self, value):
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.source_event_type, value)

    field_labels = "//span[contains(@class,'cyicon-chevron-down')]/parent::div"

    def click_on_label_field(self):
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.field_labels)

    input_field_labels = "//form//input[contains(@placeholder,'Search')]"

    def put_label_name(self, value):
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.input_field_labels, value)

    first_label = "//li[1]/div[2]"

    def click_first_label(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.first_label)

    def get_top_label(self):
        return Action.get_text(self, By.XPATH, ConfigureTrigger.first_label)

    create_btn = "//div[contains(@class,'px-5 text-right')]//button"

    def click_create_btn(self):
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.create_btn)

    text_configure_trigger_count = "//h1[contains(text(),'Configure Triggers (')]"

    def get_configure_trigger_count(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.get_count_from_string(self, By.XPATH, ConfigureTrigger.text_configure_trigger_count)

    first_config_trigger = "(//tr[contains(@class, 'el-table__row')]//div//span//a)[1]"

    def click_first_configure_trigger(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.first_config_trigger)


    def get_name_first_configure_trigger(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.get_text(self, By.XPATH, ConfigureTrigger.first_config_trigger)

    active_btn = "//span[@class='cyicon-check']"

    def deactive_configure_trigger(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.active_btn)

    def click_on_update(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.create_btn)

    close_tooltip_btn = "//div[contains(@class,'notification__closeBtn')]"

    def click_close_tooltip(self):
        return Action.normal_click(self, By.XPATH, ConfigureTrigger.close_tooltip_btn)

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.tab_active)

    main_input = "//input[@id='main-input']"

    def search_input_string(self, value):
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.main_input, value)

    def click_enter_for_search(self):
        return Action.click_enter(self)

    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.click_clear_search)
