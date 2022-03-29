import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class Syslogs(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_sysLogs = "//p[contains(text(),'Syslogs')]/parent::div/parent::div"

    def click_syslogs(self):
        return Action.javascript_click(self, By.XPATH, Syslogs.tab_sysLogs)

    btn_new_syslog = "//header//button"

    def click_new_syslog(self):
        return Action.javascript_click(self, By.XPATH, Syslogs.btn_new_syslog)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, Syslogs.text_slider_heading)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, Syslogs.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Syslogs.tab_inactive, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.tab_active)

    tab_all = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.tab_all)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, Syslogs.tab_all, 'color')

    title_count = "//h1[contains(text(),'Syslogs (')]"

    def get_syslog_count(self):
        return Action.get_count_from_string(self, By.XPATH, Syslogs.title_count)

    first_active_syslog = "(//span[text()='Active' and @class='status__text'])[1]"

    def visibility_of_first_active_syslog(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, Syslogs.first_active_syslog)

    first_inactive_syslog = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def visibility_of_first_inactive_syslog(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, Syslogs.first_inactive_syslog)

    syslog_title = "(//div[contains(@class,'cy-input')]//input)[1]"

    def put_syslog_title(self, value):
        return Action.send_keys(self, By.XPATH, Syslogs.syslog_title, value)

    def clear_syslog_title(self):
        return Action.clear_field(self, By.XPATH, Syslogs.syslog_title)

    syslog_port = "(//div[contains(@class,'cy-input')]//input)[2]"

    def put_port_number(self, value):
        return Action.send_keys(self, By.XPATH, Syslogs.syslog_port, value)

    def generate_port_number(self):
        port_number = int(Action.get_random_digit(self))
        return str(port_number + 1024)

    list_source_event_apps = "//span[contains(@class,'cyicon-chevron-down')]"

    def click_on_list_Source_Events_App(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.list_source_event_apps)

    search_source_event_app = "//div[contains(@class,'webhooks')]//input[contains(@placeholder,'Search')]"

    def put_source_event_app(self, value):
        return Action.send_keys(self, By.XPATH, Syslogs.search_source_event_app, value)

    first_option_source_event_list = "(//div[contains(@class,'webhooks')]//li)[1]"

    def select_first_source_event_app_and_type(self):
        time.sleep(3)
        return Action.wait_and_click(self, By.XPATH, Syslogs.first_option_source_event_list)

    def visibility_of_first_options_in_event_list(self):
        return Action.check_visibility_of_element(self, By.XPATH, Syslogs.first_option_source_event_list)

    list_source_event_type = "(//div[contains(@class,'cy-select__menu--chevron-transform')])[2]"

    def click_on_list_Source_Events_Type(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.list_source_event_type)

    save_btn = "//div[contains(@class,'px-5 text-right')]//button"

    def click_save_btn(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.save_btn)

    three_dot = "(//i[contains(@class,'icon-more-vertical ')]/parent::span)[1]"

    def check_drop_down(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Syslogs.three_dot)

    edit_button = "//body/ul[1]/li[1]"

    def click_edit_button(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.edit_button)

    delete_button = "//body/ul[1]/li[2]"

    def click_delete_button(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.delete_button)

    deactivate_button = "//body/ul[1]/li[3]"

    def click_deactivate_button(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.deactivate_button)

    def click_activate_button(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.deactivate_button)

    main_input = "//input[@id='main-input']"

    def search_input_string(self, value):
        return Action.send_keys(self, By.XPATH, Syslogs.main_input, value)

    def click_enter_for_search(self):
        return Action.click_enter(self)

    first_syslog_name = "//tr[1]//div//span//a[1]"

    def get_name_first_syslog(self):
        return Action.get_text(self, By.XPATH, Syslogs.first_syslog_name)

    def visibility_of_first_syslog(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, Syslogs.first_syslog_name)

    def click_first_syslog(self):
        return Action.wait_and_click(self, By.XPATH, Syslogs.first_syslog_name)

    click_clear_search = "//div[contains(@class,'clear-button')]"

    def clear_search(self):
        return Action.javascript_click(self, By.XPATH, Syslogs.click_clear_search)

    syslog_status = "(//tr[@class='el-table__row']//td[7]//span[2])[1]"

    def get_status_of_syslog(self):
        return Action.get_text(self, By.XPATH, Syslogs.syslog_status)

    def select_test_syslog_source_event_app(self, value):
        return Action.wait_and_click(self, By.XPATH, value)
