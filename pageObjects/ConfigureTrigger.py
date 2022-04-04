from selenium.webdriver.common.by import By
from utilities.Actions import Action


class ConfigureTrigger(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_configure_trigger = "//header//button"

    def click_new_configure_trigger_btn(self):
        """
            Click on New Configure button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.button_configure_trigger)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        """
            Get Configure Trigger page heading
            :return:
        """
        return Action.get_text(self, By.XPATH, ConfigureTrigger.text_page_heading)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_heading(self):
        """
            Get Slider heading of New Configure Trigger
            :return:
        """
        return Action.get_text(self, By.XPATH, ConfigureTrigger.text_slider_heading)

    button_close_slider = "//div[@class='modal--header']//i"

    def click_close_slider(self):
        """
            Click on close button of Configure Trigger Slider
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.button_close_slider)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        """
            Click on In-Active Tab of Configure Trigger
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.tab_inactive)

    def read_inactive_tab_color(self):
        """
            Read In-Active tab colour of Configure Trigger
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, ConfigureTrigger.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab of Configure Trigger
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.tab_All)

    def read_all_tab_color(self):
        """
            Read All tab colour of Configure Trigger
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, ConfigureTrigger.tab_All, 'color')

    source_app = "(//div[contains(@class,'cy-input')]//input)[1]"

    def put_source_app_name(self, value):
        """
            Fill Source App Name on Configure Trigger
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.source_app, value)

    def clear_source_app_name(self):
        """
            Clear Source App Name on Configure Trigger
            :return:
        """
        return Action.clear_field(self, By.XPATH, ConfigureTrigger.source_app)

    source_event_type = "(//div[contains(@class,'cy-input')]//input)[2]"

    def put_source_event_type(self, value):
        """
            Fill Source Event Type on Configure Trigger
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.source_event_type, value)

    field_labels = "//span[contains(@class,'cyicon-chevron-down')]/parent::div"

    def click_on_label_field(self):
        """
            Click on Label Field of New Configure Trigger
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.field_labels)

    input_field_labels = "//form//input[contains(@placeholder,'Search')]"

    def put_label_name(self, value):
        """
            Put Label Name on New Configure Trigger
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.input_field_labels, value)

    first_label = "//li[1]//div[contains(@class,'option-label-main')]"

    def click_first_label(self):
        """
            Click on First Label from the list of Labels drop-down
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.first_label)

    def get_top_label(self):
        """
           Select/Choose First label from the list of Labels.
            :return:
        """
        return Action.get_text(self, By.XPATH, ConfigureTrigger.first_label)

    create_btn = "//button[text()='Create']"

    def click_create_btn(self):
        """
            Click on Create button of New Configure Trigger Slider
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.create_btn)

    update_btn = "//button[text()='Update']"

    def click_on_update(self):
        """
            Click on update button of Edit Configure Trigger Slider
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.update_btn)

    text_configure_trigger_count = "//h1[contains(text(),'Configure Triggers (')]"

    def get_configure_trigger_count(self):
        """
            Get the number of Configure Triggers count.
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, ConfigureTrigger.text_configure_trigger_count)

    first_config_trigger = "(//tr[1]//div//span//a)[1]"

    def click_first_configure_trigger(self):
        """
            Click on first Configure Trigger
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.first_config_trigger)

    def get_first_configure_trigger_name(self):
        """
            Select first configure trigger from list of configure trigger
            :return:
        """
        return Action.get_text(self, By.XPATH, ConfigureTrigger.first_config_trigger)

    first_active_configured_event = "(//span[text()='Active' and @class='status__text'])[1]"

    def visibility_of_first_active_configure_trigger(self):
        """
            Check visibility of first active configure trigger
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, ConfigureTrigger.first_active_configured_event)

    first_inactive_configured_Event = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def visibility_of_first_inactive_configure_trigger(self):
        """
            Check visibility of first In-Active configure trigger
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, ConfigureTrigger.first_inactive_configured_Event)

    deactive_btn = "//span[@class='cyicon-check']"

    def click_inactive_configure_trigger(self):
        """
            Click on Inactive Configure Trigger
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.deactive_btn)

    active_btn = "//button//span[@class='cyicon-cross']"

    def click_active_configure_trigger_btn(self):
        """
            Click on active configure trigger button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.active_btn)

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        """
            Click on Actice tab of Configure Trigger
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, ConfigureTrigger.tab_active)

    main_input = "//input[@id='main-input']"

    def search_input_string(self, value):
        """
            Put Configure trigger name in search input box
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, ConfigureTrigger.main_input, value)

    def click_enter_for_search(self):
        """
            Click Enter after on Search button
            :return:
        """
        return Action.click_enter(self)

    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        """
            Clear Search box for configure triggers
            :return:
        """
        return Action.javascript_click(self, By.XPATH, ConfigureTrigger.click_clear_search)

    def select_test_syslog_label(self, value):
        """
            Select Syslog Labels
            :param value:
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, value)
