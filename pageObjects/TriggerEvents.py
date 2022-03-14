from selenium.webdriver.common.by import By
from utilities.Actions import Action


class TriggerEvents(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_create_event = "//header//button"

    def click_create_new_event(self):
        return Action.wait_and_click(self, By.XPATH, TriggerEvents.button_create_event)

    field_event_title = "//form//input[@aria-placeholder='Title *']"

    def put_event_name(self, value):
        return Action.send_keys(self, By.XPATH, TriggerEvents.field_event_title, value)


    field_labels = "//div[@name='labels']//span[contains(@class,'cyicon-chevron-down')]"

    def click_on_labels_field(self):
        return Action.wait_and_click(self, By.XPATH, TriggerEvents.field_labels)

    input_field_labels = "//div[@name='labels']//input[contains(@placeholder,'Search')]"

    def enter_label_name_to_search(self, value):
        return Action.send_keys(self, By.XPATH, TriggerEvents.input_field_labels, value)

    def visibility_of_label(self, label_name):
        path = "//div[@name='labels']//li[1]//div[contains(text(),'" + label_name + "')]"
        return Action.check_visibility_of_element(self, By.XPATH, path)

    top_first_searched_label = "//div[@name='labels']//li[1]/div[2]"

    def click_on_top_label(self):
        return Action.wait_and_click(self, By.XPATH, TriggerEvents.top_first_searched_label)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        return Action.get_text(self, By.XPATH, TriggerEvents.text_page_heading)

    def get_events_count(self):
        return Action.get_count_from_string(self, By.XPATH, TriggerEvents.text_page_heading)

    search_bar = "//input[contains(@placeholder,'Search')]"

    def put_string_to_search(self, value):
        return Action.send_keys(self, By.XPATH, TriggerEvents.search_bar, value)

    def click_enter_for_search(self):
        return Action.click_enter(self)

    first_event_in_listing = "(//tbody/tr[1]/td[2]//span)[2]"

    def get_first_event_name(self):
        return Action.get_text(self, By.XPATH, TriggerEvents.first_event_in_listing)

    def click_on_first_event(self):
        return Action.wait_and_click(self, By.XPATH, TriggerEvents.first_event_in_listing)


    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        return Action.javascript_click(self, By.XPATH, TriggerEvents.click_clear_search)

    text_get_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_text(self):
        return Action.get_text(self, By.XPATH, TriggerEvents.text_get_slider_heading)

    button_close_slider = "//div[@class='modal--header']//i"

    def click_close_slider(self):
        return Action.javascript_click(self, By.XPATH, TriggerEvents.button_close_slider)

    button_create = "//button[contains(text(),'Create')]"

    def click_on_create_button(self):
        return Action.wait_and_click(self, By.XPATH, TriggerEvents.button_create)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tooltip(self):
        return Action.javascript_click(self, By.XPATH, TriggerEvents.tooltip_close)

    successful_tooltip_txt = "//div[@role='alert']//span[2]/span[1]"

    def get_successful_tooltip_txt(self):
        return Action.get_text(self, By.XPATH,TriggerEvents.successful_tooltip_txt)

