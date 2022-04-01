import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class Labels(Action):
    click_select_all_columns = (By.XPATH, "//button[contains(text(),'Select All Columns')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    create_new_Label = "//header//button"

    def click_new_label(self):
        """
            Click on new label button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.create_new_Label)

    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        """
            Clear search text box
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.click_clear_search)

    created_by_in_customize_table = (By.XPATH, "(//span[@class='el-checkbox__inner'])[2]")

    def select_created_by_customization(self):
        """
            Select created by Customization table slider
            :return:
        """
        return self.driver.find_element(*Labels.created_by_in_customize_table)

    modified_by_in_customize_table = (By.XPATH, "(//span[@class='el-checkbox__inner'])[4]")

    def select_modified_by_customization(self):
        """
            Select modified by customization
            :return:
        """
        return self.driver.find_element(*Labels.modified_by_in_customize_table)

    save_customized_table = (By.XPATH, "//div[@class='cy-right-model__footer']//button")

    def save_table_customization(self):
        """
            Click on Save button for table customization
            :return:
        """
        return self.driver.find_element(*Labels.save_customized_table)

    label_field_error_msg = "//div[@class='el-form-item__error']"

    def get_label_field_error_msg(self):
        """
            Get Label field error message
            :return:
        """
        return Action.get_text(self, By.XPATH, Labels.label_field_error_msg)

    label_slider_title = "//div[@class='modal--header']//span"

    def get_label_slider_title(self):
        """
            Get Create new label Slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, Labels.label_slider_title)

    click_customizable_button = (By.XPATH, "//i[@class='cyicon-settings']")

    def click_customize_table(self):
        """
            Click on customize table icon
            :return:
        """
        return self.driver.find_element(*Labels.click_customizable_button)

    click_on_close_label_slider = "//form//i[contains(@class,'el-icon-close')]"

    def close_label_slider(self):
        """
            Click on close button on label slider
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.click_on_close_label_slider)

    btn_inactive_toggle = "//form//div[4]//span[text()='On ']"

    def click_inactive_toggle(self):
        """
            Click on Inactive toggle button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.btn_inactive_toggle)

    text_box_search = "#main-input"

    def put_search_string(self, value):
        """
            Put string for label search
            :param value:
            :return:
        """
        return Action.send_keys(self, By.CSS_SELECTOR, Labels.text_box_search, value)

    def click_enter_for_search(self):
        """
            Click enter for search
            :return:
        """
        return Action.click_enter(self)

    top_label_in_listing = "(//tr//a)[1]"

    def get_top_1_label_name(self):
        """
            Get Top first label name from list of table
            :return:
        """
        return Action.get_text(self, By.XPATH, Labels.top_label_in_listing)

    def click_top_first_label(self):
        """
            Click on top first label name
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.top_label_in_listing)

    first_active_label = "(//span[text()='Active' and @class='status__text'])[1]"

    def visibility_of_first_active_label(self):
        """
            Visibility of first active label
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, Labels.first_active_label)

    first_inactive_label = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def visibility_of_first_inactive_label(self):
        """
            Visibility of first in-active label
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, Labels.first_inactive_label)

    label_created_user = "//tbody/tr[1]/td[2]"

    def get_label_created_user(self):
        """
            get label created by username
            :return:
        """
        return Action.get_text(self, By.XPATH, Labels.label_created_user)

    label_modified_user = "//tbody/tr[1]/td[4]"

    def get_label_modified_user(self):
        """
            Get label modified by username
            :return:
        """
        return Action.get_text(self, By.XPATH, Labels.label_modified_user)

    tab_inActive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        """
            Click on inactive tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.tab_inActive)

    def get_inactive_tab_color(self):
        """
            Click on inactive tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, Labels.tab_inActive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.tab_All)

    def get_all_tab_color(self):
        """
            Get all tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, Labels.tab_All, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        """
            Click on active tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.tab_active)

    button_sort = (By.XPATH, "//span[contains(text(),'Sort')]")

    def click_sort(self):
        """
            Click on sort
            :return:
        """
        return self.driver.find_element(*Labels.button_sort)

    text_box_Label_Name = "//input[@aria-placeholder='Label Name']"

    def put_label_name(self, value):
        """
            put label name in text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, Labels.text_box_Label_Name, value)

    def clear_label_field(self):
        """
            Clear label text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, Labels.text_box_Label_Name)

    button_update = "//button[text()='Update']"

    def click_update_label(self):
        """
            Click on update label button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.button_update)

    text_box_Description = "//textarea[@aria-placeholder='Description']"

    def put_description(self, value):
        """
            Put description on text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, Labels.text_box_Description, value)

    def clear_description_field(self):
        """
            Clear description text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, Labels.text_box_Description)

    get_labels_count = "//h1[contains(text(),'Labels (')]"

    def get_label_count(self):
        """
            Get label's total count
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, Labels.get_labels_count)

    button_create = "//button[text()='Create']"

    def create_Label(self):
        """
            Click on create label button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Labels.button_create)
